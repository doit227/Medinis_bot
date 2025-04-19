import telebot

# Įrašyk savo tikrą bot token čia
TOKEN = "8075766947:AAHzZ5RCdLlzBbozvE2HwsTn_MHoXpkIeZY"

bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()

print("Webhook sėkmingai ištrintas.")
