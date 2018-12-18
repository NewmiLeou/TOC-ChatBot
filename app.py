from bottle import route, run, request, abort, static_file

from fsm import TocMachine
# -*- coding: UTF-8 -*-


VERIFY_TOKEN = "newmileou"
machine = TocMachine(
    states=[
        'user',
        'jordan',
        'jordan1',
        'jordan4',
        'jordan11',
        'adidas',
        'yeezy',
        'ultra',
        'nmd',
        'nike',
        'airforce',
        'airmax',
        'basketball'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'jordan',
            'conditions': 'is_going_to_jordan'
        },
        {
            'trigger': 'advance',
            'source': 'jordan',
            'dest': 'jordan1',
            'conditions': 'is_going_to_jordan1'
        },
        {
            'trigger': 'advance',
            'source': 'jordan',
            'dest': 'jordan4',
            'conditions': 'is_going_to_jordan4'
        },
        {
            'trigger': 'advance',
            'source': 'jordan',
            'dest': 'jordan11',
            'conditions': 'is_going_to_jordan11'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'adidas',
            'conditions': 'is_going_to_adidas'
        },
        {
            'trigger': 'advance',
            'source': 'adidas',
            'dest': 'yeezy',
            'conditions': 'is_going_to_yeezy'
        },
        {
            'trigger': 'advance',
            'source': 'adidas',
            'dest': 'ultra',
            'conditions': 'is_going_to_ultra'
        },
        {
            'trigger': 'advance',
            'source': 'adidas',
            'dest': 'nmd',
            'conditions': 'is_going_to_nmd'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'nike',
            'conditions': 'is_going_to_nike'
        },
        {
            'trigger': 'advance',
            'source': 'nike',
            'dest': 'airforce',
            'conditions': 'is_going_to_airforce'
        },
        {
            'trigger': 'advance',
            'source': 'nike',
            'dest': 'airmax',
            'conditions': 'is_going_to_airmax'
        },
        {
            'trigger': 'advance',
            'source': 'nike',
            'dest': 'basketball',
            'conditions': 'is_going_to_basketball'
        },
        {
            'trigger': 'go_back',
            'source': [
                'jordan1',
                'jordan4',
                'jordan11',
                'yeezy',
                'ultra',
                'nmd',
                'airforce',
                'airmax',
                'basketball'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
