README.txt for SessionCalculator.py
------------------------------------

Description:
------------
SessionCalculator.py is a Python script designed to process log files for session management. It reads a log file containing session start and end times for different users and calculates the total duration and number of sessions for each user.

Requirements:
-------------
- Python 3

Usage:
------
To run the script, use the following command in the terminal:

python SessionCalculator.py <path_to_log_file>

Replace <path_to_log_file> with the actual path to your log file.

Example:
python3 SessionCalculator.py logs.txt

Input File Format:
------------------
The log file should contain entries in the following format:
HH:MM:SS USERNAME Start/End

Each entry should be on a new line.


Output:
-------
The script outputs the total duration and the number of sessions for each user to the console.

Assumptions:
------------
- The log file entries are chronologically ordered.
- Each 'Start' and 'End' entry in the log file is correctly formatted.

Note:
-----
This script is written and tested in Python 3.11.4 If you are using a different Python version, some adjustments may be required.
The document does mention to use Python 2.7 however I am unable to download that into my linux machine. I can provide the code in Python 2.7, however it will not be tested. The changes will be mainly around the print statement, exception handling and dictionary access.

