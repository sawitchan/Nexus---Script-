import telebot
import os
import subprocess
import psutil
import time
from telebot import types

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
bot = telebot.TeleBot(TOKEN)

MAIN_PATH = os.path.join(os.getcwd(), "main.py")

IMG = {
    "main": "https://c.termai.cc/i101/NoQ.jpg",
    "intel": "https://c.termai.cc/i113/G3u.jpg",
    "dev": "https://c.termai.cc/i106/C8SCWk3.jpg"
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
        types.InlineKeyboardButton("👨‍💻 Dev Hub", callback_data="cat_dev")
    ]
    markup.add(*btns)
    caption = "🚀 **NEXUS-OMNI DASHBOARD V15.0**\nStatus: Stealth Mode Active\nUser: Tuan"
    bot.send_photo(message.chat.id, IMG["main"], caption=caption, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "cat_system":
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        msg = f"⚙️ **SYSTEM MONITOR**\nCPU Usage: {cpu}%\nRAM Usage: {ram}%\nLog Status: Wiped Clean"
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main"))
        bot.edit_message_caption(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "cat_dev":
        if not is_admin(call): return
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🔄 AUTO-UPDATE ENGINE", callback_data="dev_update"),
                   types.InlineKeyboardButton("🚀 GIT PUSH (REMOTE)", callback_data="dev_push"),
                   types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main"))
        bot.edit_message_caption("👨‍💻 **DEVELOPER HUB**\nControl Termux dari jarak jauh.", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "dev_update":
        bot.answer_callback_query(call.id, "🔄 Updating...")
        res = subprocess.getoutput("git pull origin main && pm2 restart Nexus-Bot")
        bot.send_message(call.message.chat.id, f"✅ **UPDATE SUCCESS:**\n`{res}`")

    elif call.data == "dev_push":
        bot.answer_callback_query(call.id, "🛰️ Pushing...")
        res = subprocess.getoutput("git add . && git commit -m 'Remote Sync' && git push origin main")
        bot.send_message(call.message.chat.id, f"✅ **GIT PUSH:**\n`{res}`")

    elif call.data == "back_main":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_welcome(call.message)

    elif call.data.startswith("cat_"):
        # Logika kategori fitur lainnya (Network, Intel, dll)
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔍 Run Modul", callback_data="run_mod"),
                                                  types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main"))
        bot.edit_message_caption(f"📂 Kategori {call.data.split('_')[1].upper()} Ready.", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "run_mod":
        msg = bot.send_message(call.message.chat.id, "🎯 **Masukkan Nomor Modul & Target:**\n(Contoh: 29 google.com)")
        bot.register_next_step_handler(msg, execute_remote)

def execute_remote(message):
    try:
        data = message.text.split()
        mod_id = data[0].zfill(2)
        target = data[1]
        bot.send_message(message.chat.id, f"⚡ **Executing Modul {mod_id} on {target}...**")
        cmd = f"python3 {MAIN_PATH} --mod {mod_id} --target {target}"
        result = subprocess.getoutput(cmd)
        bot.send_message(message.chat.id, result, parse_mode="Markdown")
    except:
        bot.send_message(message.chat.id, "❌ Format salah. Gunakan: `[Nomor] [Target]`")

while True:
    try:
        bot.polling(non_stop=True, interval=0, timeout=20)
    except:
        time.sleep(5)
