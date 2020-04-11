#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Data Show'
SITENAME = 'Data Show Notebooks'
SITEURL = ''

PATH = 'notebooks'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

USE_FOLDER_AS_CATEGORY=False
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/DataShow_'),
          ('instagram', 'https://www.instagram.com/datashow_'),
          ('github', 'https://github.com/data-show'),)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.
IGNORE_FILES = ['.ipynb_checkpoints', 'Logo_and_Cover']

# Ipynb
IPYNB_GENERATE_SUMMARY=False
