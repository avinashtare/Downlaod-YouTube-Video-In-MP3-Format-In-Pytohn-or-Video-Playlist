# importing packages
from pytube import YouTube,Playlist
import os

data = []

def AllPlaylistLinks(url):
  links = Playlist(url)
  return links

# download single music
def downloadMusic(url, savePath):
  # url input from user
  yt = YouTube(str(url))

  # extract only audio
  video = yt.streams.filter(only_audio=True).first()

  # check for destination to save file
  destination = savePath

  try:
    # download the file
    out_file = video.download(output_path=destination)
  
    # save the file
    base, ext = os.path.splitext(str(out_file))
    new_file = str(base)+'.mp3'
  
    os.rename(out_file, str(new_file))
  
    # result of success
    print(yt.title + " has been successfully downloaded.")
    if(yt):
      return 0

  except :
    print("Falid To Downaload file")

# downlaod more then one music
def DownlaodAll(data):
  try:
      for index, i in enumerate(data):
        print(len(data), index)
        downloadMusic(i, "Music")
  except:
      print("Sorry! Somting Woring In code")

isStart = input("You want to start programm [y,n].... ")
isPlaylist = None;
if(isStart == "y"):
  isPlaylist = input("Do You Want to Downlaod Playlist [y,n]...")

# Playlist or video downlaod
if(isPlaylist == "y"):
  url = input("Uplaod Playlist Url => ")
  data = AllPlaylistLinks(url)
  DownlaodAll(data)

elif(isPlaylist == "n"):
    url = input("Uplaod Video Url => ")
    data = [url];
    DownlaodAll(data)
      
print("Your Code is End...")