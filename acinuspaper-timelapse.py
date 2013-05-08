'''
Script to check out each and every revision of the Acinus-Paper repository, so
I can then generate some kind of "timelapse" of the evolution of the paper.
'''

import os
import subprocess
import shutil

# Setup
SaveToDirectory = os.path.join('c:', 'Users', 'haberthu', 'Desktop',
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

# Check out each revision into its own directory, remove unnecessary files
for Revision in range(1, MaxRevision + 1):  # go from 1 to MaxRev, not between
    SavePath = os.path.join(SaveToDirectory,
                            'PaperRevision' + "%02d" % Revision)
    print 'Checking out revision', Revision, 'of the acinus manuscript to',\
        SavePath
    # See if we can make a directory. If not, it might already exist. If not,
    # then quit the whole shenanigans.
    try:
        os.mkdir(SavePath)
    except:
        if not os.path.isdir(SavePath):
            print 'I do not know what is wrong'
            exit()
    # Redirect subprocess output to Nirvana: http://stackoverflow.com/a/1244757
    nirvana = open("NUL", "w")
    subprocess.call('svn checkout -r ' + str(Revision) +
        ' http://code.ana.unibe.ch/svn/AcinusPaper ' + SavePath,
        stdout=nirvana, stderr=nirvana, shell=True)
    #~ subprocess.Popen('latexmk ' + str(os.path.join(SavePath, 'acinus.tex')),
        #~ stdout=nowhere, stderr = nowhere)
    # Nirvana was probably a bad choice of variable name, since the Nirvana
    # cannot be closed
    nirvana.close()
    os.rename(os.path.join(SavePath, 'acinus.tex'),
              os.path.join(SavePath, 'acinus_rev' + "%02d" % Revision +
                           '.tex'))
    # remove SVN directory, we don't need that
    shutil.rmtree(os.path.join(SavePath, '.svn'))
    # remove movies for larger revisions, we don't need them
    if Revision > 57:
        shutil.rmtree(os.path.join(SavePath, 'movies'))
