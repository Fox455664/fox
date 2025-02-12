import asyncio
import re
import sys
from os import getenv
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from dotenv import load_dotenv
from AarohiX import app
from AarohiX.misc import SUDOERS
from strings.filters import command

# تحميل المتغيرات من .env
load_dotenv()

# المتغيرات من البيئة
OWNER_ID = getenv("OWNER_ID")
OWNER_USER_NAME = getenv("OWNER_USER_NAME")
NEON = getenv("NEON")
OWNER = getenv("OWNER")

# رسالة الرد وأزرار الرد
REPLY_MESSAGE = "**👋︙مـرحـبـا بـك عـزيـزي الـمـطـور ♥️**\n**✨︙فــي قـائـمـة التحـكـم بـالـبـوت💞**"
REPLY_MESSAGE_BUTTONS = [
    ["《مطور البوت》", "✨ مطور السورس"],
    ["《اضافه البوت لمجموعتك》"],
    ["السورس", "⋖━❲𖣂❳━⋗", "✭ قسم المطورين"],
    ["✭ قسم الاذاعه", "⋖━❲𖣂❳━⋗", "✭ قسم الجروبات"],
    ["✨ بنك العالم", "⋖━❲𖣂❳━⋗", "✨ ابراج"],
    ["✨ ازكار", "⋖━❲𖣂❳━⋗", "✨ حكمه"],
    ["●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●"],
    ["زخرفه", "⋖━❲𖣂❳━⋗", "✨ نسبه الرجوله"],
    ["✨ احكام", "⋖━❲𖣂❳━⋗", "✨ معلومات"],
    ["✨ العاب", "⋖━❲𖣂❳━⋗", "✨ اغاني"],
    ["✨ اسمي", "⋖━❲𖣂❳━⋗", "✨ افلام"],
    ["✨ كت", "⋖━❲𖣂❳━⋗", "✨ تويت"],
    ["✨ رايك بصورتي", "⋖━❲𖣂❳━⋗", "✨ حساب العمر"],
    ["●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●"],
    ["✨ حذف حسابي", "⋖━❲𖣂❳━⋗", "✨ انصحني"],
    ["✨ مميزات", "⋖━❲𖣂❳━⋗", "✨ بوت"],
    ["✨ نكته", "⋖━❲𖣂❳━⋗", "✨ حروف"],
    ["✨ صوره", "⋖━❲𖣂❳━⋗", "✨ غنيلي"],
    ["✨ انمي", "⋖━❲𖣂❳━⋗", "✨ متحركه"],
    ["✨ اقتباسات", "⋖━❲𖣂❳━⋗", "✨ هيدرات"],
    ["●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●"],
    ["✨ صور بنات", "⋖━❲𖣂❳━⋗", "✨ صور شباب"],
    ["✨ قرآن", "⋖━❲𖣂❳━⋗", "✨ الشيخ نقشبندي"],
    ["✨ استوريهات", "⋖━❲𖣂❳━⋗", "✨ عاوز انصب"],
    ["✨ ايدي", "⋖━❲𖣂❳━⋗", "✨ خيرني"],
    ["✨ تلاوة"],
    ["🥺 ¦ حذف الكيبورد"]
]

@app.on_message(command(["كيب", "✭ رجوع"]) & SUDOERS)
async def crsourceowner(client: Client, message: Message):
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=REPLY_MESSAGE,
        reply_markup=reply_markup
    )

# دوال التعامل مع الأوامر المختلفة
async def create_reply_markup(buttons):
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

@app.on_message(filters.command(["✭ قسم الاذاعه"], "") & SUDOERS)
async def section_broadcast(client: Client, message: Message):
    buttons = [["✭ اذاعه عام", "✭ اذاعه بالتوجيه"], ["✭ رجوع"]]
    reply_markup = await create_reply_markup(buttons)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=reply_markup)

