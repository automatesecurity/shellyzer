#!/usr/bin/env python

import sys, os, re, time

class Logger(object):
	"""Ensure the logger is setup properly"""
	def __init__(self):
		self.terminal = sys.stdout
		self.log = open("shellyzer.log", "a")

	"""Write stdout to both the terminal and log file"""
	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	"""Ensure compatability with Python 3"""
	def flush(self):
		pass
		
sys.stdout = Logger()

def checkStrings(filepath):
	"""Compare lint signatures against lines of code
	within each line of a file retrieved from the 
	given filepath.

	The following method will loop through each file
	matching the .sh extension and compare it to the
	lintList to determine if a signature exists in a
	source file.  If a signature is found in source 
	then the line number and line of code will be 
        sent to stdout and result in a response code (0).

	For issues found, a counter will increment to track
	for reporting purposes per source file and for the
	overall run of the script across multiple files.

	"""

	globalcount = 0
	# customize the lintList signatures below
	lintList = ['eval', 'exec']
	with open(filepath) as f:
		issuecount = 0
		print "-"*50
		print "In file: %s"%filepath
		print "-"*50
		for num, line, in enumerate(f, 1):
			line = line.split('#')[0]
			for item in lintList:
				if item in line:
					issuecount += 1
					print "\33[91m%s\33[0m found on line: %d - %s"%(item, num, line),
				else:
					pass
		if issuecount == 0:
			print "0 issues found"
		globalcount = globalcount + issuecount
		if issuecount > 0:
			print ""
			print "%d issue(s) found"%issuecount
		issuecount = 0
		print ""
		return int(globalcount)

def main():
	# Set totalissues for issue tracking
	totalissues = 0
	print "~"*50
	print "~              S H E L L Y Z E R v 1.0           ~"
	print "~"*50
	"""Walk the directory tree based on receiving user input"""
	rootdir = str(raw_input("Enter the full path to the source code you want to scan \n"))
	for dirs,subdirs,files in os.walk(rootdir):
		for file in files:
			filepath = dirs + os.sep + file
			# Customize the file extension per your needs
			if filepath.lower().endswith(('.sh')):
				totalissues += checkStrings(filepath)
	# TODO(Daniel): Ensure file permission errors are trapped
	# TODO(Daniel): Output logfile of only errors to error.log
	print "Total issues found: %d"%totalissues
	if totalissues > 0:
		print "Response Code: 1"
	else:
		print "Response Code: 0"

if __name__ == "__main__":
	main()
