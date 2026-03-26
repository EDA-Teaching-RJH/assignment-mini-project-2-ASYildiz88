import re


def is_error(line):
    return re.search("ERROR", line)


def is_warning(line):
    return re.search("WARNING", line)


def is_info(line):
    return re.search("INFO", line)