#!/usr/bin/env python2
import gandalf
import sys

if len(sys.argv) == 4:
	g = gandalf.Gandalf( int(sys.argv[3],16) , True )
	g.sendControlCommand(0x0000) # prepare for config data in EP2
	g.sendConfigurationFile(sys.argv[1])
else:
	print("usage: " + sys.argv[0] + " <configfile.bin> <cardselect> <hexID>")
