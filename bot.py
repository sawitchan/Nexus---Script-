import telebot
import os
import subprocess
import psutil
from telebot import types

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
bot = telebot.TeleBot(TOKEN)

submit_count = 0 

IMG = {
    "main": "https://c.termai.cc/i101/NoQ.jpg",
    "intel": "https://c.termai.cc/i113/G3u.jpg",
    "exploit": "https://c.termai.cc/i197/UCCvsQM.jpg",
    "dev": "https://c.termai.cc/i167/dWi8H3u.jpg"
}

def is_admin(m):
    return str(m.from_user.id) == ADMIN_ID

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = [
        types.InlineKeyboardButton("🌐 Network Tools", callback_data="cat_network"),
        types.InlineKeyboardButton("🛡️ Security Suite", callback_data="cat_sec"),
        types.InlineKeyboardButton("🕵️ Intelligence", callback_data="cat_intel"),
        types.InlineKeyboardButton("🚀 Exploit Area", callback_data="cat_exploit"),
        types.InlineKeyboardButton("⚙️ System Monitor", callback_data="cat_system")
    ]
    if is_admin(message):
        btns.append(types.InlineKeyboardButton("👨‍💻 Dev Access", callback_data="cat_dev"))
    markup.add(*btns)
    
    caption = "🚀 **NEXUS-OMNI Dashboard**\nReality Mode: [ACTIVE] 💫\nSemua fitur 100% Berjalan."
    bot.send_photo(message.chat.id, IMG["main"], caption=caption, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    bot.answer_callback_query(call.id, "⚡ Nexus Syncing...")
    
    if call.data == "cat_dev":
        global submit_count
        files = subprocess.getoutput("ls -F | head -n 5")
        msg = (
            f"👨‍💻 **DEV ACCESS HUB**\n"
            f"────────────────────\n"
            f"📜 **Script Active**: `main.py`, `bot.py`, `Nexus-Omni`\n"
            f"🔄 **Total Submit/Update**: `{submit_count}`\n"
            f"📂 **Current Path**: `home/termux/Nexus-Omni`\n"
            f"────────────────────\n"
            f"**Server Files:**\n`{files}`"
        )
        markup = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("📝 Update Code", callback_data="dev_update"),
            types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main")
        )
        bot.edit_message_media(media=types.InputMediaPhoto(media=IMG["dev"], caption=msg, parse_mode="Markdown"),
                               chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "cat_intel":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btns = [
            types.InlineKeyboardButton("🛰️ DNS No-IDN", callback_data="run_dns"),
            types.InlineKeyboardButton("🕵️ Reality Proxy", callback_data="run_proxy"),
            types.InlineKeyboardButton("🔍 Port Scanner", callback_data="run_29"),
            types.InlineKeyboardButton("⬅️ Kembali", callback_data="back_main")
        ]
        markup.add(*btns)
        bot.edit_message_media(media=types.InputMediaPhoto(media=IMG["intel"], caption="🕵️ **INTELLIGENCE CATEGORY**\nMode: intelegensi"),
                               chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "back_main":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_welcome(call.message)

    elif call.data.startswith("run_"):
        msg = bot.send_message(call.message.chat.id, "🎯 **Target (IP/Domain):**")
        bot.register_next_step_handler(msg, execute_logic, call.data)

def execute_logic(message, mod):
    target = message.text
    bot.send_message(message.chat.id, f"⚡ **Executing {mod} on {target}...**")
    res = subprocess.getoutput(f"python3 main.py --mode reality --target {target} --mod {mod}")
    bot.send_message(message.chat.id, f"✅ **RESULT:**\n`{res}`", parse_mode="Markdown")

@bot.message_handler(func=lambda m: is_admin(m) and (m.text.startswith('import') or m.text.startswith('def')))
def auto_update(message):
    global submit_count
    with open("main.py", "w") as f:
        f.write(message.text)
    submit_count += 1
    bot.reply_to(message, f"✅ **CODE UPDATED!**\nSubmit Ke: `{submit_count}`\nServer Reality Restarting...")

print(">> NEXUS-OMNI V12.9 ACTIVE!")
bot.infinity_polling()
