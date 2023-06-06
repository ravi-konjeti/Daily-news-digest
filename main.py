import requests
import spark
import send_email as se

"""
The apis are application program interface where we data 
is seen by user in visual format in a website
However, a webstie in the backend for the data of the news
uses a webapi which has code in json data 
so the front end program should understand the backed webapi data
and should be able to show that in clean visualization
We used NwesAPI.org where we get the API DATA from this website'
and we build a code that can interpret the json data of news 
and make it into a proper readable format and sends the 
news through email
"""

topic = "tesla"

api_key = "11a66b6e97a84a61b3688f877f8f8704"
# By using this we saved all the json data into url variable
# where now we can make use of that data
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=11a66b6e97a84a61b3688f877f8f8704&" \
      "language=en"

request = requests.get(url)

# This brings the data in string format which is unusable
# content = request.text
# Now we bought data from url in form of dictionary
content = request.json()

body = ""
# Accessed the article titles and description
for article in content["articles"]:

      body ="Subject: Today's news" + "\n" +\
            body + article["title"] + "\n" +\
            article["description"] + "\n"+ article["url"] + 2 * "\n"

# we had to change the string data to utf-8 because we were getting an ascii error
# so we changed the encoding of data
body = body.encode('utf-8')
se.send_email(body)
print("Email_sent")
