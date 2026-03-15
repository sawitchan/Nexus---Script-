import telebot
import os
import requests
import subprocess
from telebot import types

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
bot = telebot.TeleBot(TOKEN)

IMG_MAIN = "https://c.termai.cc/i101/NoQ.jpg"
IMG_SECURITY = "https://c.termai.cc/i106/C8SCWk3.jpg"
IMG_INTEL = "https://c.termai.cc/i113/G3u.jpg"
IMG_EXPLOIT = "https://c.termai.cc/i197/UCCvsQM.jpg"
IMG_DEV = "https://c.termai.cc/i197/UCCvsQM.jpg"

def is_admin(m):
    return str(m.from_user.id) == ADMIN_ID

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = [
        types.InlineKeyboardButton("🌐 Network Tools", callback_data="cat_network"),
        types.InlineKeyboardButton("🛡️ Security Suite", callback_data="cat_security"),
        types.InlineKeyboardButton("🕵️ Intelligence", callback_data="cat_intel"),
        types.InlineKeyboardButton("🚀 Exploit Area", callback_data="cat_exploit"),
        types.InlineKeyboardButton("⚙️ System Hub", callback_data="cat_system"),
        types.InlineKeyboardButton("💎 Final Defense", callback_data="cat_defense")
    ]
    if is_admin(message):
        btns.append(types.InlineKeyboardButton("👨‍💻 Developer Hub", callback_data="cat_dev"))
    markup.add(*btns)
    
    caption = (
        f"Hallo, {message.from_user.first_name} 👋\n"
        f"Selamat Datang di **Nexus-Omni Dashboard**\n"
        f"───────────────────\n"
        f"🛠️ **Fitur**: 50 Modules Integrated\n"
        f"👥 **Total User**: Publik Access Ready\n"
        f"───────────────────\n"
        f"Gunakan Menu Button di bawah untuk mengakses 50 modul premium kami."
    )
    # Gunakan InputMediaPhoto untuk header awal
    bot.send_photo(message.chat.id, IMG_MAIN, caption=caption, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # KATEGORI: INTELLIGENCE (VISUAL CHANGE)
    if call.data == "cat_intel":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btns = [
            types.InlineKeyboardButton("📍 IP Tracker", callback_data="run_05"),
            types.InlineKeyboardButton("🔍 Deep Port Scan", callback_data="run_29"),
            types.InlineKeyboardButton("🌍 Global IP", callback_data="run_15"),
            types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main")
        ]
        markup.add(*btns)
        bot.edit_message_media(media=types.InputMediaPhoto(media=IMG_INTEL), 
                            chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_caption("🕵️ **INTELLIGENCE SUITE**\nPilih modul untuk eksekusi target:", 
                               call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "cat_exploit":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btns = [
            types.InlineKeyboardButton("🚀 SQL Injector", callback_data="run_16"),
            types.InlineKeyboardButton("💥 Brute Force", callback_data="run_18"),
            types.InlineKeyboardButton("😈 Backdoor Gen", callback_data="run_20"),
            types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main")
        ]
        markup.add(*btns)
        bot.edit_message_media(media=types.InputMediaPhoto(media=IMG_EXPLOIT), 
                            chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_caption("🚀 **EXPLOIT AREA**\nModul serangan tingkat lanjut:", 
                               call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "back_main":
        send_welcome(call.message)

    elif call.data == "cat_dev":
        if not is_admin(call): return
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("🗑️ Delete main.py", callback_data="dev_delete"),
                 types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main"))
        bot.edit_message_media(media=types.InputMediaPhoto(media=IMG_DEV), 
                            chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_caption("👨‍💻 **DEVELOPER HUB**\nKontrol Server Jarak Jauh:", 
                               call.message.chat.id, call.message.message_id, reply_markup=markup)

print(">> NEXUS-OMNI VISUAL ")
bot.infinity_polling()
