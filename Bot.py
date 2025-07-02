import logging
import json
import os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, filters, ContextTypes
from dotenv import load_dotenv  # 🔥 استدعاء dotenv

# إعداد نظام السجلات
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# تحميل ملفات البيئة (.env)
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")  # 🔥 استدعاء التوكن من الملف السري

# مراحل المحادثة
(ENTRY, STOP_LOSS, TARGETS, SESSION, TRADE_TYPE, MODEL, RESULT, NOTE, 
 CONFIRM, MENU, VIEW_TRADES, DELETE_TRADE) = range(12)

# 👇 الكلاس TradingBot كامل ديالك لصقو هنا تحت بدون تغيير
# (راه طويل بزاف، وخاصك غير تكملو عادي من هنا)

# ‼️ ملاحظة: تأكد أنك لصقت **كامل الكلاس** TradingBot اللي عطيتيني فالسابق
# ما تبدل فيه والو، فقط حطو بعد هاد السطر:

class TradingBot:
    def __init__(self, token):
        self.token = token
        self.trades_file = "trades.json"
        self.trades = self.load_trades()
    
    # ... 👈 لصق باقي الكود اللي عندك هنا كامل ...

# تشغيل البوت
if __name__ == '__main__':
    if not BOT_TOKEN:
        print("❌ لم يتم العثور على التوكن! تأكد من أنك وضعت BOT_TOKEN في ملف .env")
    else:
        bot = TradingBot(BOT_TOKEN)
        bot.run()
