import main
import config

import speech_recognition as sr
from pydub import AudioSegment

import urllib
import io

r = sr.Recognizer()


async def voice_rec(audio):
    with sr.AudioFile(audio) as source:
        audio = r.record(source)  # read the entire audio file

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        # print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language="ru"))
        return r.recognize_google(audio, language="ru", show_all=False)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "Could not request results from Google Speech Recognition service; {0}".format(e)


async def text_from_voice(message):
    file_info = await main.bot.get_file(message.voice.file_id)
    fi = file_info.file_path
    req = urllib.request.Request(f'https://api.telegram.org/file/bot{config.TOKEN}/{fi}')
    with urllib.request.urlopen(req) as response:
        voice_ogg = response.read()

    audio = AudioSegment.from_ogg(io.BytesIO(voice_ogg))
    audio_buf = io.BytesIO()
    audio_buf = audio.export(audio_buf, format="wav")
    return await voice_rec(audio_buf)
