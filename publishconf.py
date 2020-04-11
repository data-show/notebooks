#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://notebooks.data-show.com'
RELATIVE_URLS = False

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
GITHUB_URL='https://github.com/data-show/notebooks'
TWITTER_USERNAME='DataShow_'
GOOGLE_ANALYTICS = 'UA-162035849-2'
