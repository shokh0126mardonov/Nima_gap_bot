from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import CallbackContext

# /start komandasi uchun
def echo_start(update: Update, context: CallbackContext):
    name = update.message.from_user.full_name
    greeting_text = f"Assalomu alaykum {name}!"

    bot = update.message.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text=greeting_text,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton("🎁 Buyurtma berish", web_app=WebAppInfo(
                        url="https://uzum.uz/uz/category/smartfonlar-va-telefonlar-10044?srsltid=AfmBOopFqCWILBgAeWwGrgRndz5Xxub_n0MLQIVeGwMiqnDRCiXvExj_"
                    ))
                ],
                [
                    KeyboardButton("📦 Buyurtmalarim"),
                    KeyboardButton("⚙️ Sozlamalar")
                ],
                [
                    KeyboardButton("ℹ️ Biz haqimizda"),
                    KeyboardButton("✍️ Fikr qoldirish")
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

# 📦 Buyurtmalarim tugmasi bosilganda
def echo_buyurtma(update: Update, context: CallbackContext):
    update.message.reply_text("📦 Sizda hali birorta ham buyurtma yo‘q.")

# Boshqa har qanday matnga javob
def echo_text(update: Update, context: CallbackContext):
    update.message.reply_text("Xabaringiz uchun tashakkur, imkon qadar tezroq siz bilan bog'lanamiz.")

def echo_settings(update: Update, context: CallbackContext):
    bot = update.message.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "⚙️ Sozlamalar",
        reply_markup = ReplyKeyboardMarkup(
            [
                [KeyboardButton("🌐 Tilni o'zgartirish")],
                [KeyboardButton("📞 Telefon raqamingizni o'zgartiring")],
                [KeyboardButton("⬅️ Orqaga")]
            ],
            resize_keyboard = True,
            one_time_keyboard = True
        )
    )

def echo_language(update: Update, context: CallbackContext):
    bot = update.message.bot
    id = update.effective_user.id
    
    bot.send_message(
        chat_id = id,
        text = "Tilni tanlang",
        reply_markup = ReplyKeyboardMarkup(
            keyboard = [
                [
                KeyboardButton(text = "O'zbekcha"),KeyboardButton("Русский")
                ],
                [
                    KeyboardButton("English")
                ],
                [
                    KeyboardButton("⬅️ Orqaga")
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

def echo_language_uzbek(update: Update, context: CallbackContext):
  
    bot = update.message.bot
    user = update.effective_user

    bot.send_message(
        chat_id = user.id,
        text = "🏠 Bosh menyu",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton("🎁 Buyurtma berish", web_app=WebAppInfo(
                        url="https://uzum.uz/uz/category/smartfonlar-va-telefonlar-10044?srsltid=AfmBOopFqCWILBgAeWwGrgRndz5Xxub_n0MLQIVeGwMiqnDRCiXvExj_"
                    ))
                ],
                [
                    KeyboardButton("📦 Buyurtmalarim"),
                    KeyboardButton("⚙️ Sozlamalar")
                ],
                [
                    KeyboardButton("ℹ️ Biz haqimizda"),
                    KeyboardButton("✍️ Fikr qoldirish")
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def echo_language_ru(update: Update, context: CallbackContext):
      
    bot = update.message.bot
    user = update.effective_user

    bot.send_message(
        chat_id = user.id,
        text = "🏠 Главное меню",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton("🎁 Buyurtma berish", web_app=WebAppInfo(
                        url="https://uzum.uz/uz/category/smartfonlar-va-telefonlar-10044?srsltid=AfmBOopFqCWILBgAeWwGrgRndz5Xxub_n0MLQIVeGwMiqnDRCiXvExj_"
                    ))
                ],
                [
                    KeyboardButton("📦 Buyurtmalarim"),
                    KeyboardButton("⚙️ Sozlamalar")
                ],
                [
                    KeyboardButton("ℹ️ Biz haqimizda"),
                    KeyboardButton("✍️ Fikr qoldirish")
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def echo_language_eng(update: Update, context: CallbackContext):
      
    bot = update.message.bot
    user = update.effective_user

    bot.send_message(
        chat_id = user.id,
        text = "🏠 Main menu",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton("🎁 Buyurtma berish", web_app=WebAppInfo(
                        url="https://uzum.uz/uz/category/smartfonlar-va-telefonlar-10044?srsltid=AfmBOopFqCWILBgAeWwGrgRndz5Xxub_n0MLQIVeGwMiqnDRCiXvExj_"
                    ))
                ],
                [
                    KeyboardButton("📦 Buyurtmalarim"),
                    KeyboardButton("⚙️ Sozlamalar")
                ],
                [
                    KeyboardButton("ℹ️ Biz haqimizda"),
                    KeyboardButton("✍️ Fikr qoldirish")
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def echo_phone(update: Update, context: CallbackContext):
    bot = update.message.bot
    id = update.effective_user.id
    
    bot.send_message(
        chat_id = id,
        text = "Iltimos, telefon raqamingizni yuboring",
        reply_markup  = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton("Mening raqamim")
                ],
                [
                    KeyboardButton("⬅️ Orqaga")
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )




# def echo_contact(update: Update, context: CallbackContext):
#     tugma = ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton("📱 Mening raqamim", request_contact=True)]
#         ],
#         resize_keyboard=True,
#         one_time_keyboard=True
#     )

#     # HECH QANDAY MATN YO‘Q — faqat tugma yuboriladi
#     update.message.reply_text(
#         text="📱",  # yoki oddiy belgicha; butunlay bo‘sh qoldirish ham mumkin emas
#         reply_markup=tugma
#     )
