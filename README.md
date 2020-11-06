# python-question-real-deal

### How to run
```bash
python3 analyze_files.py --fn <folder_name> --p <percent>
```

I would check this program as follows:

1. There are no files for analyzing in folder
2. There are not only files for analyzing but others files with another names, and subdirectories as well
3. Check if files for analyzing are not executable. It may be dangerous to open them
4. Check format of input files:
    - file is not empty
    - no letters and special symbols
    - each line consists of 5 comma-separated elements
5. Check folder name and percent as input parameters:
    - absolute and relative path works correctly
    - incorrect folder name
    - empty folder name
    - incorrect percent: i.e. percent with letters, negative number or >100
    - empty value in percent, by default it's 30
6. Size of files. They should not be too long
