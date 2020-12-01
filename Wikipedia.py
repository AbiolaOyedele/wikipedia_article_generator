#importing libraries

import Wikipedia
from bs4 import BeautifulSoup as soup
import webbrowser 
import requests
import string


#random wikipedia page

while True:
    print("Welcome!!!\n\nAre you ready to find something new on wikipedia?\n\n")
    random_wiki = "https://en.wikipedia.org/wiki/Special:Random"
    get_requests = requests.get(random_wiki)
    soups = soup(get_requests.content , "html.parser")
    title = soups.find(id ="firstHeading").text
    print ("Who you like to read about {}? (Yes/No)".format(title))
    answer = str(input("")) 

    if (answer.lower() == "y" or answer.lower() == "yes"):
        page = soups.find(class_ = "mw-parser-output").text
        print("Do You want to open in browser? (Yes/No)")
        ans = str(input("")) 
        if (ans.lower() == "y" or ans.lower() == "yes"):
            
            url = 'https://en.wikipedia.org/wiki/%s' %title
            webbrowser.open(url)
        elif (ans.lower() == "n" or ans.lower() == "no"):
            
            print(page)
        
    elif (answer.lower() == "n" or answer.lower() == "no"): 

        print("Okay,Let's Find Something Else!!!")
        continue

    elif (answer.lower() == "end" or answer.lower() == "end"):

        break
    else:
        print("Good Bye!!")
        break
 
 #Current events on wikipedia

while True:
    print("Welcome!!!\n\nWould you like to read Current events on Wikipedia?\n\n")
    current_events = "https://en.wikipedia.org/wiki/Portal:Current_events"
    events_requests = requests.get(current_events)
    soups = soup(events_requests.content , "html.parser")
    title = soups.find(id ="firstHeading").text
    print ("Who you like to read about {}? (Yes/No)".format(title))
    answer = str(input("")) 

    if (answer.lower() == "y" or answer.lower() == "yes"):
        page = soups.find(class_ = "mw-parser-output").text
        print("This is better viewed in browser, Continue? (Yes/No)")
        ans = str(input("")) 
        if (ans.lower() == "y" or ans.lower() == "yes"):
            
            url = 'https://en.wikipedia.org/wiki/%s' %title
            webbrowser.open(url)
        elif (ans.lower() == "n" or ans.lower() == "no"):
            
            print(page)
        
    elif (answer.lower() == "n" or answer.lower() == "no"): 

        print("Okay,Let's Find Something Else!!!")

        
        continue

    elif (answer.lower() == "end" or answer.lower() == "end"):

        break
    else:
        print("Good Bye!!")
        break

#Article for a specific month and year

while True:
    print("Welcome!!!\n\nWould you like to find events that occured in a particular Month and Year on Wikipedia? (YES/NO) \n\n")
    answer = str(input("")) 

    if (answer.lower() == "y" or answer.lower() == "yes"):
        
        month = str(input("Enter Specific Month e.g August: ")) 
        #capitalize the first letter of the word inputted
        month_string = string.capwords(month)
        year = int(input("Enter Specific Year from 1994 till date: ")) 
        specific_events = "https://en.wikipedia.org/wiki/Portal:Current_events/"
        specific_requests = requests.get(specific_events)
        soups = soup(specific_requests.content , "html.parser")
        print ("You would like to read articles from {} {} ? (Yes/No)".format(month_string , year))
        reply = str(input("")) 

        if (reply.lower() == "y" or reply.lower() == "yes"):
            page_url = 'https://en.wikipedia.org/wiki/%s_%s' %(month_string ,year)
            webbrowser.open(page_url)
        elif (reply.lower() == "n" or reply.lower() == "no"):

            break
        
    else:
        print("Good Bye!!")
        break


