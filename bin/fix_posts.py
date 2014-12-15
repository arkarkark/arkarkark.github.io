#!/usr/bin/python
# Copyright 2014 Alex K (wtwf.com)
"""
Fixes up some posts imported from blogger with permalinks

posts imported with: https://gist.github.com/ngauthier/1506614

make all.txt with this (it finds all the blogger posts' urls):

for yr in $(seq 2005 2014); do \
  for mo in $(seq -w 1 12); do \
   sleep 1; wget -q -O - \
     "http://blog.wtwf.com/?action=getTitles&widgetId=BlogArchive1&widgetType=BlogArchive&responseType=js&path=http%3A%2F%2Fblog.wtwf.com%2F${yr}_${mo}_01_archive.html" \
     | egrep -o "http://blog.wtwf.com[^']*"; done; done | tee all.txt

make rpc.json from the blogger_rpc call that looks like this:
https://draft.blogger.com/blogger_rpc?blogID=10...44

"""

__author__ = 'wtwf.com (Alex K)'

import getopt
import logging
import os
import sys
import urlparse
import yaml
import json

YAML_SEP = '---\n'
FILE_PREFIX_LENGTH = 5
POSTS_DIR = '_posts'

def Usage(code, msg=''):
  """Show a usage message."""
  if code:
    fd = sys.stderr
  else:
    fd = sys.stdout
  PROGRAM = os.path.basename(sys.argv[0]) # pylint: disable=invalid-name,unused-variable
  print >> fd, __doc__ % locals()
  if msg:
    print >> fd, msg
  sys.exit(code)

def Main():
  """Run."""
  logging.basicConfig()
  logging.getLogger().setLevel(logging.DEBUG)
  try:
    opts, args = getopt.getopt(sys.argv[1:], 'h', 'help,permalinks,labels'.split(','))
  except getopt.error, msg:
    Usage(1, msg)

  if args:
    Usage(1)

  for opt, arg in opts:
    if opt in ('-h', '--help'):
      Usage(0)
    if opt == '--permalinks':
      FixPermalinks()
    if opt == '--labels':
      FixLabels()

def FixPermalinks():
  """fix it to add permalinks."""
  urls = LoadExistingUrls()
  for file_name  in os.listdir(POSTS_DIR):
    key = KeyFromFileName(file_name)
    if key:
      perm = urls.get(key)
      if perm:
        SetJekyllVariable(file_name, 'permalink', perm)
      else:
        logging.error('unable to find permalink for %r', file_name)

def LoadExistingUrls():
  """Load the list of existing urls."""
  urls = {}
  for url in open('all.txt'):
    url = urlparse.urlparse(url.strip())
    key = KeyFromPath(url.path)
    if key:
      urls[key] = url.path
  return urls

def SetJekyllVariable(file_name, key, value):
  """Update a variable in the jenkins section of a post file."""
  file_name = os.path.join(POSTS_DIR, file_name)
  contents = open(file_name).read()
  sections = contents.split(YAML_SEP)
  if len(sections) < 2:
    logging.fatal('invalid file format: %r', file_name)
  jenky = yaml.load(sections[1])
  jenky[key] = value
  sections[1] = yaml.dump(jenky, default_flow_style=False)
  open(file_name, 'w').write(YAML_SEP.join(sections))


def FixLabels():
  logging.info('Fixing Labels')
  blogger = json.load(open('rpc.json'))
  posts = blogger['result']['2']
  file_map = GetFileMap()
  for post in posts:
    title = post['2']
    url = post['9']
    date = post['6']
    labels = post.get('8')
    state = post['7']
    file_name = FindPostFileFromUrl(file_map, url, date)
    missing = []
    if file_name and labels:
      logging.info('%s: %s', title, file_name)
      SetJekyllVariable(file_name, 'tags', map(str, labels))
    else:
      missing.append('Unable to find file for: %s %s' % (state, title))
    if missing:
      logging.warn('\n'.join(missing))

def GetFileMap():
  file_map = {}
  for file_name  in os.listdir(POSTS_DIR):
    key = KeyFromFileName(file_name)
    if key:
      file_map[key] = file_name
    key = KeyFromFileNameDate(file_name)
    if key:
      file_map[key] = file_name
  return file_map

def KeyFromFileName(file_name):
  parts = file_name.split('-', 3)
  if len(parts) < 3:
    return None
  del parts[2]
  parts[-1] = parts[-1][0:FILE_PREFIX_LENGTH]
  return '-'.join(parts)

def KeyFromFileNameDate(file_name):
  parts = file_name.split('-', 3)
  if len(parts) < 3:
    return None
  del parts[3]
  return '-'.join(parts)

def KeyFromPath(path):
  paths = path.lstrip('/').split('/', 2)
  if len(paths) > 2:
    paths[-1] = paths[-1][0:FILE_PREFIX_LENGTH]
    return '-'.join(paths)
  return None


def FindPostFileFromUrl(file_map, url, date):
  url = urlparse.urlparse(url)
  key = KeyFromPath(url.path)
  file_name = file_map.get(key)
  if not file_name:
    date_parts = map(int, date.split('/'))
    if len(date_parts) == 3:
      key = '20%02d-%02d-%02d' % (date_parts[2], date_parts[0], date_parts[1])
      file_name = file_map.get(key)
  return file_name

if __name__ == '__main__':
  Main()
