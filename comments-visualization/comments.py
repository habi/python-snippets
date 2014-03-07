'''
Plotting comment number from a WordPress MySQL database
'''

from __future__ import division
import optparse
import random
import string
import sys

try:
    import mysql.connector
except ImportError:
    print 'mysql.connector not found'
    sys.exit('try installing it with "pip install mysql-connector-python"')
try:
    import matplotlib.pyplot as plt
    plot = True
except ImportError:
    print 'matplotlib not found, I cannot plot'
    print 'If you want to see the plot, install it with help from',\
        'http://matplotlib.org/users/installing.html'
    plot = False
try:
    import names
    name = '_'.join(names.get_full_name().split(' '))
except ImportError:
    name = 'John_Doe'

# Use Pythons Optionparser to define and read the options, and also
# give some help to the user
parser = optparse.OptionParser()
usage = "usage: %prog [options] arg"
parser.add_option('-s', '--Server', dest='Server', metavar='example.com',
                  help='Server to access the database from.')
parser.add_option('-d', '--Database', dest='Database', metavar='databank',
                  help='Database from which you would like to grab the data')
parser.add_option('-u', '--User', dest='User', metavar='Fridolin',
                  help='Username for the database above')
parser.add_option('-p', '--Password', dest='Password', metavar='UhuereGheim',
                  help='Password for the user of the database')
parser.add_option('-n', '--Normalized', dest='Normalized',
                  default=True, action='store_true',
                  help='Plot the normalized comments, e.g. relative to the '
                       'maximal amount of comments per post. (default: '
                       '%default)')
parser.add_option("-r", '--Real', dest='Normalized',
                  action="store_false",
                  help='Plot the comments per post. (default is "-n")')
(options, args) = parser.parse_args()

# show the help necessary parameters are missing
if not (options.Server and options.Database and options.User and
        options.Password):
    print 'At least one of the necessary parameters (Server, Database, User',\
        'or Password) is missing!'
    parser.print_help()
    password = ''.join(random.choice(string.lowercase) for i in range(8))
    print
    print 'Example:'
    print 'The command gets the comments'
    print '   * out of the database "awesomebase" on server "example.com"'
    print '   * for user "' + name + '"'
    print '   * with the password "' + password + '"'
    print 'and plots them with the real numbers (if matplotlib is available',\
        'otherwise it just gives out the numbers.'
    print
    print 'comments.py -s example.com -d awesomebase -u', name, '-p',\
        password, '-r'
    print
    sys.exit('Plese try again')

databaseconnection = mysql.connector.connect(host=options.Server,
                                             database=options.Database,
                                             user=options.User,
                                             password=options.Password)
cursor = databaseconnection.cursor()

query = ' '.join(["SELECT YEAR(post_date) , COUNT(ID) , AVG(comment_count)",
                  "FROM `wp_posts`",
                  "WHERE post_status = 'publish'",
                  "GROUP BY YEAR( post_date )"])

cursor.execute(query)
Years = [int(post_date) for (post_date, ID, comment_count) in cursor]

cursor.execute(query)
Posts = [int(ID) for (post_date, ID, comment_count) in cursor]
NormalizedPosts = [x / max(Posts) for x in Posts]

cursor.execute(query)
CommentsPerPost = [float(comment_count) for
                   (post_date, ID, comment_count) in cursor]
NormalizedComments = [x / max(CommentsPerPost) for x in CommentsPerPost]

cursor.close()
databaseconnection.close()

print
print 'Year | Posts | Cmnts | Cmnts, normalized'
print 40 * '-'
for y in Years:
    print y, '|', str(Posts[Years.index(y)]).rjust(5), '|',\
        str(round(CommentsPerPost[Years.index(y)], 2)).ljust(5), '|',\
        str(round(NormalizedComments[Years.index(y)], 3)).ljust(8)

# Colors by http://tools.medialab.sciences-po.fr/iwanthue/, Fancy (light
# background), 2 colors, soft (k-means)
if plot:
    plt.rc('lines', linewidth=3, marker='s')
    plt.figure(figsize=(16, 5))
    plt.subplot(131)
    plt.plot(Years, Posts, color='#B8C7D5')
    plt.xlabel('Year')
    plt.xlim([min(Years), max(Years) - 1])
    plt.title('Posts per year')
    plt.subplot(132)
    if options.Normalized:
        plt.plot(Years, NormalizedComments, color='#BCD684')
        plt.title('Normalized comments per post')
    else:
        plt.plot(Years, CommentsPerPost, color='#BCD684')
        plt.title('Comments per post')
    plt.xlabel('Year')
    plt.xlim([min(Years), max(Years) - 1])
    plt.subplot(133)
    plt.plot(Years, NormalizedPosts, label='posts', color='#B8C7D5')
    plt.plot(Years, NormalizedComments, label='comments', color='#BCD684')
    plt.legend(loc='best')
    plt.title('Normalized posts\nand comments')
    plt.xlim([min(Years), max(Years) - 1])
    plt.savefig(str(options.User) + '.png')
    plt.show()
