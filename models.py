class LogEntry:
    def __init__(self, line):
        self.line = line
        self.type = self.detect_type()

    def detect_type(self):
        if "ERROR" in self.line:
            return "ERROR"
        elif "WARNING" in self.line:
            return "WARNING"
        else:
            return "INFO"