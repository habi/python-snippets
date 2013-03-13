# -*- coding: utf-8 -*-

"""
Skript, um einzelne Bilder in andere zu überblenden
"""

testing = True

import os

BasePath = '/Users/habi/Desktop/SLS 2012/Stereographic'
Blending = range(1,101)
Images = range(1,12)

for Image in Images:
	try:
		os.mkdir(os.path.join(BasePath,"%02d" % Image + '_' + "%02d" % (Image + 1)))
	except OSError:
		pass
	for level in Blending:
		ImageName = "%02d" % Image + '_' + "%02d" % (Image + 1) + '_' +\
			"%03d" % level + '.jpg'
		print str(level) +  '% of', '%02d' % Image + '_stereographic.tif +',\
			str(100 - level) + '% of', '%02d' % (Image + 1) + '_stereographic.tif',\
			'=', ImageName 
		blendcommand = 'convert ' +  "%02d" % Image + '_stereographic.tif ' "%02d" % (Image + 1) + '_stereographic.tif -rotate ' + str(level) + ' -alpha on -compose blend -define compose:args=' + "%03d" % level + ' -composite ' +  os.path.join("%02d" % Image + '_' + "%02d" % (Image + 1),"%02d" % Image + '_' + "%02d" % (Image + 1) + '_' + "%03d" % level + '.jpg')
		if testing is True:
			print blendcommand
		else:
			os.chdir(BasePath)
			os.system(blendcommand)