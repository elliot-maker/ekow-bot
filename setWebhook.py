import telebot

bot = telebot.TeleBot('7081209694:AAG27dZPntfq19kXIUEWytkwubPBqSVGPC0')

WEBHOOK_URL = 'https://be28-102-176-75-190.ngrok-free.app/7081209694:AAG27dZPntfq19kXIUEWytkwubPBqSVGPC0'

bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

print(f"Webhook set to {WEBHOOK_URL}")
