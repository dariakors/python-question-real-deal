import os
import re
import argparse

from collections import Counter
from exceptions import FilesNotFoundException, FileFormatException, ExecutableFileException


def parse_file(file_name, cnt):

    with open(file_name, 'r') as f:
        for line in f:

            # check if there are not letters and special symbols in file
            if re.search('[a-zA-Z@_!#$%^&*()<>?/|}{~:]', line):
                raise FileFormatException("File format is not supported")

            splitted_list = line.split(',')

            # check the structure of file
            if len(splitted_list) != 5:
                raise FileFormatException("File is empty or file format is not supported")

            cnt[splitted_list[0]] += 1


def analyze_files(folder_name, percent) -> list:
    os.chdir(folder_name)

    files = []

    for f in os.listdir('.'):
        folder_content = re.match(r'(^result_p1[01]\.[02468]_p2[01]\.[02468].txt$)', f)
        if folder_content and os.path.isfile(f):

            # check if file is not executable
            if os.access(f, os.X_OK):
                raise ExecutableFileException("Ahtung! File is executable!")

            files.append(folder_content.group(0))

    count_files = len(files)

    # check if folder has not got necessary files
    if count_files == 0:
        raise FilesNotFoundException("Files are not found")

    cnt = Counter()
    for f in files:
        parse_file(f, cnt)

    return [key for key, value in cnt.items() if float(value * 100 / count_files) >= percent]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Getting folder name and percentage')
    parser.add_argument('--folder_name', '--fn', type=str)
    parser.add_argument('--percent', '--p', default=30, type=float)
    arguments = parser.parse_args()

    if arguments.percent > 100 or arguments.percent < 0:
        raise ValueError("Percent should be between 0 and 100")

    res = analyze_files(arguments.folder_name, arguments.percent)

    with open('the_most_popular_frames.txt', 'w') as result:
        result.write(','.join(res))
