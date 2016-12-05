import sys
import subprocess
from melissa.profile_loader import load_profile
from melissa.tts import tts
#from melissa.stt import stt
from melissa.brain import query
import telepot
import telepot.helper
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.delegate import (per_chat_id, create_open, pave_event_space, include_callback_query_chat_id)

# Melissa Profile
data = load_profile(True)

# thread-safe dict
propose_records = telepot.helper.SafeDict()  

class Lover(telepot.helper.ChatHandler):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
                   InlineKeyboardButton(text='Yes', callback_data='yes'),
                   InlineKeyboardButton(text='um ...', callback_data='no'),
               ]])

    def __init__(self, *args, **kwargs):
        super(Lover, self).__init__(*args, **kwargs)

        # Retrieve from database
        global propose_records
        if self.id in propose_records:
            self._count, self._edit_msg_ident = propose_records[self.id]
            self._editor = telepot.helper.Editor(self.bot, self._edit_msg_ident) if self._edit_msg_ident else None
        else:
            self._count = 0
            self._edit_msg_ident = None
            self._editor = None

    def _propose(self):
        self._count += 1
        sent = self.sender.sendMessage('%d. Would you marry me?' % self._count, reply_markup=self.keyboard)
        self._editor = telepot.helper.Editor(self.bot, sent)
        self._edit_msg_ident = telepot.message_identifier(sent)

    def _cancel_last(self):
        if self._editor:
            self._editor.editMessageReplyMarkup(reply_markup=None)
            self._editor = None
            self._edit_msg_ident = None

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if (content_type == 'text') and (str(chat_id) in allowed_chat_ids):
            command = msg['text']
            print(command)

            ### GENERIC METHODS ###
            if command == '/roll':
                bot.sendMessage(chat_id, random.randint(1,6))
            elif command == '/start':
                bot.sendMessage(chat_id, 'hola!')
            elif command == '/menu':
                replymarkup = {
                    "keyboard": [[{"text":"/alarm"}], [{"text":"/favstates"}], [{"text":"/roll"}]],
                    "resize_keyboard": True,
                    "one_time_keyboard": True
                }
                bot.sendMessage(chat_id, 'Please choose an option...',reply_markup=replymarkup)

            ### CAMERA COMMANDS ###
            elif command == '/missile':
                replymarkup = {
                    "keyboard": [[{"text":"/left"}, {"text":"/right"}], [{"text":"/up"}, {"text":"/down"}], [{"text":"/shoot"}]],
                    "resize_keyboard": True,
                    "one_time_keyboard": False
                }
                bot.sendMessage(chat_id, 'Please choose an option...',reply_markup=replymarkup)
            elif command == '/left':
                missile.run_command(command, 400)
            elif command == '/right':
                missile.run_command(command, 400)
            elif command == '/up':
                missile.run_command(command, 200)
            elif command == '/down':
                missile.run_command(command, 200)
            elif command == '/shoot':
                missile.run_command(command, 1)

            ### ACTION COMMANDS ###
            elif command == '/actions':
                replymarkup = {
                    "keyboard": [[{"text":"/sleep"}], [{"text":"/home"}], [{"text":"/grocery_list"}]],
                    "resize_keyboard": True,
                     "one_time_keyboard": False
                }
                bot.sendMessage(chat_id, 'Please choose an option...',reply_markup=replymarkup)
            elif command == '/sleep':
                service_call('media_player','turn_off',{'entity_id': 'media_player.sony_bravia_tv'})
                service_call('light','turn_off',{'entity_id': 'light.family_room_light'})
                bot.sendMessage(chat_id, 'Goodnight')
            elif command == '/grocery_list':
                bot.sendMessage(chat_id, todoist.DisplayGroceryList())



        ### ELSE NOT TEXT ###
        elif (content_type == 'location') and (str(chat_id) in allowed_chat_ids):
            latitude = msg['location']['latitude']
            longitude = msg['location']['longitude']
            #bot.sendMessage(chat_id, 'LATITUDE: ' + repr(latitude) + '\nLONGITUDE: ' + repr(longitude))
            servicedata = {'dev_id': 'abotlegacywindowsphone', 'gps': [latitude, longitude]}
            service_call('device_tracker','see',servicedata)
            bot.sendMessage(chat_id, 'You are checked in.')
        elif (content_type == 'audio') and (str(chat_id) in allowed_chat_ids):
            mimetype = msg['audio']['mime_type']
            print(mimetype)
            bot.sendMessage(chat_id, mimetype)
        else:
            query(text)




    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

        if query_data == 'yes':
            self._cancel_last()
            self.sender.sendMessage('Thank you!')
            self.close()
        else:
            self.bot.answerCallbackQuery(query_id, text='Ok. But I am going to keep asking.')
            self._cancel_last()
            self._propose()

    def on__idle(self, event):
        self.sender.sendMessage('I know you may need a little time. I will always be here for you.')
        self.close()

    def on_close(self, ex):
        # Save to database
        global propose_records
        propose_records[self.id] = (self._count, self._edit_msg_ident)

bot = telepot.DelegatorBot(bot_token, [
    include_callback_query_chat_id(
        pave_event_space())(
            per_chat_id(types=['private']), create_open, Lover, timeout=10),
])
bot.message_loop(run_forever='Listening ...')
bot.sendMessage(chat_id, 'Welcome ' + data['name'] + ', how can I help you?')