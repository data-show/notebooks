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

STATIC_PATHS = [
    'static',
    'images',
    'extra'
    # 'extra/CNAME',
    # 'extra/robots.txt',
    # 'extra/android-chrome-192x192.png',
    # 'extra/android-chrome-512x512.png',
    # 'extra/apple-touch-icon.png',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extra/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/site.webmanifest': {'path': 'site.webmanifest'},
}

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/DataShow_'),
          ('instagram', 'https://www.instagram.com/datashow_'),
          ('youtube', 'https://www.youtube.com/channel/UC1siUJqeSI3Zoyj02tw1jgA'),
          ('github', 'https://github.com/data-show'),
          ('linkedin', 'https://www.linkedin.com/company/data-show-blog'))

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = ['related_posts', 'neighbors', 'post_stats', 'sitemap', 'ipynb.markup']
THEME = './'

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.
IGNORE_FILES = ['.ipynb_checkpoints', 'Logo_and_Cover']

# Ipynb
IPYNB_GENERATE_SUMMARY=False

# Github Corner
GITHUB_CORNER_URL = 'https://github.com/data-show/notebooks'

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    },
    'exclude': ['tag/', 'category/']
}
