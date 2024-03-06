from pytube import YouTube
from pytube import Stream

def download_audio(link: str, output_path: str):
    yt = YouTube(link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=output_path)

if __name__ == "__main__":
    link = input("Enter the YouTube video link: ")
    output_path = input("Enter the output path to save the audio file: ")
    download_audio(link, output_path)
