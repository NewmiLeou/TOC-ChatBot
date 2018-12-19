# TOC-ChatBot
Final Program for TOC class

A Facebook messenger bot based on a finite state machine



## Features
### Button
* web_url button
* postback button

### Image
* It can send image of the collection

### Web Crawler
* Use BeautifulSoup to crawl stockX website info



## Finite State Machine
![fsm](fsm.png)



## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will trigger `is_going_to_jordan` or `is_going_to_adidas` or `is_going_to_nike` or `is_going_to_yeezy`.

* user
	* Input: "air jordan"
	* Reply: 
		
	![air jordan](jordan.png)

	* Input: "adidas"
		* Reply: 
	
	* Input: "nike"
		* Reply: 
	
	* Input: "yeezy"
		* Reply: 




## Reference
[stockX](https://stockx.com/) 
