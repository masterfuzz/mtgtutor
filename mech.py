import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

#br.set_proxies({"http": "fastweb.int.bell.ca:80", "https": "fastweb.int.bell.ca:80"})




#list = soup.find('table', attrs={'class': 'Stable'})



br.open("http://www.mtgtop8.com/format?f=ST")

decks = []

list = br.links(url_regex="archetype")
for arch in list:
	print(str(arch))
	try:
		br.follow_link(arch)
		for deck in br.links(url_regex="event"):
			decks.append(deck)

	except Exception:
		pass


#for deck in decks:
deck = decks[0]
br.follow_link(deck)
soup = BeautifulSoup(br.response().read())
cards = soup.findAll('span', attrs={'class': 'L14'})


for card in cards:
	print(card.children[0])
	print("\n")





	
