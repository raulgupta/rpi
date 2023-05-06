import os
import subprocess
import time
from datetime import datetime
import boto3
from gpiozero import LED

# Blink the LED 5 times with a 1 second delay between blinks
for j in range(5):
    os.system('echo 1 | sudo dd status=none of=/sys/class/leds/led0/brightness')
    time.sleep(1)

# Function to record video
def record_video(filename):
    cmd = f"libcamera-vid -t 7000 -o {filename}.h264 --qt-preview"
    subprocess.call(cmd.split())

# Function to upload file to S3
def upload_to_s3(filepath, bucket_name):
    s3 = boto3.client("s3")
    file_key = os.path.basename(filepath)
    s3.upload_file(filepath, bucket_name, file_key)

def main():

    # Generate a unique filename
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"video_{timestamp}"

    # Record video
    record_video(filename)

    # Upload to S3
    local_file_path = f"/home/stratas/{filename}.h264"
    bucket_name = "stratas-dashcam-bucket"
    upload_to_s3(local_file_path, bucket_name)
    print(f"Uploaded {filename}.h264 to S3 bucket {bucket_name}")

if __name__ == "__main__":
    main()

