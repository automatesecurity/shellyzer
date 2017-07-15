#!/usr/bin/env python

import os

def checkStrings(filepath):
	globalcount = 0
	lintList = ['eval(', 'exec(','sudo']
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
					print "%s found on line: %d --> %s"%(item.split('(')[0], num, line),
				else:
					pass
                globalcount = globalcount + issuecount
		if issuecount == 0:
			print "0 issues found"
		if issuecount > 0:
			print ""
			print "%d issue(s) found"%issuecount
		issuecount = 0
		print ""
		return int(globalcount)

def main():
	totalissues = 0
	print "~"*100
	print "~              Shell Script Linter v 1.0           ~"
	print "~"*100
	rootdir = str(raw_input("Enter the full path of the directory that contains the script \n"))
	for dirs,subdirs,files in os.walk(rootdir):
		for file in files:
			filepath = dirs + os.sep + file
			if filepath.lower().endswith(('.sh')):
				totalissues += checkStrings(filepath)
	print "Total issues found: %d"%totalissues

if __name__ == "__main__":
	main()
