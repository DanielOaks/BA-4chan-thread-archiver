BA 4chan API Thread Archiver
===============

`Github <https://github.com/bibanon/BA-4chan-thread-archiver>`_

This script uses the `4chan API <https://github.com/4chan/4chan-API>`_ to:

* Download all images and/or thumbnails in a certain thread.
* Download a JSON dump of thread comments using the 4chan API.
* Download the HTML page
* Convert links in HTML to use the downloaded images
* Download CSS and convert HTML to use them
* Keep downloading until 404 (with a user-set delay)
* Can be restarted at any time

This script is designed to replace "Right-click Save As, Web Page Complete" when saving 4chan threads, since it does not save full-sized images or JSON. 

It can also be used as a far lighter, static HTML alternative to Fuuka.

Part of the JSON-based-chanarchiver by Lawrence Wu, built 2013/04/04.

Usage
============

::

    Usage:
      4chan-thread-archiver <url> [--path=<string>] [--delay=<int>] [--nothumbs] [--thumbsonly]
      4chan-thread-archiver -h | --help
      4chan-thread-archiver -v | --version

    Options:
      --nothumbs          Don't download thumbnails
      --thumbsonly        Download thumbnails, no images
      --delay=<int>       Delay between thread checks [default: 20]
      -h --help           Show help
      -v --version        Show version

By default, the script saves to the folder ``4chan`` in the current working directory.

Installation
============

Windows
-------

1. Install `Python 2.7.` <http://python.org/download/>_ 32-bit version is recommended
2. Install `pip1.6` <https://sites.google.com/site/pydatalog/python/pip-for-windows> using the linked easy installer.
3. Follow the instructions on that site to install the package `BA-4chan-thread-archiver`

::

    pip install BA-4chan-thread-archiver

Linux/Mac
---------

Install Python on your computer. On Linux, Python is almost always preinstalled; however, you will also have to install the program ``pip`` from the repositories to install the necessary packages.

::

    easy_install pip
    pip install BA-4chan-thread-archiver
    
Example
=======

::

    4chan-thread-archiver http://boards.4chan.org/b/res/423861837 --path=4chan-threads --delay 5 --thumbsonly

Modifications to original
============

Originally forked from Socketub's `4chan-thread-archiver. <https://github.com/socketubs/4chan-thread-archiver>`_ 

However, all the original has long since been replaced, and the scripts are totally different. Here is a list of additions:

* Based on `py4chan <https://github.com/e000/py-4chan>`_
* Downloads HTML dump of thread
* New --thumbsonly option to download thumbnails and no images
* Code modularization
* More comments in code
* Support for new 4cdn.org server

More info and a full journal can be found in ``log.md``.

Wishlist
=========

* Prompt user for metadata information.
* Define the ``.chan.zip`` format for 4chan thread archive transfer
* Create a PyQt GUI
