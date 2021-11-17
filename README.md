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

#### Converting Line Endings

This may be needed in soem circumstances - determine if this is the case with
the `file` command - you should have CRLF and UTF-8, not CR and ASCII

```bash
# Install "dos2unix" - like "brew install dos2unix" ?

# mac2unix will convert the "CR" (carriage-return) at the end of each file
# to "LF" (linefeed) - the unix standard.  This is useful even just to do
# examinations of the files, as shown around "Tracking Down Gremlins"

mac2unix < source-file.tsv > file-with-lf.tsv
unix2dos < file-with-lf.tsv > file-with-crlf.tsv

# from inside the convert util path!
mkdir out/
python3 convert.py -S file-with-lf.tsv -o out/

unix2dos < out/file-with-lf.tsv > file-with-new-chars-and-crlf.tsv
```

#### Tracking Down Gremlins

Amont other things, VSCode with the "gremins" extension can help.

To find all "upper ascii" (as in, not normal text) characters in a file. This
can be run in bash (in the "Terminal" on a Mac, for example).

Note: You may want to ensure the files have LF endings; see mac2unix above.
Otherwise, grep will not know where line endings are, and you'll get useless
results.

```bash
# Shows all lines (prefixed with line numbers) with upper ascii
grep -anP '[\x80-\xFF]' some-source-file.tsv

# Shows only the first chunks of data, to make it easier to read
# (splits on tabs) - add ",5" to the end to get the whole description
grep -anP '[\x80-\xFF]' some-source-file.tsv | cut -d$'\t' -f 1-3

# Find othr stuff that may not appear above: check if your locale is UTF-8
locale

# grep - 
grep -avx '.*' a-file-with-greminls.tsv-lf
```

## External Links & References

- [HTML Entities](https://www.w3.org/TR/html4/sgml/entities.html)
