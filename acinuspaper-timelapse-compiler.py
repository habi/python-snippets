'''
Script to 'latexmk' every revision of the acinus-paper.
'''

import os
import subprocess
import glob

# Setup
SaveToDirectory = os.path.join('c:\\', 'Users', 'haberthu', 'Desktop',
    'Dropbox', 'Work', 'AcinusPaperTimeLapse')
    
    
# Get SVN info from remote repository
(Output, Error) = subprocess.Popen(('svn', \
                                    'info',\
                                    'http://code.ana.unibe.ch/svn/' + \
                                    'AcinusPaper'),
                                    stdout=subprocess.PIPE,
                                    shell=True).communicate()

# Do some string manipulation to find the highest revision number
# The 'Output' above contains 'Revision: $RevisionNumber', thus find the first
# occurrence of 'Revision' in Output, and use the two digits that come after it
# If we have more than 99 revisions 2 will need to be changed to 3. :)
MaxRevision = int(Output[Output.find('Revision') + len('Revision: '):
                         Output.find('Revision') + len('Revision: ') + 2])

silent = True
# Go into each folder and 'latexmk' this thing
for Revision in range(1, MaxRevision + 1):  # go from 1 to MaxRev, not between    
    Directory = os.path.join(SaveToDirectory,
                            'PaperRevision' + "%02d" % Revision)
    print 'Latexmk-ing revision', Revision
    os.chdir(Directory)
    nirvana = open("NUL", "w")
    # compile even with errors (for some revisions we're missing the images) 
    subprocess.call('latexmk -pdf -silent *.tex', stdout=nirvana, stderr=nirvana,
        shell=True)
    # cleanup after compilation
    subprocess.call('latexmk -c *.tex', stdout=nirvana, stderr=nirvana,
        shell=True)        
    nirvana.close()
