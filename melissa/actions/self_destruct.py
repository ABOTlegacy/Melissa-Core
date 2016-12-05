import subprocess

# Melissa
from melissa.tts import tts

WORDS = {'self_destruct': {'groups': [['self', 'destruct']]}}


def self_destruct(text, bot, chat_id):
    tts('Self destruction mode engaged, over and out.', bot, chat_id)
    subprocess.call(['sudo', 'rm', '-r', '../Melissa-Core'])
    quit()
