
from bs4 import BeautifulSoup
import urllib2
import html5lib
quote_page = 'http://lewicpro.net/index.php/2017/01/03/how-to-install-your-own-cloud/'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html5lib')
name_box = soup.find('h4', attrs = {'class': 'widgettitle'})
name = name_box.txt.strip()
print name