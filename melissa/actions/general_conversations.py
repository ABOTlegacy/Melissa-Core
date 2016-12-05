import random

# Melissa
from melissa import profile
from melissa.tts import tts

WORDS = {'who_are_you': {'groups': [['who', 'are', 'you']]},
         'toss_coin': {'groups': [['heads', 'tails'],
                                  ['toss', 'coin'], ['flip', 'coin']]},
         'how_am_i': {'groups': [['how', 'i', 'look'], ['how', 'am', 'i']]},
         'tell_joke': {'groups': [['tell', 'joke']]},
         'who_am_i': {'groups': [['who', 'am', 'i']]},
         'where_born': {'groups': [['where', 'born']]},
         'how_are_you': {'groups': [['how', 'are', 'you']]},
         'are_you_up': {'groups': [['you', 'up']]},
         'love_you': {'groups': [['love', 'you']]},
         'marry_me': {'groups': [['marry', 'me']]},
         'undefined': {'groups': []}}


def who_are_you(text, bot, chat_id):
    va_name = profile.data['va_name']
    messages = ['I am ' + va_name + ', your lovely personal assistant.',
                va_name + ', didnt I tell you before?',
                'You ask that so many times! I am ' + va_name]
    tts(random.choice(messages), bot, chat_id)


def toss_coin(text, bot, chat_id):
    outcomes = ['heads', 'tails']
    tts('I just flipped a coin. It shows ' + random.choice(outcomes), bot, chat_id)


def how_am_i(text, bot, chat_id):
    replies = [
        'You are goddamn handsome!',
        'My knees go weak when I see you.',
        'You are sexy!',
        'You look like the kindest person that I have met.'
    ]
    tts(random.choice(replies), bot, chat_id)


def tell_joke(text, bot, chat_id):
    jokes = [
        'What happens to a frogs car when it breaks down? It gets toad away.',
        'Why was six scared of seven? Because seven ate nine.',
        'Why are mountains so funny? Because they are hill areas.',
        'Have you ever tried to eat a clock?'
        'I hear it is very time consuming.',
        'What happened when the wheel was invented? A revolution.',
        'What do you call a fake noodle? An impasta!',
        'Did you hear about that new broom? It is sweeping the nation!',
        'What is heavy forward but not backward? Ton.',
        'No, I always forget the punch line.'
    ]
    tts(random.choice(jokes), bot, chat_id)


def who_am_i(text, bot, chat_id):
    name = profile.data['name']
    tts('You are ' + name + ', a brilliant person. I love you!', bot, chat_id)


def where_born(text, bot, chat_id):
    tts('I was created by a magician named Tanay, in India, '
        'the magical land of himalayas.', bot, chat_id)


def how_are_you(text, bot, chat_id):
    tts('I am fine, thank you.', bot, chat_id)


def are_you_up(text, bot, chat_id):
    tts('For you sir, always.', bot, chat_id)


def love_you(text, bot, chat_id):
    replies = [
               'I love you too.',
               'You are looking for love in the wrong place.'
              ]
    tts(random.choice(replies), bot, chat_id)


def marry_me(text, bot, chat_id):
    tts('I have been receiving a lot of marriage proposals recently.', bot, chat_id)


def undefined(text, bot, chat_id):
    tts('I dont know what that means!', bot, chat_id)
