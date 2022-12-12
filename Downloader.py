from pytube import YouTube
from pytube.cli import on_progress

def downloader(video_link, download_dir=None):
    try:
        #I added a progress bar so we know the download progress
        tube = YouTube(video_link,on_progress_callback=on_progress)
        title = tube.title

        print("Now downloading, '"+ str(title) +"'")
        video = tube.streams.filter(progressive=True, file_extension='mp4').first()
        print('FileSize: ' + str(round(video.filesize/(1024*1024))) + 'MB')

        if download_dir is not None:
            video.download(download_dir)
        else:
            video.download()
        print("Download completed, '" +str(title) + "'")

    except Exception as ex:
        print("Error Downloading video: | '" + str(video_link) + "'")


if __name__ == '__main__':
    yturl = input("YouTube link: ")
    download_dir = input("Save to: ")       
    downloader(yturl, download_dir)