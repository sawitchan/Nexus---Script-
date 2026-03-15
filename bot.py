import telebot
import os
import requests
import subprocess

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
bot = telebot.TeleBot(TOKEN)

def is_admin(message):
    return str(message.chat.id) == ADMIN_ID

@bot.message_code_handler(func=lambda m: True)
def handle_code(message):
    if not is_admin(message): return
    # Fitur Ganti Kode Otomatis via Chat
    with open("main.py", "w") as f:
        f.write(message.text)
    bot.reply_to(message, "✅ **CODE UPDATED!**\nSistem Reality telah diperbarui oleh Tuan Markus.")

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    if not is_admin(message):
        bot.reply_to(message, "❌ Akses Ditolak. Anda bukan Tuan Markus.")
        return
    
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('🛡️ Scan Target (Reality)')
    item2 = telebot.types.KeyboardButton('🛰️ Ghost Proxy Status')
    item3 = telebot.types.KeyboardButton('⚙️ System Check')
    item4 = telebot.types.KeyboardButton('🗑️ Clear Logs')
    markup.add(item1, item2, item3, item4)
    
    welcome_msg = (
        "╔════════════════════════╗\n"
        "      NEXUS-OMNI CONTROL   \n"
        "╚════════════════════════╝\n"
        "Selamat datang, Tuan Markus.\n"
        "Sistem siap mengendalikan Termux."
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == '🛡️ Scan Target (Reality)')
def ask_target(message):
    if not is_admin(message): return
    msg = bot.send_message(message.chat.id, "🎯 **Masukkan IP/Domain Target:**")
    bot.register_next_step_handler(msg, process_scan)

def process_scan(message):
    target = message.text
    bot.send_message(message.chat.id, f"⚡ **Executing Handshake via No-IDN...**")
    try:
        res = requests.get(f"http://ip-api.com/json/{target}").json()
        report = (
            f"📊 **SCAN REPORT**\n"
            f"────────────────────\n"
            f"📍 Target  : `{target}`\n"
            f"🌍 Negara  : {res.get('country')}\n"
            f"🏢 ISP     : {res.get('isp')}\n"
            f"🏙️ Kota    : {res.get('city')}\n"
            f"🛡️ Security: KTP ACTIVE\n"
            f"────────────────────"
        )
        bot.send_message(message.chat.id, report, parse_mode="Markdown")
    except:
        bot.send_message(message.chat.id, "❌ Gagal menarik data Reality.")

print(">> BOT NEXUS-OMNI TELAH AKTIF DI TELEGRAM TUAN MARKUS!")
bot.infinity_polling()
