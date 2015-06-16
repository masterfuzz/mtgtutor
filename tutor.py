#!/bin/python
import mtg

class Card:
	def __init__(self):
		#default card
		self.name = "Blank"

	def __init__(self, name):
		self = Card.GetCard(name)

	def GetCard(name):
		res = mtg.search(name)
		if len(res) == 1:
			newCard = Card()
			for att in ('name', 'type',...):
				newCard.__dict__[att] = res[0][att]
		else:
			raise Exception("%s cards returned instead of 1!" % len(res))
		return newCard

