import whisper
from pytubefix import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename="testFile")
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)

model = whisper.load_model("base")
result = model.transcribe("testFile", fp16=False)
print(result["text"])