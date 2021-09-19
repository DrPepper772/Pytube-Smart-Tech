#import Youtube from pytube module
from pytube import YouTube
from pytube.cli import on_progress
import os

Invalid_url = True
Invalid_command = True
#use while loop to make sure url is correct format
#if url cant be readed by pytube, type in the url again
while Invalid_url:
    try:
        URL = str(input("Enter the URL of the video you want to download: \n>> "))
        yt =YouTube(URL, on_progress_callback=on_progress)
        Invalid_url = False
    #url not string or cant be detected by pytube
    except:
        print('Invalid URL. Please try again')
        
#add show valid command for user
print("Select download format:")
print("1: Video file with audio (.mp4)")
print("2: Audio only (.mp3)")

#use while loop to make sure command is correct
#if Invalid command input ,choose command again
while Invalid_command:
    try:
        media_type = input(">> ")
        if media_type == "1":
            #setting for mp4
            video = yt.streams.get_by_resolution("720p")
            #count file size
            filesize=round(video.filesize/(1024*1024))
            Invalid_command = False

        elif media_type == "2":
            #setting for mp3
            video = yt.streams.filter(only_audio = True).first()
            #count file size
            filesize=round(video.filesize/(1024*1024))
            Invalid_command = False
            
        #if command not equal to '1' / '2' run again
        else:
           print('Invalid command. Please Try again')
    except:
        print('Invalid Command. Please Try again')
print("Loading....")
#download video
out_file = video.download(output_path = os.path.expanduser("~\Downloads")) #~given path to user’s home directory

if media_type == "2":
    base, ext = os.path.splitext(out_file)#split the path name into a pair root and ext
    new_file = base + '.mp3'
    os.rename(out_file, new_file)#turns mp4 to mp3 audio file
    
#show size file
print('FileSize : ' + str(filesize) + 'MB')
#remind when video download success
print(yt.title + " has been successfully downloaded.")
#show file that download video
print("Your video will be saved to: "+ os.path.expanduser("~/Downloads"))
