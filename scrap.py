# Get job title location and Date all plain text no tags


import requests    # Imports the python request library

from bs4 import BeautifulSoup as souper      # imports beautiful soup from beautiful soup and renames it to a simpler term "souper"

URL = "https://realpython.github.io/fake-jobs/"         # The URL that is being accesed and scraped 
page = requests.get(URL)                                # Sends a request to the URL 

soup = souper(page.content,"html.parser")               # Pulls all of the html from the url request


Job_title = soup.find_all(class_='title is-5')          # Finds all the tags where job titles are stored in 

Job_location = soup.find_all(class_ = "location")       # Finds all tags with job locations 

Job_date = soup.find_all("time")                        # Finds all the tags with the job posted date 



for (title, location, date) in zip(Job_title, Job_location, Job_date):              # For loop that uses the zip function to bundle all the data together and prints them all out in blocks 
    print(title.text,  )
    print(location.get_text().strip())                                              # Pulls the text and removes the html tags and .strip removes the whitespace/padding
    print(date.get_text().strip())
    print("\n")                                                                     # prints a empty line to separate the blocks from each other. 
