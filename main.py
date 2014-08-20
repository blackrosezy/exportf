import nltk
from bs4 import BeautifulSoup

xml = open('data/AdviceCreator.xml', 'r').read()
soup = BeautifulSoup(xml, "xml")
for obj in soup.find_all("object", attrs={"type": "SubPage"}):

    top_nav = obj.find('object',recursive=False)
    if not top_nav:
        continue

    print top_nav.get('title')
    print '=================='

    for obj2 in top_nav.find_all('fields',attrs={"type": "List"},recursive=False):
        for field in obj2.find_all('object',recursive=False):
            val = field.object
            if val != None:
                title = val.get('title')
                name = val.get('name')
                if title == None:
                    title = val.get('alternative_title')
                if title == "Field":
                    title = val.get('alternative_title')
                print '    \t[%-5s] {%-65s} %s' % (field.get('type'),name, nltk.clean_html(title))
        print ''