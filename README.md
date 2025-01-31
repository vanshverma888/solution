# Problem

We have a huge log file (1 TB in size) with logs for multiple years. Each log starts with a date in the format YYYY-MM-DD. The task is to extract all logs for a specific date efficiently without loading the entire file into memory.

Solution Steps

Create an Index:
The script scans the log file once and creates an index.
The index maps each date (e.g., 2024-12-01) to its starting position (byte offset) in the file.
This index is saved to a file (log_index.txt) so we don’t need to scan the log file again.

Load the Index:
When you run the script, it loads the index from log_index.txt into memory.
This allows the script to quickly find where logs for a specific date start in the file.

Extract Logs:
The script uses the index to jump directly to the logs for the specified date.
It reads the file from that position and collects all logs for the date.
It stops when it finds logs for the next date.

Save the Logs:
The extracted logs are saved to a file in the output folder, named output_YYYY-MM-DD.txt.


How to Use

1. Download the Log File:
 Use the provided curl command to download the log file.
2. Run the Script:
 Run the script with the date you want to extract logs for:
python extract_logs.py 2024-12-01
3. Check the Output:
The logs for the specified date will be saved in output/output_YYYY-MM-DD.txt.

Example
If you run:
python extract_logs.py 2024-12-01

The script will:
1. Use the index to find where logs for 2024-12-01 start in the file.
2. Extract all logs for that date.
3. Save them to output/output_2024-12-01.txt.