@app.on_message(filters.command(["السورس"], "") & SUDOERS)
async def source_section(client: Client, message: Message):
    buttons = [["✭ قـنـاة الـسـورس", "✭ للتواصل معنآ"], ["✭ مطور السورس"], ["✭ رجوع"]]
    reply_markup = await create_reply_markup(buttons)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم السورس تحكم بالازار**", reply_markup=reply_markup)

@app.on_message(filters.command(["✭ قسم المطورين"], "") & SUDOERS)
async def developers_section(client: Client, message: Message):
    buttons = [["✭ مـطـوريـنـك", "✭ للتواصل معنآ"], ["✭ رجوع"]]
    reply_markup = await create_reply_markup(buttons)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم المطورين تحكم بالازار**", reply_markup=reply_markup)

@app.on_message(filters.command(["✭ قسم الجروبات"], "") & SUDOERS)
async def groups_section(client: Client, message: Message):
    buttons = [["✭ الجروبات المحظوره", "✭ الاحصائيات", "✭ حـظـر الـجـروبـات"], ["✭ رجوع", "✭ جـروبـاتـك النـشـطـه"]]
    reply_markup = await create_reply_markup(buttons)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الجروبات تحكم بالازار**", reply_markup=reply_markup)

@app.on_message(filters.regex("✭ قـنـاة الـسـورس"))
async def reply_to_channel(client: Client, message: Message):
    await message.reply_photo(
        photo="https://t.me/nor_o",
        caption="[ َِ.سـورس ميـوزك الـعالم.〙-𓏺Whoever humbles #himself to god will be #exalted](https://t.me/vzo_a)",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url="https://t.me/vzo_a")]]
        )
    )

@app.on_message(filters.regex("✭ مطور السورس"))
async def reply_to_dev(client: Client, message: Message):
    await message.reply_photo(
        photo="https://t.me/nor_o",  # تأكد من صحة الرابط
        caption="[THIS DEV MAIN  سـورس ميـوزك الـعالم](https://t.me/nor_o)",  # تأكد من النص والرابط
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url="https://t.me/vzo_a")]]  # تأكد من صحة الرابط هنا أيضًا
        )
    )

@app.on_message(filters.regex("✭ مـطـوريـنـك"))
async def reply_to_devs(client: Client, message: Message):
    buttons = [
        [InlineKeyboardButton("مطور السورس", url="https://t.me/NOR_O")],
        [InlineKeyboardButton("مبرمج السورس", url="https://t.me/F_o_x_5")],
        [InlineKeyboardButton("مطور السورس", url="https://t.me/N_7_K")],  # يمكنك تعديل هذا الرابط حسب الحاجة
        [InlineKeyboardButton("رجوع", callback_data="back_to_main")]
    ]
    await message.reply_text(
        "**أهلا بك عزيزي المطور**\n**هنا قسم المطورين، اختر من الأزرار أدناه للتواصل مع مطوري السورس.**",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@app.on_message(filters.regex("✨ استوريهات"))
async def reply_to_stories(client: Client, message: Message):
    await message.reply_text("**هنا قسم الاستوريهات**")

@app.on_message(filters.regex("✨ فيلم"))
async def reply_to_movies(client: Client, message: Message):
    await message.reply_text("**هنا يمكنك طلب أفلام**")

@app.on_message(filters.regex("✨ ايدي"))
async def reply_to_id(client: Client, message: Message):
    await message.reply_text("**هنا يمكنك طلب معرفات**")

@app.on_message(filters.regex("✨ خيرني"))
async def reply_to_choose(client: Client, message: Message):
    await message.reply_text("**هنا يمكنك اختيار من بين الخيارات المتاحة**")

@app.on_message(filters.regex("🥺 ¦ حذف الكيبورد"))
async def remove_keyboard(client: Client, message: Message):
    await message.reply_text("**تم حذف الكيبورد**", reply_markup=ReplyKeyboardRemove())

if __name__ == "__main__":
    app.run()

