from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url
from utils import send_button_message
from utils import get_jordan_pop_name
from utils import get_jordan_pop_img
from utils import get_jordan_price
from utils import get_adidas_pop_name
from utils import get_adidas_pop_img
from utils import get_adidas_price
from utils import get_nike_pop_name
from utils import get_nike_pop_img
from utils import get_nike_price
from utils import get_yeezy_pop_name
from utils import get_yeezy_pop_img
from utils import get_yeezy_price
from utils import get_street_pop_name
from utils import get_street_pop_img
from utils import get_street_price


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_jordan(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'air jordan'
        return False

    def is_going_to_jordan1(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'air jordan1'
        return False
    
    def is_going_to_jordan4(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'air jordan4'
        return False
    
    def is_going_to_jordan11(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'air jordan11'
        return False

    def is_going_to_adidas(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'adidas'
        return False
    
    def is_going_to_iniki(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'iniki'
        return False
    
    def is_going_to_ultra(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'ultra boost'
        return False
    
    def is_going_to_nmd(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'nmd'
        return False
    
    def is_going_to_nike(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'nike'
        return False
    
    def is_going_to_airforce(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'air force'
        return False
    
    def is_going_to_airmax(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'air max'
        return False

    def is_going_to_basketball(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'basketball'
        return False

    def is_going_to_yeezy(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'yeezy'
        return False
    
    def is_going_to_350(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'yeezy 350'
        return False
    
    def is_going_to_500(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'yeezy 500'
        return False
    
    def is_going_to_700(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text.lower() == 'yeezy 700'
        return False
    
    def is_going_to_recommend(self, event):
        if event.get("message"):
            if event['message'].get('text'):
                text = event['message']['text']
                return text.lower() == 'recommend me some streetwear to fit this shoe'
        return False

    #jordan
    def on_enter_jordan(self, event):
        print("I'm entering jordan")

        buttons = [
                    {
                        "type": "postback",
                        "title": "Air Jordan1",
                        "payload": "Air Jordan1" 
                        
                    },
                    {
                        "type": "postback",
                        "title": "Air Jordan4",
                        "payload": "Air Jordan4" 
                        
                    },
                    {
                        
                        "type": "postback",
                        "title": "Air Jordan11",
                        "payload": "Air Jordan11" 
                    }
        ]
        sender_id = event['sender']['id']
        responese = send_button_message(sender_id,"These three series are popular recently🔥\nWhich series do you what to find?",buttons)
        #self.go_back()

    #jordan1
    def on_enter_jordan1(self, event):
        print("I'm entering jordan1")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/retro-jordans/air-jordan-1",
                        "title": "See more Air Jordan1"
                    },
        ]
        name = get_jordan_pop_name(1)
        img_url = get_jordan_pop_img(1)
        price = get_jordan_price(1)
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in Air Jordan1 series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more Air Jordan1 series"
                                                    ,buttons)
        


    #jordan4
    def on_enter_jordan4(self, event):
        print("I'm entering jordan4")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/retro-jordans/air-jordan-4",
                        "title": "See more Air Jordan4"
                    },
                    {
                        "type": "postback",
                        "title":"Choose some streetwear to fit this shoe!",
                        "title": "Choose some streetwear to fit this shoe!"
                    }
        ]
        name = get_jordan_pop_name(4)
        img_url = get_jordan_pop_img(4)
        price = get_jordan_price(4)
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in Air Jordan4 series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more Air Jordan4 series"
                                                    ,buttons)
       

    #jordan11
    def on_enter_jordan11(self, event):
        print("I'm entering jordan11")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/retro-jordans/air-jordan-11",
                        "title": "See more Air Jordan11"
                    }
        ]
        name = get_jordan_pop_name(11)
        img_url = get_jordan_pop_img(11)
        price = get_jordan_price(11)
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in Air Jordan11 series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more Air Jordan11 series"
                                                    ,buttons)
        

    #adidas
    def on_enter_adidas(self, event):
        print("I'm entering adidas")

        buttons = [
                    {
                        "type": "postback",
                        "title": "Iniki",
                        "payload": "Iniki" 
                        
                    },
                    {
                        "type": "postback",
                        "title": "Ultra Boost",
                        "payload": "Ultra Boost" 
                        
                    },
                    {
                        
                        "type": "postback",
                        "title": "NMD",
                        "payload": "NMD" 
                    }
        ]
        sender_id = event['sender']['id']
        responese = send_button_message(sender_id,"These three series are popular recently🔥\nWhich series do you what to find?",buttons)
        #self.go_back()

    #yeezy
    def on_enter_iniki(self, event):
        print("I'm entering iniki")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/adidas/yeezy",
                        "title": "See more Iniki"
                    }
        ]
        name = get_adidas_pop_name("iniki")
        img_url = get_adidas_pop_img("iniki")
        price = get_adidas_price("iniki")
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in Iniki series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more Iniki series"
                                                    ,buttons)
       
    
    #ultra
    def on_enter_ultra(self, event):
        print("I'm entering ultra")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/adidas/ultra-boost",
                        "title": "See more Ultra Boost"
                    }
        ]
        name = get_adidas_pop_name("ultra-boost")
        img_url = get_adidas_pop_img("ultra-boost")
        price = get_adidas_price("ultra-boost")
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in Ultra Boost series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more Ultra Boost series"
                                                    ,buttons)
        

    #nmd
    def on_enter_nmd(self, event):
        print("I'm entering nmd")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/adidas/nmd",
                        "title": "See more NMD"
                    }
        ]
        name = get_adidas_pop_name("nmd")
        img_url = get_adidas_pop_img("nmd")
        price = get_adidas_price("nmd")
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in NMD series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more NMD series"
                                                    ,buttons)



    #nike
    def on_enter_nike(self, event):
        print("I'm entering nike")

        buttons = [
                    {
                        "type": "postback",
                        "title": "Air Force",
                        "payload": "Air Force" 
                        
                    },
                    {
                        "type": "postback",
                        "title": "Air Max",
                        "payload": "Air Max" 
                        
                    },
                    {
                        
                        "type": "postback",
                        "title": "Basketball",
                        "payload": "Basketball" 
                    }
        ]
        sender_id = event['sender']['id']
        responese = send_button_message(sender_id,"These three series are popular recently🔥\nWhich series do you what to find?",buttons)
        #self.go_back()

    #air force
    def on_enter_airforce(self, event):
        print("I'm entering air force")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/nike/air-force/most-popular",
                        "title": "See more Air Force"
                    }
        ]
        name = get_nike_pop_name("air-force")
        img_url = get_nike_pop_img("air-force")
        price = get_nike_price("air-force")
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in Air Force series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more Air Force series"
                                                    ,buttons)
       

    #air max
    def on_enter_airmax(self, event):
        print("I'm entering air max")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/nike/air-max/most-popular",
                        "title": "See more Air Max"
                    }
        ]
        name = get_nike_pop_name("air-max")
        img_url = get_nike_pop_img("air-max")
        price = get_nike_price("air-max")
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in Air Max series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more Air Max series"
                                                    ,buttons)
       

    #basketball
    def on_enter_basketball(self, event):
        print("I'm entering basketball")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/nike/basketball/most-popular",
                        "title": "See more Basketball"
                    }
        ]
        name = get_nike_pop_name("basketball")
        img_url = get_nike_pop_img("basketball")
        price = get_nike_price("basketball")
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in Basketball series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more Basketball series"
                                                    ,buttons)
    
    #yeezy
    def on_enter_yeezy(self, event):
        print("I'm entering yeezy")

        buttons = [
                    {
                        "type": "postback",
                        "title": "YEEZY 350",
                        "payload": "YEEZY 350" 
                        
                    },
                    {
                        "type": "postback",
                        "title": "YEEZY 500",
                        "payload": "YEEZY 500" 
                        
                    },
                    {
                        
                        "type": "postback",
                        "title": "YEEZY 700",
                        "payload": "YEEZY 700" 
                    }
        ]
        sender_id = event['sender']['id']
        responese = send_button_message(sender_id,"These three series are popular recently🔥\nWhich series do you what to find?",buttons)
        

    #350
    def on_enter_350(self, event):
        print("I'm entering 350")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/adidas/yeezy/350/most-popular",
                        "title": "See more YEEZY 350"
                    }
        ]
        name = get_yeezy_pop_name(350)
        img_url = get_yeezy_pop_img(350)
        price = get_yeezy_price(350)
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in YEEZY 350 series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more YEEZY 350 series"
                                                    ,buttons)
   


    #500
    def on_enter_500(self, event):
        print("I'm entering 500")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/adidas/yeezy/500/most-popular",
                        "title": "See more YEEZY 500"
                    }
        ]
        name = get_yeezy_pop_name(500)
        img_url = get_yeezy_pop_img(500)
        price = get_yeezy_price(500)
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in YEEZY 500 series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more YEEZY 500 series"
                                                    ,buttons)
      


    #700
    def on_enter_700(self, event):
        print("I'm entering 700")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/adidas/yeezy/700/most-popular",
                        "title": "See more YEEZY 700"
                    }
        ]
        name = get_yeezy_pop_name(700)
        img_url = get_yeezy_pop_img(700)
        price = get_yeezy_price(700)
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular shoes in YEEZY 700 series🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more YEEZY 700 series"
                                                    ,buttons)
   

    
    #recommend
    def on_enter_recommend(self, event):
        print("I'm entering recommend")

        sender_id = event['sender']['id']
        buttons = [
                    {
                        "type": "web_url",
                        "url":"https://stockx.com/streetwear/most-popular",
                        "title": "See more Streetwear"
                    }
        ]
        name = get_street_pop_name()
        img_url = get_street_pop_img()
        price = get_street_price()
        send_image_url(sender_id, img_url)
        responese = send_button_message(sender_id,"This is the most popular streetwear recently🔥\n👟Name : "+name+"\n" \
                                                    "💸Price : US"+price+"\n👇🏻Click the button below to see more Streetwear"
                                                    ,buttons)
        self.go_back()

    def on_exit_recommend(self):
        print('Leaving recommend')
    