import streamlit as st
import speech_recognition as sr


def main():
    st.title("Track Your Speech!")
    if st.button("Start"):
        transcribe_audio()


def transcribe_audio():
    r = sr.Recognizer()
    lang_code = "en-US"

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        st.write("Listening...")

        while True:
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio, language=lang_code)
                st.write("Transcription:", text)
            except sr.UnknownValueError:
                st.write("Couldn't get the words!")
            except sr.RequestError as e:
                st.write("Couldn't process the result; {0}".format(e))


if __name__ == "__main__":
    main()
