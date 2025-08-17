# Introduction
This is some code I wrote using the WhisperAI, PyTube, and StreamLit APIs to introduce high schoolers to working with open-source AI API models. These students had been using Carnegie Mellon's CS Academy [Python graphics API](https://pypi.org/project/cmu-graphics/) to learn coding in their AP CSP class. This code was part of a demo where I introduced them to various Python APIs they could utilize for speech-to-text projects.

- WhisperAI is a speech-to-text open source model. You feed it audio, and it detects the language and transcribes it for you. 
- Pytube is an open-source library that allows you to interact with videos, channels, and playlists on Youtube free of charge.
- Streamlit is an open-source framework designed to create web applications for data science and machine learning projects with minimal effort. It is a Python-based library that allows data scientists and machine learning engineers to build and share web apps quickly without needing extensive knowledge of web development.

# Get started with Whisper AI on Windows
1.	Install Python
- From Whisper AI documentation: [“We used Python 3.9.9 and PyTorch 1.10.1 to train and test our models, but the codebase is expected to be compatible with Python 3.8-3.11 and recent PyTorch versions.”](https://github.com/openai/whisper?tab=readme-ov-file#setup)
- [Install Python 3.11.8](https://www.python.org/downloads/release/python-3118/)
- After installing Python, to ensure other commands work as expected, ensure python.exe and pip.exe are added to the Windows Path
  -  [Add Python To Path](https://realpython.com/add-python-to-path/)
  -	[[Solved] 'pip' is not recognized as an internal or external command, operable program or batch file](https://www.youtube.com/watch?v=Jw_MuM2BOuI)
2.	Install Whisper AI Model: 
-	[Whisper AI Documentation](https://github.com/openai/whisper)
-	Open up a Command Prompt terminal and run: pip install -U openai-whisper
3.	Install FFmpeg
-	This wiki has the best instructions to download ffmpeg. Follow each step exactly as it says to. [How to Install FFmpeg on Windows: A Step-by-Step Guide](https://www.wikihow.com/Install-FFmpeg-on-Windows)
4.	VSCode
- [Download VSCode](https://code.visualstudio.com/download)
- Create a new folder and open it in VSCode. Create a new Python file in this folder.
- Then, copy the ffmpeg.exe file into the folder of your python file so the whisper code will execute properly. This is what your VSCode should look like:
<img width="1217" height="417" alt="image" src="https://github.com/user-attachments/assets/a064f5e5-a4d9-4ac4-b898-dd94efa75158" />

-	Note: The ffmpeg.exe will be in the ffmpeg/bin folder. The ffmpeg folder should be in your root directory from step 3.
<img width="1186" height="336" alt="image" src="https://github.com/user-attachments/assets/48eee61b-7b1e-4bd6-b9be-047736206f1b" />

<img width="1169" height="319" alt="image" src="https://github.com/user-attachments/assets/d125631f-680f-4f18-a3c8-fac27d007002" />

5.	Tutorial on writing and executing Python in VSCode: [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
6.	[Streamlit API documentation](https://docs.streamlit.io/)
-	[Installation instructions](https://docs.streamlit.io/get-started/installation) 
-	[Install Streamlit AudioRecorder library](https://docs.streamlit.io/get-started/installation)
  -	Note: Streamlist AudioRecorder is an extension of Streamlit
-	You will end up running two different “pip install” commands to install streamlit and streamlist audiorecorder
7.	[Pytube documentation](https://app.readthedocs.org/projects/python-pytube/downloads/pdf/stable/#:~:text=The%20on_complete_callback%20function%20will%20run%20after%20a%20video,a%20video%20like%20trimming%20the%20length%20of%20it.)
-	Navigate to “User Guide” section of documentation for installation instructions

# Files in Repository
Each of these code segments build off of one another.
## whisper-basicexample.py
This code is the most basic usage of the Whisper AI API. Whisper transcribes an audio file downloaded to your computer and prints out the transcription to the console.
This is a link to the hardcoded mp4 audio file: https://aka.ms/mslearn-speech-files  
## whisper-pytubeexample.py
This is an extension of the basic example where you utilize PyTube to download a YouTube video via a url and then Whisper transcribes the video's audio and prints the transcription to the console.
## whisper-detectlangandtranscribe.py
An extension of the pytube example. When demonstrating this code, I found a YouTube video in a language other than English to demonstrate that Whisper was able to accurately detect the language being spoken. The transcription in that language is then printed to the console.
## streamlit-recordaudio.py
An extension of the detect lang and transcribe. This is code that utilizes the StreamLit API so that the user can record and transcribe audio using a website in the browser. Streamlit allows you to create a website in Python without any prior knowledge of building websites from scratch.

- Note: While all the files with the "whisper" prefix can be ran directly in VSCode, the StreamList code needs to be executed from a Command Prompt terminal. More instructions can be found [here](https://docs.streamlit.io/get-started/fundamentals/main-concepts).
<img width="1224" height="417" alt="image" src="https://github.com/user-attachments/assets/208194cb-f1f8-4035-997b-d24874e7062a" />

# Resources
## Whisper AI
Introducing Whisper | OpenAI
openai/whisper: Robust Speech Recognition via Large-Scale Weak Supervision
Really Real Time Speech To Text · openai/whisper · Discussion #608
OpenAI Whisper – Converting Speech to Text | GeeksforGeeks
Creating an Audio Transcription and Summarization with OpenAI’s Whisper and Python | by Alex Rodrigues | Medium
OpenAI Whisper Python Tutorial: Step-by-Step Guide - Analyzing Alpha

## Pytube and Streamlit documentation
python - get_highest_resolution function doesn't work in pytube - Stack Overflow
streamlit-audiorecorder/README.md at main · theevann/streamlit-audiorecorder
How to Build a Voice Transcription and Translation App with OpenAI Whisper and Streamlit | HackerNoon

## Text-to-Speech Open Source model
synesthesiam/opentts: Open Text to Speech Server
canopyai/Orpheus-TTS: Towards Human-Sounding Speech
