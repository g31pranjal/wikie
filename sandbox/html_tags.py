from HTMLParser import HTMLParser
from bs4 import BeautifulSoup as bs


class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.strict = False
		self.convert_charrefs= True
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()


def main():
	fhandle = open('fsg342s.raw', 'r')
	a = fhandle.read()


	print strip_tags(a)


def me_mem() :
	fhandle = open('fsg342s.raw', 'r')
	a = fhandle.read()

	soup = bs(a, 'html.parser')
	x = soup.find("div", {'id' : 'mw-content-text'}, { 'class' : 'mw-content-ltr' })

	# remove all hatnotes
	for child in x.find_all("div", class_="hatnote") :
		child.extract()

	# remove infobox
	for child in x.find_all("table", class_="infobox") :
		child.extract()

	# remove infobox
	for child in x.find_all("table", class_="plainlinks") :
		child.extract()

	# remove table of contents
	for child in x.find_all("div", {'id' : 'toc'}) :
		child.extract()

	# remove all image placeholders
	for child in x.find_all("div", class_="thumb") :
		child.extract()

	# remove all references
	for child in x.find_all("div", class_="reflist") :
		child.extract()

	print strip_tags(str(x))

me_mem()