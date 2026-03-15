import telebot
import os
import subprocess
import psutil
from telebot import types

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
bot = telebot.TeleBot(TOKEN)

MAIN_PATH = os.path.join(os.getcwd(), "main.py")

IMG = {
    "main": "https://pomf2.lain.la/f/v0m3z3z.jpg",
    "sec": "https://pomf2.lain.la/f/y2m5y6b.jpg",
    "intel": "https://pomf2.lain.la/f/p7m8p9z.jpg",
    "exploit": "https://pomf2.lain.la/f/k1m2k3y.jpg"
}

def is_admin(m):
    return str(m.from_user.id) == ADMIN_ID

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = [
        types.InlineKeyboardButton("🌐 Network", callback_data="cat_network"),
        types.InlineKeyboardButton("🛡️ Security", callback_data="cat_security"),
        types.InlineKeyboardButton("🕵️ Intelligence", callback_data="cat_intel"),
        types.InlineKeyboardButton("🚀 Exploit", callback_data="cat_exploit"),
        types.InlineKeyboardButton("⚙️ System", callback_data="cat_system"),
        types.InlineKeyboardButton("💎 Defense", callback_data="cat_defense")
    ]
    if is_admin(message):
        btns.append(types.InlineKeyboardButton("👨‍💻 Developer Hub", callback_data="cat_dev"))
    markup.add(*btns)
    
    caption = "🚀 **NEXUS-OMNI Dashboard V13.0**\n50 fitur siap eksekusi , Tuan."
    bot.send_photo(message.chat.id, IMG["main"], caption=caption, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    bot.answer_callback_query(call.id, "⚡ Processing...")

    if call.data == "cat_network":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("🛡️ Proxy Scraper", callback_data="run_06"),
                   types.InlineKeyboardButton("📡 DNS Check", callback_data="run_dns"),
                   types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main"))
        bot.edit_message_caption("🌐 **NETWORK TOOLS**", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "cat_security":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("🔐 Web Shield", callback_data="run_shield"),
                   types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main"))
        bot.edit_message_caption("🛡️ **SECURITY SUITE**", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "cat_intel":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("🔍 Port Scanner", callback_data="run_29"),
                   types.InlineKeyboardButton("📍 IP Tracker", callback_data="run_05"),
                   types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main"))
        bot.edit_message_media(media=types.InputMediaPhoto(media=IMG["intel"], caption="🕵️ **INTEL SUITE**"),
                               chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "cat_dev":
        if not is_admin(call): return
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("📝 Update main.py (Chat)", callback_data="dev_update"),
                   types.InlineKeyboardButton("🚀 Git Add, Commit, Push", callback_data="dev_push"),
                   types.InlineKeyboardButton("🗑️ Hapus main.py", callback_data="dev_del"),
                   types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main"))
        bot.edit_message_caption("👨‍💻 **DEVELOPER HUB**\nRemote Termux Tanpa Buka Aplikasi.", 
                                 call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "dev_push":
        res = subprocess.getoutput("git add . && git commit -m 'Remote Update via Telegram' && git push origin main")
        bot.send_message(call.message.chat.id, f"✅ **GIT SUCCESS:**\n`{res}`")

    elif call.data == "back_main":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_welcome(call.message)

    elif call.data.startswith("run_"):
        msg = bot.send_message(call.message.chat.id, "🎯 **Target:**")
        bot.register_next_step_handler(msg, execute_script, call.data)

def execute_script(message, mod_id):
    target = message.text
    bot.send_message(message.chat.id, f"🚀 **Running {mod_id} on {target}...**")
    cmd = f"python3 {MAIN_PATH} --mod {mod_id} --target {target}"
    result = subprocess.getoutput(cmd)
    bot.send_message(message.chat.id, f"✅ **RESULT:**\n`{result}`", parse_mode="Markdown")

bot.infinity_polling()
