import telebot
import time
import threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# بيانات البوت
TOKEN = "7578353579:AAG9_vIkC19Idepm-nMqf1-9IMcA1ni_bAE"
GROUP_ID = "-1002207678151"  # تأكد من أن الجروب سوبر جروب

# إنشاء البوت
bot = telebot.TeleBot(TOKEN)

# الرسالة التي سيتم إرسالها للجروب
MESSAGE_TEXT = """📢 *تم فتح باب الإيداع الآن!* 📢

🚀 استثمر في *الفوركس والعملات الرقمية* مع *الأستاذ أحمد فرج رمضان الليبي* 💰  
💡 *فرصة استثمارية مضمونة* لتحقيق أرباح مميزة! ✅  

🔹 استفد من خبرتنا في السوق  
🔹 إدارة أموالك بأمان واحترافية  
🔹 تحقيق عوائد مستدامة  

⬇️ للاشتراك والاستثمار اضغط على الزر أدناه ⬇️"""

# الرسالة التلقائية عند استقبال رسالة في الخاص
AUTO_REPLY_TEXT = """🎯 *هل تبحث عن استثمار مضمون وآمن؟* 🎯  

🚀 استثمر في *الفوركس والعملات الرقمية* معنا وحقق أرباحًا مميزة!  

💰 *لماذا تختارنا؟*  
✅ أرباح ثابتة ومضمونة  
✅ إدارة محترفة للأموال  
✅ نسبة المخاطر معدومة  

⬇️ اضغط للاشتراك والاستثمار ⬇️"""

# متغير لتخزين ID آخر رسالة مرسلة في الجروب
last_message_id = None

# إنشاء لوحة الأزرار
def get_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("💵 للاشتراك والاستثمار اضغط هنا", url="https://t.me/AHMED1_1FARAG"))
    markup.add(InlineKeyboardButton("📞 للتواصل عبر واتساب اضغط هنا", url="https://wa.me/message/DECYCNVGV2OEP1"))
    return markup

# وظيفة إرسال الرسالة للجروب كل 10 دقائق مع حذف الرسالة القديمة
def send_message():
    global last_message_id
    while True:
        try:
            # حذف الرسالة القديمة إذا كانت موجودة
            if last_message_id:
                try:
                    bot.delete_message(GROUP_ID, last_message_id)
                    print("🗑️ تم حذف الرسالة القديمة بنجاح.")
                except Exception as e:
                    print(f"⚠️ لم يتمكن من حذف الرسالة القديمة: {e}")

            # إرسال الرسالة الجديدة
            msg = bot.send_message(GROUP_ID, MESSAGE_TEXT, parse_mode="Markdown", reply_markup=get_keyboard())
            last_message_id = msg.message_id  # تخزين ID الرسالة الجديدة
            
            print(f"✅ تم إرسال الرسالة الجديدة (ID: {last_message_id})")

            time.sleep(600)  # 10 دقائق = 600 ثانية
        except Exception as e:
            print(f"❌ حدث خطأ أثناء إرسال الرسالة للجروب: {e}")
            time.sleep(60)  # انتظار دقيقة قبل المحاولة مجددًا

# الرد التلقائي عند استقبال رسالة في الخاص
@bot.message_handler(func=lambda message: message.chat.type == "private", content_types=['text'])
def auto_reply(message):
    try:
        bot.send_message(message.chat.id, AUTO_REPLY_TEXT, parse_mode="Markdown", reply_markup=get_keyboard())
        print(f"✅ تم الرد تلقائيًا على المستخدم {message.chat.id}")
    except Exception as e:
        print(f"❌ حدث خطأ أثناء الرد التلقائي: {e}")

# تشغيل الوظائف في نفس الوقت
if __name__ == "__main__":
    threading.Thread(target=send_message, daemon=True).start()
    print("✅ البوت يعمل الآن بنجاح!")

    while True:
        try:
            print("🔄 إعادة تشغيل البوت...")
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            print(f"⚠️ خطأ في الاتصال، سيتم إعادة المحاولة خلال 5 ثوانٍ: {e}")
            time.sleep(5)  # انتظار 5 ثوانٍ قبل إعادة المحاولة