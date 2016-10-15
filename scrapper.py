import lxml.html as lh
import requests
import urllib2

url = 'https://en.wikipedia.org/wiki/India'

doc = lh.parse(urllib2.urlopen(url))

print doc