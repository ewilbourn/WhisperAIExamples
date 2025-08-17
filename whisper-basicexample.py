import whisper

model = whisper.load_model("base")
audio = "C:/Users/ewilb/Downloads/Speech/WhatAICanDo.m4a"

result = model.transcribe(audio, fp16=False, language="en")
print(result["text"])