import os
import csv
import argparse

parser = argparse.ArgumentParser(
    description="Writes filenames from folder to a file, or print file content"
)

parser.add_argument("-p", "--path", type=str, required=False, help="path to folder")
parser.add_argument(
    "-f", "--file-name", type=str, required=False, help="name of the target file"
)
parser.add_argument(
    "-fn",
    "--file-names",
    type=str,
    required=False,
    help="list of file names, to print first line",
)
parser.add_argument(
    "-e",
    "--email-file-names",
    type=str,
    required=False,
    help="list of file names, to print lines containing an email",
)
parser.add_argument(
    "-md",
    "--md-files",
    type=str,
    required=False,
    help="list of md files, to print headlines",
)


def write_filenames_from_folder(path, file_name):
    with open(file_name, "w") as file:
        writer = csv.writer(file)
        for _, _, f in os.walk(path):
            writer.writerow(f)


def print_first_line(*file_names):
    for file in file_names:
        with open(file) as file:
            first_line = file.readline()
            print(first_line)


def print_email_line(*file_names):
    for file in file_names:
        with open(file) as file:
            lines = file.readlines()
            for line in lines:
                if "@" in line:
                    print(line.rstrip())


def print_headlines(*md_files):
    for file in md_files:
        with open(file) as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("#"):
                    print(line.rstrip())


arguments = parser.parse_args()
if arguments.path != None and arguments.file_name != None:
    write_filenames_from_folder(arguments.path, arguments.file_name)
elif arguments.file_names != None:
    print_first_line(arguments.file_names)
elif arguments.email_file_names != None:
    print_email_line(arguments.email_file_names)
elif arguments.md_files != None:
    print_headlines(arguments.md_files)
