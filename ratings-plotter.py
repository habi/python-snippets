"""
Plot the ratings of all Simpsons episodes ever aired
"""

from __future__ import division
from bs4 import BeautifulSoup
import urllib2
import matplotlib.pyplot as plt

Season = []
Episode = []
AirDate = []
Name = []
Rating = []

UpToSeason = 26

for S in range(1, UpToSeason):
    url = 'http://www.tvrage.com/The_Simpsons/episode_list/' + str(S)
    print 'Getting data for Season', S
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())

    # find all 'td' tags and put them in a list
    tag = soup.findAll('td')

    for item in tag:
        if str(S) + 'x' in item.text:
            Season.append(int(item.text.split('x')[0]))
            Episode.append(int(item.text.split('x')[1]))
            AirDate.append(tag[tag.index(item) + 1].text)
            Name.append(tag[tag.index(item) + 2].text.strip())
            Rating.append(float(tag[tag.index(item) + 3].text))

verbose = True
if verbose:
    for i in range(len(Episode)):
        print 'S', Season[i], 'Ep.', Episode[i], 'aired on', AirDate[i], \
            'was called', Name[i], 'and was rated', Rating[i]

plt.plot(Season, Rating, 'o')
plt.xlim([0, UpToSeason])
plt.ylim([0, 10])
plt.title('The Simpsons')
plt.xlabel('Season')
plt.ylabel('Rating')
plt.savefig('Simpsons.png')
plt.show()
