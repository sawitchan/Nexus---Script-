import telebot
from telebot import types
import subprocess

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
bot = telebot.TeleBot(TOKEN)

FEATURES = {
    "NETWORK": [("01 DDoS Flood", "01"), ("04 Web-Shield", "04"), ("06 Proxy Scrap", "06"), ("22 Proxy Gate", "22"), ("23 VPN Tunnel", "23"), ("24 Botnet Node", "24"), ("40 Tor Node", "40"), ("42 Port Forward", "42"), ("46 API Protect", "46")],
    "SECURITY": [("03 Anti-Sniff", "03"), ("25 Health Check", "25"), ("26 IDS Sniffer", "26"), ("27 Tele Alert", "27"), ("31 WiFi Crack", "31"), ("32 Packet Sniff", "32"), ("35 Metadata Ex", "35"), ("38 Email Verif", "38"), ("44 Vuln Scan", "44"), ("45 Shell Acc", "45"), ("50 Final Def", "50")],
    "INTEL": [("05 IP Track", "05"), ("09 Port Scan", "09"), ("10 DNS Lookup", "10"), ("15 Global IP", "15"), ("29 Deep Scan", "29"), ("30 Domain Intel", "30"), ("37 Subdom Find", "37"), ("41 Admin Find", "41"), ("43 Sitemap Gen", "43")],
    "EXPLOIT": [("16 SQLi", "16"), ("17 XSS Scan", "17"), ("18 Brute Force", "18"), ("19 Payload Gen", "19"), ("20 Backdoor", "20"), ("33 Ssh Brute", "33"), ("34 Ftp Exploit", "34"), ("36 Hash Crack", "36"), ("39 Cloud BP", "39"), ("49 Web Cloner", "49")],
    "SYSTEM": [("02 Auth Keygen", "02"), ("07 MAC Change", "07"), ("08 Sys Info", "08"), ("11 RAM Usage", "11"), ("12 CPU Temp", "12"), ("13 Storage Check", "13"), ("14 Log Cleaner", "14"), ("21 Cyber Live", "21"), ("28 Auto Clean", "28"), ("47 Encrypt", "47"), ("48 Decrypt", "48")]
}

@bot.message_handler(commands=['start', 'menu'])
def start(m):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for k in FEATURES.keys():
        markup.add(types.InlineKeyboardButton(f"📦 STORE: {k}", callback_data=f"cat_{k}"))
    bot.send_message(m.chat.id, "🏪 **NEXUS-OMNI REAL ENGINE**\nStatus: Online & Real-time Execution.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    if call.data.startswith("cat_"):
        cat = call.data.split("_")[1]
        markup = types.InlineKeyboardMarkup(row_width=2)
        btns = [types.InlineKeyboardButton(n, callback_data=f"run_{v}_{cat}") for n, v in FEATURES[cat]]
        markup.add(*btns)
        markup.add(types.InlineKeyboardButton("⬅️ BACK", callback_data="back"))
        bot.edit_message_text(f"🏪 **KATEGORI: {cat}**", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data.startswith("run_"):
        _, mid, cat = call.data.split("_")
        msg = bot.send_message(call.message.chat.id, f"🎯 **EXECUTE MODULE: {mid}**\nMasukkan Target IP/Domain:")
        bot.register_next_step_handler(msg, lambda m: run_logic(m, mid, cat))

    elif call.data == "back":
        start(call.message)

def run_logic(m, mid, cat):
    # INI ADALAH EKSEKUSI NYATA KE TERMINAL TERMUX
    res = subprocess.getoutput(f"python3 main.py --mod {mid} --target {m.text}")
    markup = types.InlineKeyboardMarkup()
  
    if cat == "INTEL":
        markup.add(types.InlineKeyboardButton("💉 SQL INJECTION", callback_data=f"run_16_EXPLOIT"))
    elif cat == "EXPLOIT":
        markup.add(types.InlineKeyboardButton("🚪 INSTALL BACKDOOR", callback_data=f"run_20_EXPLOIT"))

    markup.add(types.InlineKeyboardButton("🔄 MENU", callback_data="back"))
    bot.send_message(m.chat.id, f"✅ **RESULT:**\n`{res}`", reply_markup=markup, parse_mode="Markdown")

bot.polling(non_stop=True)
