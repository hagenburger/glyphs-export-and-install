#MenuTitle: Export and install font
# -*- coding: utf-8 -*-
__doc__="""
Exports and installs all active instances of this font and avoids caching.
"""

import os
import re
import datetime

installFolder = os.path.expanduser("~/Library/Fonts")
suffix = datetime.datetime.now().strftime("%Y%m%d-%H%M")
font = Glyphs.font
for instance in font.instances:
	try:
		if instance.active:
			filePattern = r"^%s(-[\d-]+)?\.(otf|ttf)" % instance.fontName
			oldFonts = [f for f in os.listdir(installFolder) if re.match(filePattern, f)]
			for oldFont in oldFonts:
				os.remove(installFolder + "/" + oldFont)
				print "Uninstalled %s" % oldFont
			fileName = "%s-%s.otf" % (instance.fontName, suffix)
			print "Exporting %s" % fileName
			instance.generate(FontPath = installFolder + "/" + fileName)
	except Exception, e:
		print e
print "Exported and installed %s" % font.familyName
Glyphs.showNotification("Export and install fonts", "Exported and installed %s" % font.familyName)
