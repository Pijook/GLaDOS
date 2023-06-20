import speech_recognition
from playsound import playsound

recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()

glados_active = False

voice_lines_file = "voice_lines/"

sounds = {
    "welcome": "welcome.wav",
    "opening_chrome": "opening_chrome",
    "no_text": "no_text.wav",
    "bye": "bye_bye.wav",
    "ready_for_input": "ready_for_input.wav"
}

print("GLaDOS is working...")


def handle_speech(to_handle):
    global glados_active

    if to_handle == "GLaDoS":
        activate_glados()
    else:
        if not glados_active:
            return None

        if to_handle == "unknown":
            deactivate_glados()
        else:
            # Do thing
            glados_active = False


def activate_glados():
    global glados_active

    glados_active = True
    secure_play_sound("ready_for_input")


def deactivate_glados():
    global glados_active
    glados_active = False
    secure_play_sound("bye")


def secure_play_sound(sound_id):
    global sounds

    path = voice_lines_file + sounds.get(sound_id, "no_text")
    playsound(path)


secure_play_sound("welcome")

while True:
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
        sentence = ""
        try:
            sentence = recognizer.recognize_google(audio, language="pl-PL")
        except speech_recognition.UnknownValueError:
            sentence = "unknown"

        handle_speech(sentence)
