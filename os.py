import subprocess
import time

def open_multiple_windows(num_windows):
    processes = []

    for _ in range(num_windows):
        try:
            chrome_process = subprocess.Popen(['start', 'chrome.exe'], shell=True)
            processes.append(chrome_process)
        except FileNotFoundError:
            print("Chrome process not found.")

        try:
            edge_process = subprocess.Popen(['start', 'msedge.exe'], shell=True)
            processes.append(edge_process)
        except FileNotFoundError:
            print("Microsoft Edge process not found.")

        try:
            explorer_process = subprocess.Popen(['explorer.exe'], shell=True)
            processes.append(explorer_process)
        except FileNotFoundError:
            print("Windows Explorer process not found.")

        time.sleep(0.2)

    for process in processes:
        process.wait()

# Call the function with the desired number of windows to open (5 in this case)
open_multiple_windows()
