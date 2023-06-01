Assignment 1: Real-time Voice Transcription App
-----------------------------------------------

**Objective**: Create a real-time voice transcription app using Streamlit.

### Problem Statement

We want you to develop a web application that allows users to transcribe their speech in real-time. The user should be able to click a microphone button and have their speech transcribed automatically as they speak. Your task is to modify an existing speech-to-text app to achieve real-time transcription functionality.


########################################################################################
AUTHOR : SIVA S K
########################################################################################

Approach!
=========
Instead of upload file, this application will translate whatever the user speaks into text form simultaneously.
Here by default (google) speech recognition with pyaudio to get the audio and to process the audio to text.

Steps to run the application.
=============================

1 . Create a virtual environment
--------------------------------
    i) run 'pip install virtualenv'
    ii) run 'virtualenv env' --> which creates an environment.
    iii) run 'source env/bin/activate' --> which activates the virtual environment.
    iv) to deactivate virtual environment, just run 'deactivate' to deactivate it.


2 . Install the required libraries such streamlit, speech recogonition.
-------------------------------------------------------------------------
    i) run 'pip install streamlit'
    ii) run 'pip install recognition'
    iii) run 'pip install PyAudio'
        * You may face difficulites while downloading this!, so you need to install 'flac' library to install 'pyaudio'.
        * So first make sure that you have installed flac, to install flac run following command
            'pip install flac'
        * Then , run 'pip install pyaudio' (or) 'pip install PyAudio'.


3 . Now copy and paste the 'main.py' file or clone the repository using 'git clone <repo-link>' command.
--

4 . Now to run the application, run the following command 'streamlit run <file-name>'. It will redirect to the http link where you can experience the application.
--
