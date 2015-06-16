# helper module for getting information about cards from mtgdb

from json import loads
import urllib2

# connection info
_url = 'http://api.mtgdb.info/'

def _get(arg):
	return loads(urllib2.urlopen(_url + arg).read())


def search(name):
	return _get("search/%s?start=0&limit=2" % name)


card = search("Cranial Archive")
