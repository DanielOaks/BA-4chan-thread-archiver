#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

if sys.argv[-1] == 'publish':
	os.system('python setup.py sdist upload')
	sys.exit()

with open('README.rst') as file:
  long_description = file.read()


setup(
		name             = 'BA-4chan-thread-archiver',
		version          = '0.6.9',
		description      = 'Makes a complete archive of a 4chan thread\'s images, HTML, and JSON, using the 4chan API.',
		long_description = long_description, 
		license          = open('LICENSE').read(),
		author           = 'Lawrence Wu',
		author_email     = 'sagnessagiel@gmail.com',
		url              = 'https://github.com/bibanon/4chandownloader',
		keywords         = '4chan downloader images json dump',
		scripts          = ['4chan-thread-archiver', '4chan-thread-archiver-old'],
		install_requires = ['requests', 'docopt==0.5.0', 'py-4chan'],
		classifiers      = (
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7')
)
