import subprocess

# Melissa
from melissa.tts import tts

WORDS = {'very_dark': {'groups': ['dark']},
         'feeling_angry': {'groups': [['feeling', 'angry']]},
         'feeling_creative': {'groups': [['feeling', 'creative']]},
         'feeling_lazy': {'groups': [['feeling', 'lazy']]},
         'turn_off': {'groups': [['lights', 'off']]}}


def very_dark(text, bot, chat_id):
    subprocess.call(['blink1-tool', '--white'])
    tts('Better now?', bot, chat_id)


def feeling_angry(text, bot, chat_id):
    subprocess.call(['blink1-tool', '--cyan'])
    tts('Calm down dear!', bot, chat_id)


def feeling_creative(text, bot, chat_id):
    subprocess.call(['blink1-tool', '--magenta'])
    tts('So good to hear that!', bot, chat_id)


def feeling_lazy(text, bot, chat_id):
    subprocess.call(['blink1-tool', '--yellow'])
    tts('Rise and shine dear!', bot, chat_id)


def turn_off(text, bot, chat_id):
    subprocess.call(['blink1-tool', '--off'], bot, chat_id)
