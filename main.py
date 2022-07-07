from pytube import YouTube
import time
from pytube.cli import on_progress
import os.path
from pathlib import Path


print('''Welcome to Aurora YouTube Downloader and Converter v0.2 Alpha \n''')
print('''Loading...\n''')
time.sleep(5)

link = input("Enter the youtube link: \u001b[31m")
yt = YouTube(link, on_progress_callback=on_progress)

time.sleep(3)
print("\u001b[0m" + "\n" + "Get Video pls wait...\n")
time.sleep(5)

print("Title: ",f"\u001b[32m {yt.title}","\u001b[0m")
print("Number of views: ",f"\u001b[34m {yt.views}", "\u001b[0m")
print("Length of video: ",f"\u001b[35m {yt.length}","seconds", "\u001b[0m" + "\n")
time.sleep(3)

print("Do u want to download it? Please choose: \n")
print("(1) Yes! \n" + "(2) No! \n")

choice = input("Choice: ")

if choice == "1":
    time.sleep(3)
    print("\n" + "Please wait while getting Video Streams...\n")
    time.sleep(3)
    path = input("Download location: ")
    pathv = Path(path)
    if os.path.exists(pathv):
        time.sleep(3)
        print("\n" + "Try to get Download... \n")
        ys = yt.streams.get_highest_resolution()
        time.sleep(3)
        print(f"Downloading {yt.title}... \n")
        ys.download(path)
        print("\n"+ "\n" + f"Done! Your Video is located under {path} \n")
    else:
        print("\n" + "Invalid path. \n")
        exit()

elif choice == "2":
    print("\n" + "Ok maybe later. \n")
    exit()

else:
    print("\n" + "invalid input! \n")
    exit()
