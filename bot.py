import telebot
import os
import subprocess
import time
from telebot import types

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
bot = telebot.TeleBot(TOKEN)

FEATURES = {
    "network": ["01 DDoS Shield", "04 Web-Shield", "06 Proxy Scraper", "22 Proxy Gate", "40 Tor Node"],
    "security": ["03 Anti-Sniff", "25 Health Check", "26 IDS Sniffer", "31 WiFi Cracker", "50 Final Defense"],
    "intel": ["05 IP Tracker", "09 Port Scanner", "15 Global IP", "30 Domain Intel", "37 Subdom Finder"],
    "exploit": ["16 SQL Injector", "18 Brute Force", "19 Payload Gen", "20 Backdoor", "34 Ftp Exploit"],
    "system": ["07 MAC Changer", "08 System Info", "11 RAM Usage", "14 Log Cleaner", "47 Encrypter"]
}

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = [types.InlineKeyboardButton(k.upper(), callback_data=f"cat_{k}") for k in FEATURES.keys()]
    markup.add(*btns)
    markup.add(types.InlineKeyboardButton("👨‍💻 DEV HUB", callback_data="cat_dev"))
    bot.send_photo(message.chat.id, "https://c.termai.cc/i101/NoQ.jpg", 
                  caption="🚀 **NEXUS-OMNI DASHBOARD V15.5**\nStatus: Online & Protected", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data.startswith("cat_") and call.data != "cat_dev":
        cat = call.data.split("_")[1]
        list_f = "\n".join([f"• {f}" for f in FEATURES[cat]])
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔍 Run Modul", callback_data="run_mod"),
                                                  types.InlineKeyboardButton("⬅️ Kembali", callback_data="back"))
        bot.edit_message_caption(f"📂 **{cat.upper()} MODULES**\n\n{list_f}", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")
    
    elif call.data == "cat_dev":
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔄 UPDATE ENGINE", callback_data="dev_upd"),
                                                  types.InlineKeyboardButton("⬅️ Kembali", callback_data="back"))
        bot.edit_message_caption("👨‍💻 **DEVELOPER HUB**\nAuto-Backup: ACTIVE 🛡️", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "dev_upd":
        res = subprocess.getoutput("git pull origin main && pm2 restart Nexus-Bot")
        bot.send_message(call.message.chat.id, f"✅ **Update:**\n`{res}`")

    elif call.data == "run_mod":
        msg = bot.send_message(call.message.chat.id, "🎯 **Input: [Nomor] [Target]**")
        bot.register_next_step_handler(msg, execute_remote)

    elif call.data == "back":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_welcome(call.message)

def execute_remote(message):
    try:
        mod, tgt = message.text.split()
        res = subprocess.getoutput(f"python3 main.py --mod {mod} --target {tgt}")
        bot.send_message(message.chat.id, res, parse_mode="Markdown")
    except: bot.send_message(message.chat.id, "❌ Error Format")

bot.polling(non_stop=True)
