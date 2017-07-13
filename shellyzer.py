#!/usr/bin/env python

import sys, os, re, time

class Logger(object):
	def __init__(self):
		self.terminal = sys.stdout
		self.log = open("shellyzer.log", "a")

	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def flush(self):
		pass
		
sys.stdout = Logger()

def checkStrings(filepath):
	globalcount = 0
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
	totalissues = 0
	print "~"*50
	print "~              S H E L L Y Z E R v 1.0           ~"
	print "~"*50
	rootdir = str(raw_input("Enter the full path to the source code you want to scan \n"))
	for dirs,subdirs,files in os.walk(rootdir):
		for file in files:
			filepath = dirs + os.sep + file
			if filepath.lower().endswith(('.sh')):
				totalissues += checkStrings(filepath)
	print "Total issues found: %d"%totalissues
	if totalissues > 0:
		print "Response Code: 1"
	else:
		print "Response Code: 0"

if __name__ == "__main__":
	main()