import csv
import platform
import argparse

parser = argparse.ArgumentParser(
    description="Copy csv content to terminal or other file"
)

parser.add_argument(
    "-i", "--input-file", type=str, required=True, help="file with content to copy"
)
parser.add_argument("-f", "--file-name", type=str, required=False, help="file target")


def read_csv(input_file, file_name=None):
    my_list = []
    with open(input_file) as f:
        reader = csv.reader(f)
        for row in reader:
            my_list.append(row)
        if file_name == None:
            print(my_list)
        else:
            with open(file_name, "w") as file_object:
                output_writer = csv.writer(file_object)
                for line in my_list:
                    output_writer.writerow(line)


arguments = parser.parse_args()
read_csv(arguments.input_file, arguments.file_name)
