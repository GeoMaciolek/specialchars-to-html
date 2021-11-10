# HTML Character / Entity Converter

## Overview

This tool converts special characters to their HTML versions, for example
converting "&#339;" to the string `&#339;`. The output file(s) are saved - by
default - a filename-processed.txt (keeping the original extension).

## Usage

This requires only a standard installation of Python 3. For help, see the
[Python-Guide.com](https://docs.python-guide.org/starting/installation/).

Once Python is installed, download the contents of this repository (either via)
`git clone` or downloading the ZIP from the green "CODE" button dropdown.

Then, go to that directory in your command prompt / terminal; run as follows:

```bash
cd ~/Downloads/specialchars-to-html  # Or whatever the download path is
python3 convert.py ~/path/to/source-file.txt # Sometimes "python", not "python3"
```

### Usage Example

```text
usage: convert.py [-h] [--outpath OUTPATH] [--nosuffix] [--debug]
            [--customsuffix CUSTOMSUFFIX] [--dropextension] [--displayonly]
            [--showfilename] source_file [source_file ...]

"Special character" to HTML processor. 
    This tool converts special characters to their HTML versions, e.g. &#1234;.
    The output file(s) are saved - by default - a filename-processed.txt
    (keeping the original extension).
    

positional arguments:
  source_file           The file(s) to process

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debugging information

File Writing/Saving Options:
  These options let you customize the file saving/naming behavior.

  To save with a custom filetype, combine --dropextension and --customsuffix

  --outpath OUTPATH, -o OUTPATH
                        Write files to the specified output location
  --nosuffix, -S        Don't add "-processed" to filename. Use w/eg. --outpath)
  --customsuffix CUSTOMSUFFIX, -s CUSTOMSUFFIX
                        Set a custom suffix to add to the file when saving.
  --dropextension, -x   Drop the existing file extension

Display / stdout:
  --displayonly, -d     Display the data only; do not write output files
  --showfilename, -n    Display the filename above the output (e.g. if
                        processing multiple files)


Usage Examples:

    convert.py -S example-file.md
        Processes "example-file.md" and saves as "example-file-processed.md" in
        the same directory as the source.

    convert.py -S -o out/ some-file.txt
        Saves processed files to path "out/" w/identical names to input files)
```

## External Links & References

- [HTML Entities](https://www.w3.org/TR/html4/sgml/entities.html)
