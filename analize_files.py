import os
import re
import argparse

from collections import Counter


def parse_file(file_name) -> list:
    frames_numbers = []

    with open(file_name, 'r') as f:
        for line in f:
            a = line.split(',')[0]
            frames_numbers.append(a)

    return frames_numbers


def analize_files(folder_name, percent) -> list:
    os.chdir(folder_name)

    files = []

    for f in os.listdir('.'):
        folder_content = re.match(r'(^result_p1[01]\.[02468]_p2[01]\.[02468].txt$)', f)
        if folder_content and os.path.isfile(f):
            files.append(folder_content.group(0))

    count_files = len(files)

    cnt = Counter()
    for f in files:
        cnt += Counter(parse_file(f))

    return [key for key, value in cnt.items() if float(value * 100 / count_files) >= percent]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Getting folder name and percentage')
    parser.add_argument('folder_name', type=str)
    parser.add_argument('percent', type=float)
    arguments = parser.parse_args()
    res = analize_files(arguments.folder_name, arguments.percent)

    with open('the_most_popular_frames.txt', 'w') as result:
        result.write(','.join(res))
