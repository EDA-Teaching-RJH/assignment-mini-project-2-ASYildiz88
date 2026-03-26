import re


def count_logs(lines):
    info_count = 0
    warning_count = 0
    error_count = 0

    for line in lines:
        if re.search("ERROR", line):
            error_count += 1
        elif re.search("WARNING", line):
            warning_count += 1
        elif re.search("INFO", line):
            info_count += 1

    return info_count, warning_count, error_count


def main():
    file = open("logs.txt", "r")
    lines = file.readlines()

    info_count, warning_count, error_count = count_logs(lines)

    print("INFO count:", info_count)
    print("WARNING count:", warning_count)
    print("ERROR count:", error_count)

    file.close()


main()