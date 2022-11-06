from app import App

import os
import sys

if len(sys.argv) > 2:
    print('Pass only one file at a time')
    sys.exit()

if len(sys.argv) < 2:
    print('Please specify the filename to be redacted')
    sys.exit()

input_file = sys.argv[1]

if not os.path.isfile(input_file):
    print('The file specified does not exist')
    sys.exit()

try:
    result = App().redactImage(input_file)
    print("Image was redacted and saved in {}".format(result))
except Exception as ex:
    print("Error encountered while redacting file: {}".format(ex))

