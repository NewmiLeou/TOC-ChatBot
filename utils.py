import requests
from bs4 import BeautifulSoup
import re
import urllib


GRAPH_URL = "https://graph.facebook.com/v3.2"
ACCESS_TOKEN = "EAAJaS0gGToQBAL3emRRJHUxbUBWrevi9PXbQ4C6ZCqgDo0qsdhqZCDpxCGJyHAB5RgoifZBZBEBZCSKx4skf4gFZBGhumoYzZASOAboPSYZBMJJCTSltKNImrqrbRh3QxI7wr16ZBQQ1kjOpmsR4OqP8vFtEVmH9xMlDZCryUbQNBZCcwZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
            "attachment":{
                "type":"image",
                "payload":{
                    "url":img_url,
                    "is_reusable":"true"
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response
    
def send_button_message(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":text,
                    "buttons":buttons
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


#jordan
def get_jordan_pop_name(series):
    url = 'https://stockx.com/retro-jordans/air-jordan-%d/most-popular'%series
    res = requests.get(url)
    soup = BeautifulSoup(res.text,features='lxml')
    div = soup.find('div',{'class':'img image-link'})
    pop = div.findAll('img')[0]['alt']
    return pop

def get_jordan_pop_img(series):
    url = 'https://stockx.com/retro-jordans/air-jordan-%d/most-popular'%series
    res = requests.get(url)
    soup = BeautifulSoup(res.text,features='lxml')
    div = soup.find('div',{'class':'img image-link'})
    pop = div.findAll('img')[0]['src']
    return pop

def get_jordan_price(series):
    url = 'https://stockx.com/retro-jordans/air-jordan-%d/most-popular'%series
    res = requests.get(url)
    soup = BeautifulSoup(res.text,features='lxml')
    div = soup.find('div',{'class':'price-line'})
    price = div.findAll('div')[1].string
    return price

#adidas
def get_adidas_pop_name(series):
    url = 'https://stockx.com/adidas/%s/most-popular'%series
    res = requests.get(url)
    soup = BeautifulSoup(res.text,features='lxml')
    div = soup.find('div',{'class':'img image-link'})
    pop = div.findAll('img')[0]['alt']
    return pop

def get_adidas_pop_img(series):
    url = 'https://stockx.com/adidas/%s/most-popular'%series
    res = requests.get(url)
    soup = BeautifulSoup(res.text,features='lxml')
    div = soup.find('div',{'class':'img image-link'})
    pop = div.findAll('img')[0]['src']
    return pop

def get_adidas_price(series):
    url = 'https://stockx.com/adidas/%s/most-popular'%series
    res = requests.get(url)
    soup = BeautifulSoup(res.text,features='lxml')
    div = soup.find('div',{'class':'price-line'})
    price = div.findAll('div')[1].string
    return price

#nike
def get_nike_pop_name(series):
    url = 'https://stockx.com/nike/%s/most-popular'%series
    res = requests.get(url)
    soup = BeautifulSoup(res.text,features='lxml')
    div = soup.find('div',{'class':'img image-link'})
    pop = div.findAll('img')[0]['alt']
    return pop

def get_nike_pop_img(series):
    url = 'https://stockx.com/nike/%s/most-popular'%series
    res = requests.get(url)
    soup = BeautifulSoup(res.text,features='lxml')
    div = soup.find('div',{'class':'img image-link'})
    pop = div.findAll('img')[0]['src']
    return pop

def get_nike_price(series):
    url = 'https://stockx.com/nike/%s/most-popular'%series
    res = requests.get(url)
    soup = BeautifulSoup(res.text,features='lxml')
    div = soup.find('div',{'class':'price-line'})
    price = div.findAll('div')[1].string
    return price
