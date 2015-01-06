"""
Script to read some yearly reporst from dopplr.com, the brute force way.
Now that dopplr.com is gone, this is most probably obsolete...
"""

import os
import hashlib
import urllib
import urllib2
import sys

# Trying to download some personal reports
currenthash = "7fb16e238d5659a6"
base_url = "http://reports.dopplr.com/2009/"
try:
    os.mkdir(os.path.join(os.getcwd(), 'dopplr'))
except OSError:
    'Folder "dopplr" already exist, proceeding...'
HowMany = int(1e6)
print 'Trying to get', HowMany, 'personal reports from', base_url
for i in range(HowMany):
    random_data = os.urandom(128)
    currenthash = hashlib.md5(random_data).hexdigest()[:16]
    print str(i) + '/' + str(HowMany) + ":", currenthash + '.pdf',
    if os.path.isfile(os.path.join(os.getcwd(), 'dopplr',
                      currenthash + "_na.txt")):
        print 'which we already tried before'
    else:
        filename = str(base_url + currenthash + ".pdf")
        try:
            urllib2.urlopen(filename)
            urllib.urlretrieve(filename, os.path.join(os.getcwd(), 'dopplr',
                               currenthash + ".pdf"))
            print 'saved as', os.path.join('dopplr', currenthash + ".pdf")
        except:
            print 'is not there'
            open(os.path.join(os.getcwd(), 'dopplr', currenthash + "_na.txt"),
                 'w').close()
            # Cursor up one line: http://stackoverflow.com/a/5291044
            sys.stdout.write("\033[F")
