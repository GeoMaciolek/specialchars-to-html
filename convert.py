import csv
import json
import os.path
import sys
# import pathlib
from pprint import pprint
import argparse

# source_file = 'test-input.txt'


def replace_strings_mapdict(input_string: str, map_dict: dict) -> str:

    modified_str = input_string

    for key, mapdict in map_dict.items():
        # Could also use "mapdict.original" instead
        # print(f"{modified_str=} = modified_str.replace(key,mapdict['replacement'])")
        if str(mapdict['automatic']) == '1':
            modified_str = modified_str.replace(key,mapdict['replacement'])

    return modified_str


def mapfile_to_mapdict(mapfile_filepath: str, json_encoding: str = 'utf-8') -> dict:

    with open(mapfile_filepath, 'r', encoding=json_encoding) as mapfile_obj:
        map_dict = json.load(mapfile_obj)

    return map_dict

# Function to convert a CSV to JSON, Takes the file paths as arguments
def csv_to_json_dict(csvFilePath, json_filepath, csv_encoding='utf-8'):
    print(f"## Running csv_to_json_dict({csvFilePath=}, {json_filepath=}, {csv_encoding=})")

    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding=csv_encoding) as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary and add it to data
        for rows in csvReader:

            # Assuming a column named 'No' to be the primary key
            key = rows['original']
            # key = rows['No']
            data[key] = rows

    # Open a json writer, and use the json.dumps() function to dump data
    with open(json_filepath, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, indent=4))

def gen_outfilename(input_filename: str, suffix: str = '-processed', keep_extension: bool = True) -> str:

    # Grab "base" of filename without extension
    new_filename = os.path.splitext(input_filename)[0] + suffix
    if keep_extension:
        new_filename += os.path.splitext(input_filename)[1]
    
    return new_filename

def main(args):

    do_csv_convert = False

    csv_mapping_file = 'html-replacement-v3.csv'
    csv_encoding = 'utf-8'
    # csv_encoding = 'iso8859-1'
    # csv_encoding = 'cp1252'
    json_mapfile_filepath = 'html-replace-v3.json'

    if do_csv_convert:
        csv_to_json_dict(csv_mapping_file, json_mapfile_filepath, csv_encoding=csv_encoding)

    map_dict = mapfile_to_mapdict(json_mapfile_filepath)

    for source_file in args.source_file:

        # with open(source_file,'r', encoding='utf-8') as source_fileobj:
            # source_string = source_fileobj.read()
            source_string = source_file.read()

            remapped_string = replace_strings_mapdict(source_string, map_dict)
            if args.debug:
                print('-- Source Data --')
                pprint(source_string)
                print('-- Destination Data --')
                print(remapped_string)
            if args.displayonly:
                if args.showfilename:
                    print(f'[ {source_file.name} ]')
                print(remapped_string)
            else:
                out_opts = {}
                out_opts['keep_extension'] = not args.dropextension
                if args.customsuffix:
                    out_opts['suffix'] = args.customsuffix
                out_filename = gen_outfilename(source_file.name, **out_opts)
                print(f'WOULD SAVE TO A FILE NAMED: {out_filename}')
                # with open('test-out-converted.txt','w') as out_file:
                #     out_file.write(remapped_string)

    # # pprint(map_dict)
    # pprint(remapped_string)

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'error: {message}\n\n')
        self.print_help()
        # sys.stderr.write(f'error: {message}\n\nTry running with --help')
        sys.exit(2)

def parse_args() -> dict:
    help_text = """
    This tool converts special characters to their HTML versions, e.g. &#1234;.
    The output file(s) will be saved as filename-processed.txt.
    """
    # parser = argparse.ArgumentParser(description='HTML Processor')
    parser = MyParser(description='Special character to HTML processor')
    # parser.add_argument('source_file', help='The file to process,')
    parser.add_argument('source_file', type=argparse.FileType('r'), nargs='+',
                        help='The file(s) to process')
    
    write_grp = parser.add_argument_group(title='File Writing/Saving Options',
                                          description='These options let you customize the file saving/naming behavior. If you wish to save with a custom filetype, combine --dropextension with --customsuffix')
    # write_grp.add_argument('--outfile','-f', help='OPTIONALLY set a custom target filename')
    write_grp.add_argument('--customsuffix','-s', help='Set a custom suffix to add to the file when saving')
    write_grp.add_argument('--dropextension','-x', action="store_true",
                                    help='Set a custom suffix to add to the file when saving')

    output_group = parser.add_argument_group(title='Display / stdout')
    output_group.add_argument('--displayonly','-d', action="store_true",
                              help='Display the data only; do not write output files')
    output_group.add_argument('--showfilename','-n', action="store_true",
                              help='Display the filename above the output (e.g. if processing multiple files)')

    parser.add_argument('--debug', action="store_true", help='Display debugging information')

    args = parser.parse_args()
    return args

# Main - boilerplate plus argparse

if __name__ == "__main__":
    # # Set up ArgParse - we don't need it if we're being used as a module, etc
    cli_arguments = parse_args()

    main(cli_arguments)
