import telebot
from telebot import types
import subprocess

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
bot = telebot.TeleBot(TOKEN)

# Mapping 50 Fitur Ke Button (Sesuai Dashboard Tuan)
FEATURES = {
    "NETWORK": [("01 DDoS Shield", "01"), ("04 Web-Shield", "04"), ("06 Proxy Scraper", "06"), ("10 DNS Lookup", "10"), ("22 Proxy Gate", "22")],
    "SECURITY": [("03 Anti-Sniff", "03"), ("25 Health Check", "25"), ("26 IDS Sniffer", "26"), ("31 WiFi Cracker", "31"), ("50 Final Defense", "50")],
    "INTEL": [("05 IP Tracker", "05"), ("09 Port Scanner", "09"), ("15 Global IP", "15"), ("30 Domain Intel", "30"), ("37 Subdom Finder", "37")],
    "EXPLOIT": [("16 SQL Injector", "16"), ("18 Brute Force", "18"), ("19 Payload Gen", "19"), ("20 Backdoor", "20"), ("34 Ftp Exploit", "34")],
    "SYSTEM": [("07 MAC Changer", "07"), ("08 System Info", "08"), ("11 RAM Usage", "11"), ("14 Log Cleaner", "14"), ("47 Encrypter", "47")],
    "DEFENSE": [("02 Auth Keygen", "02"), ("12 CPU Temp", "12"), ("23 VPN Tunnel", "23"), ("40 Tor Node", "40"), ("46 API Protect", "46")]
}

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = [types.InlineKeyboardButton(k, callback_data=f"cat_{k}") for k in FEATURES.keys()]
    markup.add(*btns)
    markup.add(types.InlineKeyboardButton("👨‍💻 DEV HUB", callback_data="cat_dev"))
    bot.send_photo(message.chat.id, "https://c.termai.cc/i101/NoQ.jpg", 
                  caption="🚀 **NEXUS-OMNI FINAL V15.7**\nStatus: Stealth Mode Active\nUser: Tuan Markus", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data.startswith("cat_") and call.data != "cat_dev":
        cat = call.data.split("_")[1]
        markup = types.InlineKeyboardMarkup(row_width=2)
        # GENERATE BUTTON PER FITUR! Gak perlu ngetik lagi!
        btns = [types.InlineKeyboardButton(name, callback_data=f"run_{val}") for name, val in FEATURES[cat]]
        markup.add(*btns)
        markup.add(types.InlineKeyboardButton("⬅️ KEMBALI", callback_data="back"))
        bot.edit_message_caption(f"📂 **KATEGORI: {cat}**\nPilih modul untuk dijalankan:", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")
    
    elif call.data.startswith("run_"):
        mod_id = call.data.split("_")[1]
        msg = bot.send_message(call.message.chat.id, f"🎯 **MODUL {mod_id} SELECTED**\nMasukkan Target (Contoh: google.com atau 8.8.8.8):")
        bot.register_next_step_handler(msg, lambda m: execute_logic(m, mod_id))

    elif call.data == "back":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_welcome(call.message)

def execute_logic(message, mod_id):
    target = message.text
    bot.send_message(message.chat.id, f"🚀 **Executing run_{mod_id} on {target}...**")
    # Jalankan engine main.py Tuan
    res = subprocess.getoutput(f"python3 main.py --mod {mod_id} --target {target}")
    bot.send_message(message.chat.id, f"✅ **RESULT:**\n`{res}`", parse_mode="Markdown")

bot.polling(non_stop=True)
