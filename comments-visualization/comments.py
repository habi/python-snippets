#! /usr/bin/env python

import optparse
from pylab import *

# Use Pythons Optionparser to define and read the options, and also
# give some help to the user
parser = optparse.OptionParser()
usage = "usage: %prog [options] arg"
parser.add_option('-n', dest='Name', metavar='Fridolin')
(options, args) = parser.parse_args()

# show the help if no parameters are given
if options.Name==None:
	parser.print_help()
	print ''
	print 'Example:'
	print 'The command reads the comment from "comments_sepp.txt"'
	print 'and plots them nicely.'
	print ''
	print 'comments.py -n sepp'
	print ''
	sys.exit(1)
print ''

Data = genfromtxt('comments_' + str(options.Name) + '.txt',skip_header=True)

MaxAverage = 0
for line in Data[:,2]:
	MaxAverage = max(MaxAverage,line)

ax = plt.subplot(111)
ax.plot(Data[:,0],Data[:,2]/MaxAverage)
ax.axis([2003,2012,0,1])
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
title('Normalized comments for ' + str(options.Name))
savefig(str(options.Name) + '.png')
