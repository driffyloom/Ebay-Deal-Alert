import requests
from bs4 import BeautifulSoup

##page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
##
##soup = BeautifulSoup(page.content, 'html.parser')
##
###prints out the 3 tags at the top level (everything)
##print(list(soup.children))
##
##html = list(soup.children)[2]
##
###prints out the children of the html level
##print(list(html.children))
##
##body = list(html.children)[3]
##
###prints out all the children of the body level
##print(list(body.children))
##
##p = list(body.children)[1]
##
###now we can isolate the p tag and get all the text from it
##print(p.get_text())
##
###to find all instances of a tag use soup.find_all('p')
##print(soup.find_all('p')[0].get_text())

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

soup = BeautifulSoup(page.content, 'html.parser')
#print(list(soup.find_all(class_ = 'outer-text')))
#print(list(soup.find_all(id="first")))

#use select instead of find_all to search a page with css selectors

##    css selectors
##    p a — finds all a tags inside of a p tag.
##    body p a — finds all a tags inside of a p tag inside of a body tag.
##    html body — finds all body tags inside of an html tag.
##    p.outer-text — finds all p tags with a class of outer-text.
##    p#first — finds all p tags with an id of first.
##    body p.outer-text — finds any p tags with a class of outer-text inside
##    of a body tag.

#will find all p tags within a div
print(soup.select("div p"))
