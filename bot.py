import telebot
from telebot import types
import subprocess

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
bot = telebot.TeleBot(TOKEN)

# DATABASE 50 FITUR - FULL BUTTON
FEATURES = {
    "NETWORK & DEFENSE": [
        ("01 DDoS Shield", "01"), ("02 Auth Keygen", "02"), ("04 Web-Shield", "04"), 
        ("06 Proxy Scraper", "06"), ("22 Proxy Gate", "22"), ("23 VPN Tunnel", "23"),
        ("24 Botnet Node", "24"), ("40 Tor Node", "40"), ("42 Port Forward", "42"), ("46 API Protect", "46")
    ],
    "SECURITY & SCAN": [
        ("03 Anti-Sniff", "03"), ("25 Health Check", "25"), ("26 IDS Sniffer", "26"), 
        ("29 Deep Scan", "29"), ("31 WiFi Cracker", "31"), ("32 Packet Sniff", "32"),
        ("44 Vuln Scanner", "44"), ("45 Shell Access", "45"), ("50 Final Defense", "50"), ("27 Telegram Alert", "27")
    ],
    "INTELLIGENCE": [
        ("05 IP Tracker", "05"), ("09 Port Scanner", "09"), ("10 DNS Lookup", "10"), 
        ("15 Global IP", "15"), ("30 Domain Intel", "30"), ("35 Metadata Ex", "35"),
        ("37 Subdom Finder", "37"), ("38 Email Verif", "38"), ("41 Admin Finder", "41"), ("43 Sitemap Gen", "43")
    ],
    "EXPLOIT": [
        ("16 SQL Injector", "16"), ("17 XSS Scanner", "17"), ("18 Brute Force", "18"), 
        ("19 Payload Gen", "19"), ("20 Backdoor", "20"), ("33 Ssh Brute", "33"),
        ("34 Ftp Exploit", "34"), ("36 Hash Cracker", "36"), ("39 Cloud BP", "39"), ("49 Web Cloner", "49")
    ],
    "SYSTEM": [
        ("07 MAC Changer", "07"), ("08 System Info", "08"), ("11 RAM Usage", "11"), 
        ("12 CPU Temp", "12"), ("13 Storage Check", "13"), ("14 Log Cleaner", "14"),
        ("21 Cyber Live", "21"), ("28 Auto Clean", "28"), ("47 Encrypter", "47"), ("48 Decrypter", "48")
    ]
}

@bot.message_handler(commands=['start', 'menu'])
def start(m):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for k in FEATURES.keys():
        markup.add(types.InlineKeyboardButton(f"📂 {k}", callback_data=f"cat_{k}"))
    bot.send_photo(m.chat.id, "https://c.termai.cc/i101/NoQ.jpg", 
                  caption="🚀 **NEXUS-OMNI V16.5 ULTIMATUM**\nUser: Tuan Markus\nStatus: 50 Moduls Ready.", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    if call.data.startswith("cat_"):
        cat = call.data.split("_")[1]
        markup = types.InlineKeyboardMarkup(row_width=2)
        btns = [types.InlineKeyboardButton(n, callback_data=f"run_{v}") for n, v in FEATURES[cat]]
        markup.add(*btns)
        markup.add(types.InlineKeyboardButton("⬅️ BACK TO MENU", callback_data="back"))
        bot.edit_message_caption(f"📂 **KATEGORI: {cat}**", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data.startswith("run_"):
        mid = call.data.split("_")[1]
        msg = bot.send_message(call.message.chat.id, f"🎯 **MODUL {mid} SELECTED**\nMasukkan IP/Domain target:")
        bot.register_next_step_handler(msg, lambda m: run_engine(m, mid))

    elif call.data.startswith("chain_"):
        target = call.data.split("_")[1]
        bot.send_message(call.message.chat.id, f"💀 **CHAINING EXPLOIT ON {target}...**\nModul: 16 (SQLi) Initiated via Proxy Ghost.")

    elif call.data == "back":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start(call.message)

def run_engine(m, mid):
    res = subprocess.getoutput(f"python3 main.py --mod {mid} --target {m.text}")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🚀 HACK THIS IP (CHAIN)", callback_data=f"chain_{m.text}"))
    markup.add(types.InlineKeyboardButton("🔄 MENU", callback_data="back"))
    bot.send_message(m.chat.id, res, reply_markup=markup, parse_mode="Markdown")

bot.polling(non_stop=True)
