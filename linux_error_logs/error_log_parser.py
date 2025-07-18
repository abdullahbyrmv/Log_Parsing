import re

log_file_path = "/var/log/apache2/error.log"
output_file_path = "/home/abdbyrmv/Desktop/log_parsing/linux_error_logs/parsed_error_logs.txt"

structured_log_pattern = re.compile(
    r'^\[(?P<timestamp>[\w\s:.]+)\] '
    r'\[(?P<module>[^:\]]+):(?P<level>[^\]]+)\] '
    r'\[pid (?P<pid>\d+):tid (?P<tid>\d+)\] '
    r'(?P<error_code>AH\d{5}): (?P<message>.*)'
)

simple_pattern = re.compile(
    r'^(?P<error_code>AH\d{5}): (?P<message>.*)'
)

parsed_logs = []

try:
    with open(log_file_path, "r") as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue

            match = structured_log_pattern.match(line)
            if match:
                parsed_logs.append(match.groupdict())
            else:
                simple_match = simple_pattern.match(line)
                if simple_match:
                    parsed_logs.append(simple_match.groupdict())
                else:
                    print(f"[Line {line_number}] Could not parse: {line}")

    with open(output_file_path, "w") as out_file:
        for i, entry in enumerate(parsed_logs, 1):
            out_file.write(f"[Line {i}] {entry}\n")

    print(f"\nParsing FInished")

except FileNotFoundError:
    print(f"File not found within specified path: {log_file_path}")
