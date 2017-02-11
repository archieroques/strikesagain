import urllib2
#imports the library we need for web addresses

from bs4 import BeautifulSoup
#imports the webscraping library

import time
#imports the time library

import gpiozero
#imports the GPIO zero library for interfacing with an LED

red = gpiozero.LED(13)
amber = gpiozero.LED(19)
green = gpiozero.LED(26)
#defines each colour of LED on the Pi-Stop


while True:
    #run this code forever

    red.off()
    amber.off()
    green.off()
    #turns off all the LEDs to start again

    page = urllib2.urlopen('YOUR_URL_GOES_HERE')
    #opens the page - example URL: http://www.realtimetrains.co.uk/search/advanced/CBG/to/ELY?stp=WVS&show=pax-calls&order=wtt

    scraped = BeautifulSoup(page)
    #scrapes the data from the page

    scraped = str(scraped)
    #makes sure it's a string

    scraped = "".join(scraped.split())
    #removes all the spaces

    index = scraped.find('YOUR_IDENTIFIER_GOES_HERE')
    #finds the identifier value's position -example identifier: realtimeactual

    index = index + YOUR_INDEX_GOES_HERE
    #adds 16 to get to the start value of the time - example index addition is 16

    traintime = scraped[index:(index+4)]
    #finds and extracts the time from the code

    traintime = 2150

    currenttime = time.strftime('%H%M', time.gmtime())
    #gets the current time in HHMM format

    timeuntiltrain = int(traintime) - int(currenttime)
    #calculates the difference between the current time, and the time the train'll leave

    message = 'Train arriving in ' + str(timeuntiltrain) + ' minutes!'
    #creates the message to print

    print('Train arriving in ' + str(timeuntiltrain), '  minutes!')
    #prints out the traintime

    if timeuntiltrain > 15:
        #if there's more than 15 mins till the next train:
        red.on()
        #turn on the red LED
    elif timeuntiltrain >= 5:
        #if the time till the next train is 5 or more mins:
        amber.on()
        #light the amber LED
    elif timeuntiltrain < 5:
        #if it's under 5 mins;
        green.on()
        #turn on the green LED

    time.sleep(60)

