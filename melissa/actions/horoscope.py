from horoscope_generator import HoroscopeGenerator

# Melissa
from melissa.tts import tts

WORDS = {
    'tell_horoscope': {
        'groups': [
            ['tell', 'future'],
            ['say', 'wise'],
            ['how', 'day'],
            ['hows', 'day'],
            ['how', 'today'],
            ['hows', 'today'],
            'horoscope'
        ]
    }
}


def tell_horoscope(text, bot, chat_id):
    tts(HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence()), bot, chat_id)
