import re

log_file = "/var/log/apache2/access.log"
output_file = "/home/abdbyrmv/Desktop/log_parsing/linux_access_logs/parsed_access_logs.txt"

log_pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - '
    r'\[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>[^"]+)" '
    r'(?P<status>\d{3}) (?P<size>\d+) '
    r'"(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)"'
)

parsed_logs = []

try:
    with open(log_file, 'r') as logfile:
        for line_number, line in enumerate(logfile, 1):
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                parsed_logs.append(data)

    with open(output_file, "w") as parsed_file:
        for i, entry in enumerate(parsed_logs, 1):
            parsed_file.write(f"{entry}\n")

    print(f"\n Parsing Process Completed")

except FileNotFoundError:
    print(f"File not found in specified path: {log_file_path}")
