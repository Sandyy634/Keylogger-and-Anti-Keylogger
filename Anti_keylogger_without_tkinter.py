# FULL RESTORED CODE

import os
import psutil
import threading
import time
import datetime
import sys

SUSPICIOUS_KEYWORDS = ['keylog', 'key_logger', 'pynput', 'keyboard', 'listener', 'capture', 'record']
detecting = False
scanner_thread = None
initial_processes = set()
log_entries = []

def log(msg):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    entry = f"{timestamp} {msg}"
    log_entries.append(entry)
    print(entry)

def get_process_snapshot():
    procs = set()
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = ' '.join(proc.info['cmdline']).lower()
            procs.add((proc.info['pid'], cmdline))
        except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
            continue
    return procs

def detect_keylogger_process():
    global initial_processes
    current_procs = get_process_snapshot()
    new_procs = current_procs - initial_processes

    for pid, cmdline in new_procs:
        if any(keyword in cmdline for keyword in SUSPICIOUS_KEYWORDS):
            msg = f"⚠️ KEYLOGGER FILE STARTED: {cmdline} AT {datetime.datetime.now().strftime('%H:%M:%S')}"
            log(msg)
            initial_processes = current_procs
            break

def run_scanner():
    global detecting
    while detecting:
        detect_keylogger_process()
        time.sleep(3)

def start_detection():
    global detecting, scanner_thread, initial_processes
    if not detecting:
        log_entries.clear()
        initial_processes = get_process_snapshot()
        detecting = True
        scanner_thread = threading.Thread(target=run_scanner, daemon=True)
        scanner_thread.start()
        log("🟢 Detection started. Waiting for suspicious keylogger processes...")

def stop_detection():
    global detecting
    detecting = False
    log("⛔ Detection stopped.")

def export_logs():
    if not log_entries:
        print("ℹ️ No logs to export.")
        return
    file_path = input("Enter filename to save logs (e.g., logs.txt): ").strip()
    if file_path:
        with open(file_path, 'w') as f:
            f.write('\n'.join(log_entries))
        print(f"✅ Logs saved to {file_path}")

def show_menu():
    print("\n--- Anti-Keylogger CLI Menu ---")
    print("1. Start Detecting")
    print("2. Stop Detecting")
    print("3. Export Logs")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            start_detection()
        elif choice == '2':
            stop_detection()
        elif choice == '3':
            export_logs()
        elif choice == '4':
            stop_detection()
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_detection()
        print("\nDetection interrupted by user.")
