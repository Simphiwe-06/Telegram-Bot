#!/usr/bin/env python3

import spacy
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

nlp = spacy.load("en_core_web_md")

def start(update: Update, context: CallbackContext) -> None:
  update.message.reply_text('Hi! I am your Healthcare Assistant. How can I help you today?')

def handle_message(update Update, context: CallbackContext) -> None:
  user_message = update.message.text
  doc = nlp(user_message)
  response = "I'm here to help with your healthcare queries."
  update.message.reply_text(response)

def main() -> None:
  updater = Updater("7096953448:AAH0-F-oYRD2YsI4W8TECha7FFi5frFDZ2o")
  dispatcher = updater.dispatcher
  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
  updater.start_polling()
  updater.idle()

if __name__ == "__main__":
  main()

