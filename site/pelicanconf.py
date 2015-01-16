#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'sjolicoeur'
SITENAME = u'Dev Log of @sjolicoeur'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# THEME = 'lazystrap' 
# THEME = 'nikhil-theme'
# THEME = 'pelican-mockingbird'
THEME = 'pelican-sundown'
# THEME = 'maggner-pelican'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOAD_CONTENT_CACHE = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ["plugins", "pelican_plugins"]

PLUGINS = [
    'extended_sitemap',
    'pelican_fontawesome', # usage :fa:`fa-github`
    'pelicanfly',  # i ♥ :fa-coffee: i :fa-github:
    # 'pelican-readtime',
    'feed_summary', # Summary: -- metadata
    'pelican_gist', #[gist:id=3254906] or [gist:id=3254906,file=brew-update-notifier.sh]
    'share_post', #.share_post',
    'simple_footnotes', # Here's my written text[ref]and here is a footnote[/ref].
    'representative_image', # metadata::: `Image: /images/my-super-image.png`
    'summary', 'clean_summary',

]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



EXTENDED_SITEMAP_PLUGIN = {
    'priorities': {
        'index': 1.0,
        'articles': 0.8,
        'pages': 0.5,
        'others': 0.4
    },
    'changefrequencies': {
        'index': 'daily',
        'articles': 'weekly',
        'pages': 'monthly',
        'others': 'monthly',
    }
}

FEED_USE_SUMMARY = True

GIST_CACHE_ENABLED = True

CLEAN_SUMMARY_MAXIMUM = 1
CLEAN_SUMMARY_MINIMUM_ONE = True



# This settings indicates that you want to create summary at a certain length
SUMMARY_MAX_LENGTH = 50

# This indicates what goes inside the read more link
READ_MORE_LINK = '<span>continue</span>'

# This is the format of the read more link
READ_MORE_LINK_FORMAT = '<a class="read-more" href="/{url}">{text}</a>'


# pelican-themes -vi ~/Dev/Python/pelican-themes/two-column
