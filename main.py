from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN
from function import echo_start, echo_text, echo_buyurtma,echo_settings,echo_language,echo_language_uzbek,echo_language_ru,echo_language_eng,echo_phone

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# Commandhandler
dispatcher.add_handler(CommandHandler("start", echo_start))

# MessageHandler – TARTIB muhim!
dispatcher.add_handler(MessageHandler(Filters.text("📦 Buyurtmalarim"), echo_buyurtma))
dispatcher.add_handler(MessageHandler(Filters.text("⚙️ Sozlamalar"), echo_settings))
dispatcher.add_handler(MessageHandler(Filters.text("🌐 Tilni o'zgartirish"), echo_language))
dispatcher.add_handler(MessageHandler(Filters.text("O'zbekcha"), echo_language_uzbek))
dispatcher.add_handler(MessageHandler(Filters.text("Русский"), echo_language_ru))
dispatcher.add_handler(MessageHandler(Filters.text("English"), echo_language_eng))
dispatcher.add_handler(MessageHandler(Filters.text("📞 Telefon raqamingizni o'zgartiring"),echo_phone))
# dispatcher.add_handler(MessageHandler(Filters.text("Mening raqamim"),echo_contact))
dispatcher.add_handler(MessageHandler(Filters.text, echo_text))

updater.start_polling()
updater.idle()
