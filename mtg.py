# helper module for getting information about cards from mtgdb

from json import loads
import urllib2

# connection info
_url = 'http://api.mtgdb.info/'

def _get(arg):
	return loads(urllib2.urlopen(_url + arg).read())


def search(name):
	return _get("search/%s?start=0&limit=2" % name)

def byID(uid):
	pass


def confer(uid):
	# get gatherer comments and return list of card links
	br.open("http://gatherer.wizards.com/Pages/Card/Discussion.aspx?multiverseid=%s" % uid)
	cf = []
	
	for link in br.links(url_regex="Details.aspx.name"):
		cf.append(search(link.text))

	#TODO other comment pages
	return cf


card = search("Cranial Archive")
