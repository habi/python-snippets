'''
Script to 'latexmk' every revision of the acinus-paper.
'''

import os
import subprocess
import glob

# Setup
SaveToDirectory = os.path.join('c:\\', 'Users', 'haberthu', 'Desktop',
    'Dropbox', 'Work', 'AcinusPaperTimeLapse')

# Go into each folder and 'latexmk' this thing
for Revision in range(1, 50):
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
