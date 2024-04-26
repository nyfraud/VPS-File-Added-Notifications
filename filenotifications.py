import os
import time
import requests

# Discord webhook URL
WEBHOOK_URL = "Webhook Link Here" #webhook link

# Directory to monitor
MONITORED_DIR = "/root"  #change to file location you want to watch

def send_discord_notification(filename):
    payload = {
        "content": f":file_folder: New file added: {filename}"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            print(f"Notification sent for {filename}")
        else:
            print(f"Failed to send notification for {filename}: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error sending notification for {filename}: {e}")

def monitor_directory():
    existing_files = set(os.listdir(MONITORED_DIR))
    while True:
        current_files = set(os.listdir(MONITORED_DIR))
        new_files = current_files - existing_files
        for filename in new_files:
            send_discord_notification(filename)
        existing_files = current_files
        time.sleep(1)  # Check every minute

if __name__ == "__main__":
    monitor_directory()
