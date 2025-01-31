import sys
import os
import bisect

def create_index(log_file, index_file):
    index = {}
    with open(log_file, 'r') as f:
        while True:
            pos = f.tell()
            line = f.readline()
            if not line:
                break
            date = line.split()[0]
            if date not in index:
                index[date] = pos
    with open(index_file, 'w') as f:
        for date, pos in sorted(index.items()):
            f.write(f"{date} {pos}\n")

def load_index(index_file):
    index = {}
    with open(index_file, 'r') as f:
        for line in f:
            date, pos = line.strip().split()
            index[date] = int(pos)
    return index

def extract_logs(log_file, index, date):
    if date not in index:
        return []
    
    with open(log_file, 'r') as f:
        f.seek(index[date])
        logs = []
        while True:
            line = f.readline()
            if not line or not line.startswith(date):
                break
            logs.append(line)
        return logs

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    date = sys.argv[1]
    log_file = 'test_logs.log'
    index_file = 'log_index.txt'
    
    if not os.path.exists(index_file):
        print("Creating index...")
        create_index(log_file, index_file)
    
    index = load_index(index_file)
    logs = extract_logs(log_file, index, date)
    
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'output_{date}.txt')
    
    with open(output_file, 'w') as f:
        for log in logs:
            f.write(log)
    
    print(f"Logs for {date} have been saved to {output_file}")

if __name__ == "__main__":
    main()