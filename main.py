import speedtest
from dotenv import load_dotenv
from datetime import datetime
import os

def byte_to_mb(byte):
    return byte / 1024 / 1024
    
def get_folder_name():
    with open("db.txt", "r") as f:
        return f.read().strip()

def set_folder_name(folder_name):
    with open("db.txt", "w") as f:
        f.write(folder_name)

def create_folder_name(speed):
    return "--- Upload Speed " + str(round(byte_to_mb(speed), 2)) + " MBps ---"

def main():
    load_dotenv()
    threads = None

    # get current speeds
    s = speedtest.Speedtest(secure=True)
    upload_speed = s.upload(threads=threads)
    download_speed = s.download(threads=threads)

    # get folder names
    folder_name = get_folder_name()
    new_folder_name = create_folder_name(upload_speed)

    print("Current upload", create_folder_name(upload_speed))
    print("Current folder name", folder_name)
    print("New folder name", new_folder_name)

    # rename the folder
    base_dir = os.environ.get("BASE_DIR")
    os.rename(base_dir + folder_name, base_dir + new_folder_name)
    set_folder_name(new_folder_name)


    # add upload and download to db
    with open(base_dir + new_folder_name + "\data.csv", "a") as f:
        f.write(datetime.now().strftime("%d.%m.%Y %H:%M") + "," +str(round(byte_to_mb(upload_speed), 2)) + "," + str(round(byte_to_mb(download_speed), 2)) + "\n")

if __name__ == '__main__':
    main()