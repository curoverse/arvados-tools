#!/usr/bin/env python

import arvados
import sys
import argparse

def main():

  if len(sys.argv) <= 1:
    print "Usage: python search_for_files.py -f beginning_of_file_name -l number"
    sys.exit(0)

  parser = argparse.ArgumentParser()
  parser.add_argument(
        '-f', '--file', dest='file', required=False, help="File name or beginning of file name")
  parser.add_argument(
        '-l', '--limit', dest='limit', required=False, help="Limit of api calls you want")
  options = parser.parse_args()

  file = options.file
  limit = options.limit

  call = arvados.api().collections().list(filters=[["any","@@",file+"%:*"]], limit=limit).execute()
  print call['items_available']
  for i in xrange(0,int(limit)):#call['items_available']):
    print call['items'][i]['name'], call['items'][i]['uuid'], call['items'][i]['portable_data_hash']

if __name__ == '__main__':
    main()

