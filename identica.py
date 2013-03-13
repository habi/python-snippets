"""
Loads notices from identi.ca via the API, saves the dates of the notices and plots them
"""

import urllib2
# The XML-wrangling code is based on http://is.gd/IQUOew
from xml.dom.minidom import parseString 
import datetime
from pylab import *

howmany = 200

def NoticeGetter(Notice):
	# Load defined Notice from identica API, extract its date and plot it
	file = urllib2.urlopen('http://identi.ca/api/statuses/show/'+str(Notice)+'.xml')
	data = file.read()
	file.close()
	dom = parseString(data)
	Tag = dom.getElementsByTagName('created_at')[0].toxml()
	Date=str(Tag.replace('<created_at>','').replace('</created_at>',''))
	Date = str(Date[:-11])+str(Date[-5:]) # strip the UTC shift, since I just couldn't get the %z parameter to work...
	Date = datetime.datetime.strptime(Date,'%a %b %d %H:%M:%S %Y')
	print '[' + str(counter) + '/' + str(howmany) + '] ID',Notice,'was posted on',Date
	plt.plot_date(Date,Notice)

# Load freshest notice ID
try:
	file = urllib2.urlopen('http://identi.ca/api/statuses/public_timeline.xml')
	data = file.read()
	file.close()
	dom = parseString(data)
	Tag = dom.getElementsByTagName('id')[0].toxml()
	ID=int(Tag.replace('<id>','').replace('</id>',''))
except:
	print 'Bonkers, I cannot load the public timeline. Giving up!'
	exit()

# Load 'howmany' notices up to the freshest one and plot their date
print 'I will load',howmany,'notices from the first notice up to'
print 'notice ID',ID,'which was posted just now'
print '---'
plt.figure()
for Notice in range(1,ID,int(round(ID/howmany))+1):
	counter = Notice / (ID/howmany) +1
	try:
		NoticeGetter(Notice)
	except:
		# Try the next notice if this one doesnt exist
		try:
			Notice += 1
			NoticeGetter(Notice)
		except:
			# Try once more, then give up
			try:
				Notice += 1
				NoticeGetter(Notice)
			except:
				print '[' + str(counter) + '/' + str(howmany) + '] ID',ID,'does not exist, sorry!'

plt.title('Identica Notice ID vs. Date posted')
plt.xlabel('Date')
plt.ylabel('Notice ID')
plt.show()
