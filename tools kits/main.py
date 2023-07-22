from pystyle import Colorate, Colors
import pytube
import os
from moviepy.editor import VideoFileClip, AudioFileClip
import requests
import colorama
import sys
import re
from discord_webhook import DiscordWebhook
import time



class LogNoID:
    @staticmethod
    def Success(message):
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.LIGHTGREEN_EX}+{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.WHITE} {message}")

    @staticmethod
    def Mild(message):
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.YELLOW}/{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.WHITE} {message}")

    @staticmethod
    def Failed(message):
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RED}-{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.WHITE} {message}")


class Logger:
    @staticmethod
    def Success(message, idnum):
        print(f"{colorama.Fore.BLUE}({idnum}) {colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.LIGHTGREEN_EX}+{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.WHITE} {message}")

    @staticmethod
    def Mild(message, idnum):
        print(f"{colorama.Fore.BLUE}({idnum}) {colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.YELLOW}/{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.WHITE} {message}")

    @staticmethod
    def Failed(message, idnum):
        print(f"{colorama.Fore.BLUE}({idnum}) {colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RED}-{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.WHITE} {message}")


def youtube_downloader():
    url = input("Enter YouTube URL: ")
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print("Downloading...")
        stream.download()
        print("Download completed!")
    except pytube.exceptions.PytubeError as e:
        print(f"Error while downloading: {e}")


def tiktok_downloader():
    url = input("Enter TikTok URL: ")
    try:
        video = VideoFileClip(url)
        video.write_videofile("tiktok_video.mp4", codec='libx264')
        print("Download completed!")
    except Exception as e:
        print(f"Error while downloading: {e}")


def mp4_to_mp3():
    mp4_file = input("Enter the name of the MP4 file: ")
    mp3_file = input("Enter the name of the MP3 file: ")
    try:
        video = VideoFileClip(mp4_file)
        audio = video.audio
        audio.write_audiofile(mp3_file)
        audio.close()
        video.close()
        print("Conversion completed!")
    except Exception as e:
        print(f"Error while converting: {e}")


def mkv_to_mp4():
    mkv_file = input("Enter the name of the MKV file: ")
    mp4_file = input("Enter the name of the MP4 file: ")
    try:
        video = VideoFileClip(mkv_file)
        video.write_videofile(mp4_file)
        print("Conversion completed!")
    except Exception as e:
        print(f"Error while converting: {e}")


def ogg_to_mp3():
    ogg_file = input("Enter the name of the OGG file: ")
    mp3_file = input("Enter the name of the MP3 file: ")
    try:
        audio = AudioFileClip(ogg_file)
        audio.write_audiofile(mp3_file)
        audio.close()
        print("Conversion completed!")
    except Exception as e:
        print(f"Error while converting: {e}")


def mp4_to_mkv():
    mp4_file = input("Enter the name of the MP4 file: ")
    mkv_file = input("Enter the name of the MKV file: ")
    try:
        video = VideoFileClip(mp4_file)
        video.write_videofile(mkv_file, codec='libx264')
        print("Conversion completed!")
    except Exception as e:
        print(f"Error while converting: {e}")


def mkv_to_mp3():
    mkv_file = input("Enter the name of the MKV file: ")
    mp3_file = input("Enter the name of the MP3 file: ")
    try:
        video = VideoFileClip(mkv_file)
        audio = video.audio
        audio.write_audiofile(mp3_file)
        audio.close()
        video.close()
        print("Conversion completed!")
    except Exception as e:
        print(f"Error while converting: {e}")




def main():
    print(Colorate.Horizontal(Colors.blue_to_white, """
████████╗ ██████╗  ██████╗ ██╗         ██╗  ██╗██╗████████╗███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██║ ██╔╝██║╚══██╔══╝██╔════╝
   ██║   ██║   ██║██║   ██║██║         █████╔╝ ██║   ██║   ███████╗
   ██║   ██║   ██║██║   ██║██║         ██╔═██╗ ██║   ██║   ╚════██║
   ██║   ╚██████╔╝╚██████╔╝███████╗    ██║  ██╗██║   ██║   ███████║
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝

"""))
    print(Colorate.Horizontal(Colors.blue_to_white, "       By 2bartek | Discord: https://discord.gg/evVZ7fg6S2"))
    print("")

    print(Colorate.Horizontal(Colors.yellow_to_red, "   ┬─────────────────────────────┬───────────────────────────┬"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "   │      download Tools         │     Conventer Tools       │"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "   │─────────────────────────────┼───────────────────────────│"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "   │ [1] youtube downloader      │ [6] mp4 to mp3            │"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "   │ [2] tiktok downloader       │ [7] mkv to mp4            │"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "   │                             │ [8] ogg to mp3            │"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "   │                             │ [9] mp4 to mkv            │"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "   │                             │ [10] mkv to mp3           │"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "   └─────────────────────────────┴───────────────────────────┴"))


if __name__ == "__main__":
    main()
    choice = input("> >: ")
    if choice == "1":
        youtube_downloader()
    elif choice == "2":
        tiktok_downloader()
    elif choice == "6":
        mp4_to_mp3()
    elif choice == "7":
        mkv_to_mp4()
    elif choice == "8":
        ogg_to_mp3()
    elif choice == "9":
        mp4_to_mkv()
    elif choice == "10":
        mkv_to_mp3()
    else:
        print("Invalid choice.")

