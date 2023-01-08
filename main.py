# importing packages
from pytube import YouTube,Playlist

data = []

print("<== Welcome To YouTube Video Downlaoder ==>")

def AllPlaylistLinks(url):
  links = Playlist(url)
  return links
  
# download single music
def downloadMusic(url, SAVE_PATH):
  yt = YouTube(url) 
  try:
    yt.streams.filter(progressive = True, 
  file_extension = "mp4").first().download(output_path = SAVE_PATH,filename = f"{yt.title}.mp4")
    print(yt.title + " has been successfully downloaded.")
  
  except :
    print("Sorry: Falid To Downaload Video")
  
# downlaod more then one music
def DownlaodAll(data):
  try:
      for index, i in enumerate(data):
        print("    ----    ")
        print(str(len(data))+" Out Of "+ str(index+1))
        downloadMusic(i, "Videos")
        print("    ----    ")
      print("Your Video Downlaod in Videos Folder")
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