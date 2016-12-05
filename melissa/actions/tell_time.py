from datetime import datetime

# Melissa
from melissa.tts import tts

WORDS = {
  'what_is_time': {'groups': ['time']},
  'what_is_date': {'groups': ['date']},
  'what_is_day': {'groups': ['day']}
}


def what_is_time(text, bot, chat_id):
    tts("The time is " + datetime.strftime(datetime.now(), '%H:%M:%S'), bot, chat_id)


def what_is_date(text, bot, chat_id):
    tts("The date is " + datetime.strftime(datetime.now(), '%m/%d/%Y'), bot, chat_id)


def what_is_day(text, bot, chat_id):
    tts("The day is " + datetime.strftime(datetime.now(), '%A'), bot, chat_id)
