import urllib.request
import re
from bs4 import BeautifulSoup

print ("we will try to open this url, in order to get IP Address")

url = "http://checkip.dyndns.org"

print (url)

request = urllib.request.urlopen(url).read()
my_HTML = request.decode("utf8")
soup = BeautifulSoup(my_HTML, 'html.parser')
print(soup.get_text())
body = soup.find('body')
print(f"Body is: {body}")
print(soup)
the_contents_of_body_without_body_tags = body.findChildren()

print(f"Request is: {my_HTML}")
print ("your IP Address is: ",  the_contents_of_body_without_body_tags)
print ("your IP Address is: ",  body)

unwrap=soup.body.get_text()

print(f"unwrap variable: {unwrap}")