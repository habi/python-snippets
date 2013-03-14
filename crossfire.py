# -*- coding: utf-8 -*-

"""
                  *Cr*appy *O*pen *S*ource *S*oftware:
                 *F*eedreader *I*n *R*esponse to *E*van

This aims to be the 'crappiest Open Source RSS client' to have less
'features than Google Reader' on July 2nd 2013. It's supposed to be
funny: http://goo.gl/b9zdm

Copyright 2013 David Haberthür

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from optparse import OptionParser
import sys
import feedparser
import urllib
import time

# Use Pythons Optionparser to define and read the options, and also
# give some help to the user
parser = OptionParser()
usage = "usage: %prog [options] arg"
parser.add_option('-f', '--Feed', dest='Feed',
				  help='URL of the feed you want to read',
				  metavar='URL')
(options, args) = parser.parse_args()

# show the help if no parameters are given
if options.Feed is None:
	parser.print_help()
	print 'Example:'
	print 'The command below reads the Atom feed of http://identi.ca'
	print ''
	print (sys.argv[0],
		   '-f http://identi.ca/api/statuses/public_timeline.atom')
	print
	sys.exit(1)

starttime = time.time()
eol = time.mktime((2013, 7, 1, 0, 0, 0, 0, 0, -1))

if starttime > eol:
        print 'Sorry, this product has reached its end of life.'
	sys.exit(1)
        
print ('The current time is',
	   time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.localtime()))
print

# Copied from http://pythonhosted.org/feedparser/atom-detail.html and
# http://pythonhosted.org/feedparser/common-atom-elements.html
f = feedparser.parse(options.Feed)
print 'The feed you submitted is titled "' + f.feed.title + '"'
print 'The last entry'
print '    * is called "' + f.entries[1].title + '"'
print '    * was published on "' + f.entries[1].published + '"'
print '    * at the URL "' + f.entries[1].link + '"'

print
print ('The current time is', 
	   time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.localtime()))
print ('It took me ' + str(round(time.time() - starttime,3)) + 
	   ' seconds to do your bidding.')
print 
