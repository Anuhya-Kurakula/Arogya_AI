from gtts import gTTS
import os


def text_to_speech(text):

    output_file = "response.mp3"

    tts = gTTS(text=text, lang="en")

    tts.save(output_file)

    return output_file