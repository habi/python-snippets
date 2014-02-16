from bs4 import BeautifulSoup
import urllib2
import matplotlib.pyplot as plt

Season = 21

url = 'http://www.tvrage.com/The_Simpsons/episode_list/' + str(Season)

page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

#find all 'td' tags and put them in a list
tag = soup.findAll('td') 

Episode = []
AirDate = []
Name = []
Rating = []
for item in tag:
    if str(Season) + 'x' in item.text:
        print 'Episode', item.text, 'called', tag[tag.index(item) +2].text.strip(), \
            'aired on', tag[tag.index(item) +1].text, 'and was rated',\
            tag[tag.index(item) +3].text
        Episode.append(item.text)
        AirDate.append(tag[tag.index(item) +1].text)
        Name.append(tag[tag.index(item) +2].text)
        Rating.append(float(tag[tag.index(item) +3].text))

plt.plot(Rating)
plt.title('Season ' + str(Season))
plt.ylim([0,10])
plt.savefig('Season' + str(Season) + '.png')
plt.show()