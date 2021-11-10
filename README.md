# HTML Character / Entity Converter

## Overview

This tool converts special characters to their HTML versions, for example converting &#339; to the string `&#339;`. The output file(s) are saved - by default - a filename-processed.txt (keeping the original extension).

## Help

```
usage: convert.py [-h] [--customsuffix CUSTOMSUFFIX] [--dropextension] [--displayonly] [--showfilename] [--debug]
                  source_file [source_file ...]

Special character to HTML processor. This tool converts special characters to their HTML versions, e.g. &#1234;. The output file(s) will be
saved as filename-processed.txt.

positional arguments:
  source_file           The file(s) to process

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debugging information

File Writing/Saving Options:
  These options let you customize the file saving/naming behavior. If you wish to save with a custom filetype, combine --dropextension
  with --customsuffix

  --customsuffix CUSTOMSUFFIX, -s CUSTOMSUFFIX
                        Set a custom suffix to add to the file when saving
  --dropextension, -x   Set a custom suffix to add to the file when saving

Display / stdout:
  --displayonly, -d     Display the data only; do not write output files
  --showfilename, -n    Display the filename above the output (e.g. if processing multiple files)g. if processing multiple files)
  ```

## External Links & References

- [HTML Entities](https://www.w3.org/TR/html4/sgml/entities.html)