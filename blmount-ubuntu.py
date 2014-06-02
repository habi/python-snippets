#!/usr/bin/python

'''
Script to "replace" blmount for mounting eAccount directories on Ubuntu.
The [replacement] from Matteo works with 'sudo', thus the files are only
readable with being root.
'''

# First version: 2.6.2014

from optparse import OptionParser
import sys
import os
import subprocess

#~ sudo mount -t cifs //X02DA/e14718 ~/mnt -o username=e14718,password=chmielewski
#~ sudo umount ~/mnt

# clear the commandline
os.system('clear')

# Use Pythons Optionparser to define and read the options, and also
# give some help to the user
Parser = OptionParser()
Parser.add_option('-b', '--Beamline', dest='Beamline', default='x02da',
                  type='str',  help='Beamline you want to mount. Defaults to '
                       '%default', metavar='x02da')
Parser.add_option('-e', '--eAccount', dest='eAccount', type='str',
                  help='eAccount you want to mount.', metavar='e13960')
Parser.add_option('-p', '--Password', dest='Password', type='str',
                  help='Password of the eAccount you want to mount.')
Parser.add_option('-d', '--Directory', dest='MountPoint', default='mnt',
                  help='Directory to mount to. Defaults to /%default',
                  metavar='~/somedir')
Parser.add_option('-u', '--Unmount', dest='Unmount', default=False,
                  action='store_true', help='Unmount the directory. Defaults '
                  'to ~/%default')
Parser.add_option('-v', '--Verbose', dest='Verbose',
                  default=False, action='store_true',
                  help='Be really chatty. Default: %default')
(options, Arguments) = Parser.parse_args()

# Show the help if no parameters are given, otherwise convert path to sample to
# absolute path
if options.eAccount is None:
    Parser.print_help()
    print 'Example:'
    print 'The command below mounts the eAccount of David to the "mnt"', \
        'directory in your home folder.'
    print
    print sys.argv[0], ('-e e13960 -p haberthuer')
    print
    sys.exit('Please retry!')

# See if the desired sample folder actually exist
if not os.path.exists(os.path.join('/',options.MountPoint, options.eAccount)):
    if options.Verbose:
        print 'Making directory', os.path.join(os.path.expanduser('~'),
                                                options.MountPoint)
    os.mkdir(os.path.join('/',options.MountPoint, options.eAccount))

mountcommand = ['sudo','mount','-t','cifs']
mountcommand += ['//' + options.Beamline + '/' + options.eAccount]
mountcommand += [os.path.join('/',options.MountPoint, options.eAccount)]
mountcommand += ['-o','username=' + options.eAccount + ',password=' + options.Password]

#~ sudo mount -t cifs //X02DA/e14718 ~/mnt -o username=e14718,password=chmielewski
#~ sudo umount ~/mnt

print mountcommand

subprocess.check_call(mountcommand)

print 'Folder of eAccount', options.eAccount, 'mounted to', \
    os.path.join(options.MountPoint,options.eAccount)
