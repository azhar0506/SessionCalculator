import sys
from datetime import datetime, timedelta

def parse_log_entry(entry):
    try:
        time, user, status = entry.split()
        datetime.strptime(time, "%H:%M:%S")  # Check if time format is correct
        return time, user, status
    except ValueError:
        return None

def calculate_session_durations(log_entries):
    sessions = {}
    starts = {}
    earliest_time = log_entries[0].split()[0]
    latest_time = log_entries[-1].split()[0]

    for entry in log_entries:
        parsed = parse_log_entry(entry)
        if not parsed:
            continue

        time, user, status = parsed

        if user not in sessions:
            sessions[user] = {'total_duration': timedelta(0), 'session_count': 0}

        if status == 'Start':
            starts.setdefault(user, []).append(time)
        else:
            start_time = starts[user].pop(0) if starts.get(user) else earliest_time
            end_time = time
            duration = datetime.strptime(end_time, "%H:%M:%S") - datetime.strptime(start_time, "%H:%M:%S")
            sessions[user]['total_duration'] += duration
            sessions[user]['session_count'] += 1

    # Handle sessions that are still ongoing at the end of the log
    for user, start_times in starts.items():
        for start_time in start_times:
            duration = datetime.strptime(latest_time, "%H:%M:%S") - datetime.strptime(start_time, "%H:%M:%S")
            sessions[user]['total_duration'] += duration
            sessions[user]['session_count'] += 1

    return sessions

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            log_entries = file.readlines()

        sessions = calculate_session_durations(log_entries)

        for user, data in sessions.items():
            total_seconds = int(data['total_duration'].total_seconds())
            print(f"{user} {data['session_count']} {total_seconds}")
    except FileNotFoundError:
        print("Error: SessionCalculator.py missing - {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: SessionCalculator.py <path_to_log_file>")
    else:
        main(sys.argv[1])
