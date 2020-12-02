import urllib.request
from bs4 import BeautifulSoup

url = "http://checkip.dyndns.org"
request = urllib.request.urlopen(url).read().decode("utf8")
soup_body = BeautifulSoup(request, 'html.parser').find('body').get_text()

print(soup_body)