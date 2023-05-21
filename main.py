from pytube import YouTube, Playlist

def video_dl(link, ):
    yt = YouTube(link)
    print("Choose the type of Download:\n1 - video\n2 - Audio")
    file_type = input("Enter your choice: ")
    if file_type == 1:
        resolution = input("Enter the resolution (if the entered resolution is not available highest will be the output): ")
        output_path = input("Enter the path for the download: ")
        print(f"Downloading {yt.title}")
        try:
            yt.streams.filter(res=resolution).first().download(output_path=output_path)
        except AttributeError:
            print("Downloading the highest quality as the entered was not available.")
            yt.streams.get_highest_resolution().download()
        print("Print Download Successful!")
    elif file_type == 2:
        audio_found = yt.streams.filter(only_audio=True).get_audio_only()
        filename = input("Enter the mp3 file name (don't use any special characters): ").lower()
        path = input("Enter the path of the file: ")
        audio_found.download(output_path=path ,filename=f"{filename}.mp3")
        print(f"Completed download of {yt.title} as audio file")

def playlist_dl(link):
    playlist = Playlist(link)
    print("Choose the type of Download:\n1 - video\n2 - Audio")
    file_type = input("Enter your choice: ")
    if file_type == 1:
        print(f"Starting Download of {playlist.title} containing {playlist.length} files as video")
        resolution = input("Enter the resolution for the video output: ")
        output_path = input("Enter the output path: ")
        for url in playlist.video_urls:
            yt = YouTube(url)
            try:
                yt.streams.filter(res=resolution).first().download(output_path=output_path)
            except AttributeError:
                print(f"{yt.title} was not available in {resolution}, downloading in the highest possible quality.")
                yt.streams.get_highest_resolution().download()
            print(f"Completed {yt.title}")
    elif file_type == 2:
        print(f"Starting Download of {playlist.title} containing {playlist.length} files as audio")
        output_path = input("Enter the output path: ")
        for url in playlist.video_urls:
            yt = YouTube(url)
            title = yt.title.replace("|", "")
            yt.streams.filter(only_audio=True).get_audio_only().download(filename=f"{title}.mp3")
            print(f"Completed {yt.title}")

print("Welcome to the Youtube Downloader")
print("Choose the type of your download:\n1 - Simple Video\n2 - Full Playlist")
type_of_download = input("Enter your choice: ")
if type_of_download == 1:
    link = input("Enter the video link: ")
    video_dl(link)
elif type_of_download == 2:
    link = input("Enter the playlist link: ")
    playlist_dl(link)