#Generate Audio captcher in python
import random
from captcha.audio import AudioCaptcha
from playsound import playsound


def geneate_random_captch(length=6):
    char = '1234567890'
    captcha_text = ''.join(random.choices(char, k=length))
    return captcha_text


audio = AudioCaptcha()
captcha_text = geneate_random_captch()
print('Generate Captcha Text: ', captcha_text)
audio_captcha = audio.generate(captcha_text)
audio.write(captcha_text, 'Audio_Captcha.wav')
print('Audio Captcha generated: Audio_Captcha.wav')

# for playing note.wav file
print('playing sound using  playsound')
playsound('./Audio_Captcha.wav')

