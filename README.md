# TOC-ChatBot
Final Program for TOC class

A Facebook messenger bot based on a finite state machine



## Features

### Button
* web_url button
* postback button

### Image


### Web Crawler
* BeautifulSoup



## Finite State Machine
![fsm](fsm.png)



## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"




## Reference
[stockX](https://stockx.com/) 
