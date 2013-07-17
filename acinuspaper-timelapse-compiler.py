'''
Script to 'latexmk' every revision of the acinus-paper and to compile the PDFs
into a mosaic, so we can make a timelapse movie of the paper.
'''

import os
import subprocess
import glob

latexmk = True
montage = False

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
# If we have more than 99 revisions 'skip=2' will need to be changed to
# 'skip=3'. And probably also change the string formatting for the Directories
skip = 2
MaxRevision = int(Output[Output.find('Revision') + len('Revision: '):
                         Output.find('Revision') + len('Revision: ') + skip])

PageNumber = []
# Go into each folder and 'latexmk' this thing
if latexmk:
    for Revision in range(1, MaxRevision + 1):  # from 1 to MaxRev, not between
        Directory = os.path.join(SaveToDirectory,
                                'PaperRevision' + "%02d" % Revision)
        print 'Latexmk-ing revision', Revision
        os.chdir(Directory)
        nirvana = open("NUL", "w")
        # compile even with errors (for some revisions we're miss some images)
        subprocess.call('latexmk -pdf -silent *.tex', stdout=nirvana,
                        stderr=nirvana, shell=True)
        # cleanup after compilation
        subprocess.call('latexmk -c *.tex', stdout=nirvana, stderr=nirvana,
                        shell=True)
        nirvana.close()
        # Count Pages of the resulting PDF
        process = subprocess.Popen('identify -format %n *.pdf',
                                   stdout=subprocess.PIPE)
        NumberOfPages, Error = process.communicate()
        PageNumber.append(NumberOfPages)
        print 'The PDF of revision', Revision, 'contains', NumberOfPages[:-2],\
         'pages'
    print 'The maximum page number found is', max(PageNumber)

# Go into each folder and make a montage of the PDF
# Commandline call based on one of wiki pages http://is.gd/rpQHVk and help from
# http://is.gd/ArtPrA
# > montage -density 300 album.pdf -mode Concatenate -tile 2x1 -quality 80
# >-resize 800 two_page.jpg
if montage:
    for Revision in range(1, MaxRevision + 1):  # from 1 to MaxRev, not between
        Directory = os.path.join(SaveToDirectory,
                                'PaperRevision' + "%02d" % Revision)
        print 'Compiling all pages of Revision', Revision, 'into a mosaic'
        os.chdir(Directory)
        # concatenate all pages into one humongous image
        subprocess.call('montage -density 300 *.pdf -mode Concatenate -tile' +\
                        ' 7x6 mosaic-' + str("%02d" % Revision) + '.png',
                        shell=True)
        print 'Resizing mosaic to 4k resolution'
        # resize that humongous image to 4K resolution
        os.chdir(Directory)
        print os.getcwd()
        subprocess.call('convert mosaic-' + str("%02d" % Revision) + '.png ' +\
                        '-resize 4096 -background white -gravity north ' +\
                        '-extent 4096x4096 -gravity south -stroke \"#000C\"' +\
                        ' -strokewidth 15 -pointsize 144 -annotate 0 ' +\
                        '\"Revision ' + str("%02d" % Revision) + '\" ' +\
                        '-stroke none -fill white -annotate 0 \"Revision ' +\
                        str("%02d" % Revision) + '\" frame-' + \
                        str("%02d" % Revision) + '.png', shell=True)
