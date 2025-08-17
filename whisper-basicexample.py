import whisper

model = whisper.load_model("base")
# m4a file can be downloaded here: https://aka.ms/mslearn-speech-files 
audio = "C:/Users/ewilb/Downloads/Speech/WhatAICanDo.m4a"

result = model.transcribe(audio, fp16=False, language="en")

print(result["text"])
