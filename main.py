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
    file = open("results.txt", "w")
    file.write("Log Analysis Results\n")
    file.write("--------------------\n")
    file.write("INFO count: " + str(info_count) + "\n")
    file.write("WARNING count: " + str(warning_count) + "\n")
    file.write("ERROR count: " + str(error_count) + "\n")
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