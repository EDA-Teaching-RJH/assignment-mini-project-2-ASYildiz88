import json
from models import LogEntry


# count number of each log type
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


# save results into a JSON file
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
    # read log file
    file = open("logs.txt", "r")
    lines = file.readlines()
    file.close()

    # analyze logs
    info_count, warning_count, error_count = count_logs(lines)

    # print results
    print("INFO count:", info_count)
    print("WARNING count:", warning_count)
    print("ERROR count:", error_count)

    # save results
    save_results(info_count, warning_count, error_count)


main()