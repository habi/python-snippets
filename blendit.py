# -*- coding: utf-8 -*-

"""
I could probably do it with a shellscript, but I'm more comfortable to do it in
Python: This script constructs the commandline call for ImageMagick to blend
12 stereographic [panoramas] of the inside of the  [Swiss Light Source][sls] and
turns them around 360° while doing so.

[panoramas]: http://flic.kr/s/aHsjynREyz
[sls]: http://www.psi.ch/sls/
"""

testing = False

import os

BasePath = '/Users/habi/Desktop/SLS 2012/Stereographic'

# Go through every month
for Image in range(1,13):
	if testing:
		pass
	else:
		try:
			os.mkdir(os.path.join(BasePath,"%02d" % Image + '_' + "%02d" % (Image %12 + 1)))
		except OSError:
			pass
	print
	# Go through every blending level from 1 to 100%, don't use 0, since that is
	# 100% from the previous call.
	for blendinglevel in range(1,101):
		# 'Image' goes from 1 to 12 (each month). We use 'Image' and 'Image + 1'
		# in each loop to construct the call for ImageMagick. Since we also want
		# to merge December with January, we can simply use the Image-number 
		# modulo 12 (Image % 12), which gives 1 for 13. Voila!
		ImageName = "%02d" % Image + '_' + "%02d" % (Image % 12 + 1) + '_' +\
			"%03d" % blendinglevel + '.jpg'
		print str(blendinglevel) +  '% of', '%02d' % Image + '_stereographic.tif +',\
			str(100 - blendinglevel) + '% of', '%02d' % (Image % 12 + 1) + '_stereographic.tif',\
			'=', ImageName
		# We want to convert (merge, but wait for it) the images
		blendcommand = 'convert '
		# 1_stereographic and 2_stereographic (and 2 with 3, 3 with 4, etc.)
		blendcommand += "%02d" % Image + '_stereographic0000.tif ' "%02d" % (Image % 12 + 1) + '_stereographic0000.tif '
		# with a white background
		blendcommand += '-virtual-pixel white '
		# while rotating them around 360° for all 12 images. SRT stands for
		# Scale-Rotate-Translate: http://www.imagemagick.org/Usage/distorts/#srt)
		blendcommand += '-distort SRT ' + str(360.0/12*blendinglevel/100+((Image-1)*360/12))
		# blending requires alpha channel
		blendcommand += ' -alpha on '
		# since the rotation leaves a background, we just shave off the edge of
		# the images and crop them to a 4:3 aspect ration to get rid of the
		# background. There probably is an option to 'rotate', but this is the
		# KISS version.
		blendcommand += '-shave 1000x1250'
		# blend the two images together with a varying blending level
		blendcommand += ' -compose blend -define compose:args=' + "%03d" % blendinglevel + ' -composite '
		# to a desired output filename (in a subfolder, constructed through
		# os.path.join)
		blendcommand += os.path.join("%02d" % Image + '_' + "%02d" % (Image % 12 + 1),"%02d" % Image + '_' + "%02d" % (Image % 12 + 1) + '_' + "%03d" % blendinglevel + '.jpg')
		if testing:
			print blendcommand
		else:
			os.chdir(BasePath)
			os.system(blendcommand)
	print 'Done with month',Image,'and',Image % 12 + 1

print 'been there, done that!'