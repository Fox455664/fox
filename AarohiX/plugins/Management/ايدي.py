import asyncio
from pyrogram import Client, filters
from AarohiX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# المتغيرات العالمية
iddof = []
italy = []

# قفل الايدي
@app.on_message(
    command(["قفل الايدي", "تعطيل الايدي"]) & filters.group
)
async def iddlock(client, message):
    get = await app.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id in iddof:
            return await message.reply_text("تم تعطيل الايدي من قبل \n√")
        iddof.append(message.chat.id)
        return await message.reply_text("تم تعطيل الايدي بنجاح √")
    else:
        return await message.reply_text("لازم تكون ادمن \n√")

# فتح الايدي
@app.on_message(
    command(["فتح الايدي", "تفعيل الايدي"]) & filters.group
)
async def iddopen(client, message):
    get = await app.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if not message.chat.id in iddof:
            return await message.reply_text("الايدي مفعل من قبل √")
        iddof.remove(message.chat.id)
        return await message.reply_text("تم فتح الايدي بنجاح √")
    else:
        return await message.reply_text("لازم تكون ادمن \n√")

# عرض الايدي
@app.on_message(
    command(["ايدي", "id", "✨ ايدي"]) & filters.group
)
async def iddd(client, message):
    if message.chat.id in iddof:
        return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id) if usr.photo else None
    await message.reply_photo(photo, caption=f""" - ꪀᥲ️︎ꪔᥱ︎ :{message.from_user.mention}\n- u᥉ᥱ︎ɾ :@{message.from_user.username}\n- Ꭵძ . :`{message.from_user.id}`\nႦᎥ᥆ :{usr.bio}\nᥴ𝗁ᥲ️ƚ: {message.chat.title}\n𝚒𝚍 𝚐𝚛𝚘𝚞𝚋 :`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    ) if photo else await message.reply_text("لم أستطع تحميل صورة المستخدم.")

# قفل جمالي
@app.on_message(
    command(["قفل جمالي", "تعطيل جمالي"]) & filters.group
)
async def lllock(client, message):
    get = await app.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id in iddof:
            return await message.reply_text("جمالي معطل من قبل √")
        iddof.append(message.chat.id)
        return await message.reply_text("تم تعطيل جمالي بنجاح √")
    else:
        return await message.reply_text("لازم تكون ادمن \n√")

# فتح جمالي
@app.on_message(
    command(["فتح جمالي", "تفعيل جمالي"]) & filters.group
)
async def idljjopen(client, message):
    get = await app.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if not message.chat.id in iddof:
            return await message.reply_text("جمالي مفعل من قبل √")
        iddof.remove(message.chat.id)
        return await message.reply_text("تم فتح جمالي بنجاح √")
    else:
        return await message.reply_text("هذا الامر لأدمن فقط")

# جمالي
@app.on_message(
    command(["جمالي"]) & filters.group
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
        return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60", "66", "70", "77", "80", "85", "90", "99", "100", "1000"]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id) if usr.photo else None
    await message.reply_photo(photo, caption=f"نسبه جمالك يا مز انت \n※ \n🐉: {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    ) if photo else await message.reply_text(f"نسبه جمالك يا مز انت \n※ \n🐉: {ik} %😂❤️")

# تفعيل التعديل
@app.on_message(filters.command(['تفعيل التعديل'], prefixes=""))
async def iddlock(client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id in italy:
            return await message.reply_text("تم تفعيل التعديل مسبقًا \n√")
        italy.append(message.chat.id)
        return await message.reply_text("تم تفعيل التعديل بنجاح \n√")
    else:
        return await message.reply_text("يجب أن تكون مشرف أولاً \n√")

# تعطيل التعديل
@app.on_message(filters.command(['تعطيل التعديل'], prefixes=""))
async def iddopen(client, message):
    get = await app.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if not message.chat.id in italy:
            return await message.reply_text("التعديل معطل من قبل \n√")
        italy.remove(message.chat.id)
        return await message.reply_text("تم تعطيل التعديل بنجاح \n√")
    else:
        return await message.reply_text("يجب أن تكون أدمن أولاً \n√")
