from keep_alive import keep_alive
keep_alive()

import telebot
from telebot import types

# Tavo boto tokenas
TOKEN = "8075766947:AAHzZ5RCdLlzBbozvE2HwsTn_MHoXpkIeZY"
bot = telebot.TeleBot(TOKEN)

# Tavo Telegram user ID, kad gautum žinutes
ADMIN_ID = 7497055967

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Parašyk žinutę ir aš ją anonimiškai persiųsiu.")

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice'])
def forward_message(message):
    if message.text:
        bot.send_message(ADMIN_ID, f"Anoniminė žinutė:\n{message.text}")
    elif message.photo:
        bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=message.caption)
    elif message.video:
        bot.send_video(ADMIN_ID, message.video.file_id, caption=message.caption)
    elif message.document:
        bot.send_document(ADMIN_ID, message.document.file_id, caption=message.caption)
    elif message.audio:
        bot.send_audio(ADMIN_ID, message.audio.file_id, caption=message.caption)
    elif message.voice:
        bot.send_voice(ADMIN_ID, message.voice.file_id)

    bot.send_message(message.chat.id, "Žinutė anonimiškai išsiųsta!")

bot.infinity_polling()
