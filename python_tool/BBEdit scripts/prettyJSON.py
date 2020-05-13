#!/usr/bin/python

# Usage:
#   1. Place this script to /Library/Application Support/BBEdit/Text Filters
#   2. Restart BBEdit, and Text -> Apply Text Filter -> prettyJSON
#
# References: http://www.kyleclegg.com/blog/tidy-json-formatting-with-textwrangler

import fileinput
import json

if __name__ == '__main__':
    jsonStr = ''
    for aline in fileinput.input():
        jsonStr = jsonStr + ' ' + aline.strip()
    jsonObj = json.loads(jsonStr)
    print(json.dumps(jsonObj, ensure_ascii=False, sort_keys=True, indent=2).encode('utf8'))
