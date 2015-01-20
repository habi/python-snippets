# Script to visualize how many comments you've gotten to your WordPress blog over the years

- Install the [MySQL Connector/Python](http://dev.mysql.com/doc/connector-python/en/index.html) package.

>  pip install mysql-connector-python

- If you want to get a (potentially funny) random name in the help, also install the [names](https://pypi.python.org/pypi/names/) package.

> pip install names

- run the script to see the help

>comments.py 

- get hold of your database host, username, database and password
- run the script with the appropiate options
- you should get an image like the one shown below, which are the numbers for [my blog](http://habi.gna.ch) (if you have [matplotlib](http://matplotlib.org) installed, otherwise you only get the raw numbers).

![comments for habi.gna.ch](https://raw.githubusercontent.com/habi/python/master/comments-visualization/habi_gna_ch.png)
