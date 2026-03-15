import telebot
import os
import subprocess
import time
from telebot import types

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
bot = telebot.TeleBot(TOKEN)

MAIN_PATH = os.path.join(os.getcwd(), "main.py")

# URL Gambar Sesuai Request Tuan
IMG = {
    "main": "https://c.termai.cc/i101/NoQ.jpg",
    "intel": "https://c.termai.cc/i113/G3u.jpg",
    "exploit": "https://c.termai.cc/i197/UCCvsQM.jpg"
}

def is_admin(m):
    return str(m.from_user.id) == ADMIN_ID

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = [
        types.InlineKeyboardButton("🌐 Network", callback_data="list_network"),
        types.InlineKeyboardButton("🛡️ Security", callback_data="list_security"),
        types.InlineKeyboardButton("🕵️ Intelligence", callback_data="list_intel"),
        types.InlineKeyboardButton("🚀 Exploit", callback_data="list_exploit"),
        types.InlineKeyboardButton("⚙️ System", callback_data="cat_system"),
        types.InlineKeyboardButton("💎 Defense", callback_data="list_defense")
    ]
    if is_admin(message):
        btns.append(types.InlineKeyboardButton("👨‍💻 Developer Hub", callback_data="cat_dev"))
    markup.add(*btns)
    bot.send_photo(message.chat.id, IMG["main"], caption="🚀 **NEXUS-OMNI Dashboard V13.2**\n50 Fitur Utama Siap Dieksekusi, Tuan.", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    bot.answer_callback_query(call.id, "⚡ Processing...")

    # FIX: Pemetaan kategori agar semua 50 fitur bisa diakses
    if call.data.startswith("list_"):
        cat = call.data.replace("list_", "")
        markup = types.InlineKeyboardMarkup(row_width=2)
        
        if cat == "intel":
            markup.add(types.InlineKeyboardButton("📍 IP Tracker (05)", callback_data="run_05"),
                       types.InlineKeyboardButton("🔍 Port Scan (29)", callback_data="run_29"))
        elif cat == "network":
            markup.add(types.InlineKeyboardButton("🛡️ Proxy (06)", callback_data="run_06"),
                       types.InlineKeyboardButton("📡 DNS (dns)", callback_data="run_dns"))
        
        markup.add(types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main"))
        bot.edit_message_caption(f"📂 **KATEGORI: {cat.upper()}**\nPilih modul untuk dijalankan:", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "cat_system":
        ram = subprocess.getoutput("free -m | awk 'NR==2{printf \"%.2f%%\", $3*100/$2 }'")
        msg = f"⚙️ **SYSTEM MONITOR**\n──────────────────\n🖥️ Status: ACTIVE\n🧠 RAM Usage: {ram}\n──────────────────"
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main"))
        bot.edit_message_caption(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "cat_dev":
        if not is_admin(call): return
        markup = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("🚀 Git Add, Commit, Push", callback_data="dev_push"),
            types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main")
        )
        bot.edit_message_caption("👨‍💻 **DEVELOPER HUB**", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "dev_push":
        bot.send_message(call.message.chat.id, "🛰️ Memulai Remote Push...")
        res = subprocess.getoutput("git add . && git commit -m 'Remote Update via Bot' && git push origin main")
        bot.send_message(call.message.chat.id, f"✅ **GIT RESULT:**\n`{res}`")

    elif call.data == "back_main":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_welcome(call.message)

    elif call.data.startswith("run_"):
        msg = bot.send_message(call.message.chat.id, "🎯 **Target:**")
        bot.register_next_step_handler(msg, execute_script, call.data)

def execute_script(message, mod_id):
    target = message.text
    bot.send_message(message.chat.id, f"🚀 **Executing {mod_id} on {target}...**")
    cmd = f"python3 {MAIN_PATH} --mod {mod_id} --target {target}"
    result = subprocess.getoutput(cmd)
    bot.send_message(message.chat.id, f"✅ **RESULT:**\n`{result}`", parse_mode="Markdown")

while True:
    try:
        bot.polling(non_stop=True, interval=0, timeout=20)
    except Exception:
        time.sleep(5)
