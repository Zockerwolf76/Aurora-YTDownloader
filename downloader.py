from pytube import YouTube as Yt
from pytube.cli import on_progress
from pathlib import Path
from moviepy.editor import *
import os.path
import time
from termcolor import colored

def print_header():
    print(colored('Welcome to Aurora YouTube Downloader V.1.1\n', 'green'))

def get_youtube_link():
    return input(colored("Enter the YouTube link: ", 'red'))

def get_youtube_video(link):
    yt = Yt(link, on_progress_callback=on_progress)
    return yt

def print_video_info(yt):
    print(f"Title: {colored(yt.title, 'green')}")
    print(f"Number of views: {colored(yt.views, 'blue')}")
    print(f"Length of video: {colored(yt.length, 'magenta')} seconds\n")

def get_download_choice():
    print("Do you want to download the video?")
    choice = input(colored("(1) Yes!\n(2) No!\n", 'yellow'))
    return choice

def get_download_mode():
    print("Please choose a download mode:")
    mode = input(colored("(1) Audio & Video\n(2) Audio only\n(3) Exit\n", 'yellow'))
    return mode

def get_download_path():
    path = input(colored("Enter download location: ", 'red'))
    pathv = Path(path)
    if os.path.exists(pathv):
        return path
    else:
        print(colored("Invalid path!", 'red'))
        exit()

def download_video(yt, path):
    print("Please wait while getting Video Streams for Audio & Video...")
    time.sleep(3)
    print(colored(f"Downloading {yt.title}...\n", 'green'))
    ys = yt.streams.get_highest_resolution()
    ys.download(path)
    print(colored(f"\nDone! Your Video is located under {path}\n", 'green'))

def download_audio(yt, path):
    print("Please wait while getting Video Streams for Audio only...")
    time.sleep(3)
    print(colored(f"Downloading {yt.title}...\n", 'green'))
    ys = yt.streams.get_lowest_resolution()
    videof = ys.download(path)
    videot = VideoFileClip(videof)
    videot.audio.write_audiofile(f"{path}/{yt.title}.mp3")
    os.remove(videof)
    print(colored(f"\nDone! Your Audio is located under {path}\n", 'green'))

def handle_download_choice(choice, yt):
    if choice == "1":
        mode = get_download_mode()
        if mode == "1":
            path = get_download_path()
            download_video(yt, path)
        elif mode == "2":
            path = get_download_path()
            download_audio(yt, path)
        elif mode == "3":
            print(colored("Ok maybe later.\n", 'yellow'))
            exit()
        else:
            print(colored("Invalid input!", 'red'))
            exit()
    elif choice == "2":
        print(colored("Ok maybe later.\n", 'yellow'))
        exit()
    else:
        print(colored("Invalid input!", 'red'))
        exit()

if __name__ == '__main__':
    print_header()
    link = get_youtube_link()
    yt = get_youtube_video(link)
    print_video_info(yt)
    choice = get_download_choice()
    handle_download_choice(choice, yt)
    