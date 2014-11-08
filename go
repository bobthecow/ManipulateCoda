#!/usr/bin/python

import sys, os
from optparse import OptionParser


parser = OptionParser(usage='usage: %prog [options]')
opts = (
    ('-v', '--verbose', {'action': 'store_true', 'default': False, 'help': 'enable verbose output'}),
    ('-i', '--install', {'action': 'store_true', 'default': False, 'help': 'install plugin(s)'}),
    ('--package', {'action': 'store_true', 'default': False, 'help': 'package plugin for distribution'}),
    ('-o', {'dest': 'outfile', 'default': False, 'metavar': 'FILENAME', 'help': 'output package zip as FILENAME'}),
)
for opt in opts:
    parser.add_option(*opt[:-1], **opt[-1])

(options, rest) = parser.parse_args()

print 'Building Manipulate Coda'

# start by clearing out the dist directory
if options.verbose:
    print 'Removing old build directories.'
os.system('if [ -d dist/ ]; then rm -r dist/; fi')
os.system('if [ -d build/ ]; then rm -r build/; fi')

if options.verbose:
    print 'Building plugin bundle'
    os.system('python setup.py py2app')
else:
    os.system('python setup.py py2app > /dev/null')

# if they asked us to install them...
if options.install:
    if options.verbose:
        print 'Installing Manipulate Coda'
    os.system('open -b com.panic.Coda2 dist/*')

# if we're going to package for release
if options.package:
    if options.outfile:
        filename = options.outfile
        if filename[-4:] == '.zip':
            filename = filename[:-4]
    else:
        filename = 'manipulate-coda'

    os.system('if [ -f %s.zip ]; then rm %s.zip; fi' % (filename, filename))
    if options.verbose:
        print 'Packaging plugins for distribution'
        os.system('cd dist/; zip -r ../%s.zip *; cd ..' % filename)
    else:
        os.system('cd dist/; zip -qr ../%s.zip *; cd ..' % filename)

    # add the readme
    if options.verbose:
        print 'Adding README.md to zipfile'
        os.system('zip %s.zip README.md' % filename)
    else:
        os.system('zip -q %s.zip README.md' % filename)
