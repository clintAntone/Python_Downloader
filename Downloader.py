#This is a comment in Python
#First, you need to install a package named 'pytube'
#   pip3 install pytube

#From pytube, we will be using YouTube
from pytube import YouTube

#From pytube.cli, we will be using the on_progress method
from pytube.cli import on_progress


#We will define a function that will get the YouTube link and the download destination
#I set the download_dir to None so this will become optional
def downloader(video_link, download_dir=None):
    try:
        #I added a progress bar so we know the download progress
        tube = YouTube(video_link,on_progress_callback=on_progress)
        title = tube.title

        print("Now downloading, '"+ str(title) +"'")
        video = tube.streams.filter(progressive=True, file_extension='mp4').first()
        print('FileSize: ' + str(round(video.filesize/(1024*1024))) + 'MB')

        #Let's check if there is a directory provided
        if download_dir is not None:
            video.download(download_dir)
        else:
            video.download()
        print("Download completed, '" +str(title) + "'")

    except Exception as ex:
        print("Error Downloading video: | '" + str(video_link) + "'")


#Now let's call the function
#I will change the download path as C drive will need added authorization
#I will save the file to the downloads folder
downloader('https://www.youtube.com/watch?v=qhc_NG17_mA&ab_channel=HisLifeTV','/Users/COLLABERA/Downloads/')


#######Thanks!! That's all
