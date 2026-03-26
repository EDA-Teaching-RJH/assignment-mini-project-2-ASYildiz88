import json
from models import LogEntry


def count_logs(lines):
    info_count = 0
    warning_count = 0
    error_count = 0

    for line in lines:
        log = LogEntry(line)

        if log.type == "ERROR":
            error_count += 1
        elif log.type == "WARNING":
            warning_count += 1
        else:
            info_count += 1

    return info_count, warning_count, error_count


def save_results(info_count, warning_count, error_count):
    data = {
        "INFO": info_count,
        "WARNING": warning_count,
        "ERROR": error_count
    }

    file = open("results.json", "w")
    json.dump(data, file, indent=4)
    file.close()


def main():
    file = open("logs.txt", "r")
    lines = file.readlines()
    file.close()

    info_count, warning_count, error_count = count_logs(lines)

    print("INFO count:", info_count)
    print("WARNING count:", warning_count)
    print("ERROR count:", error_count)

    save_results(info_count, warning_count, error_count)


main()