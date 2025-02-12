from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from AarohiX import app  # Assuming `app` is initialized in AarohiX

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

# Command to send a video with buttons
@app.on_message(filters.command(["✨ سورس", "مطور السورس"]))
async def send_source_video(client: Client, message: Message):
    await message.reply_video(
        video="https://te.legra.ph/file/d04bea15f20fb094a047c.mp4",
        caption="⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("مـطور السـورس", url="https://t.me/M_9_T"),
                    InlineKeyboardButton("مبزمج السورس", url="https://t.me/F_o_x_5")
                ],
                [
                    InlineKeyboardButton("قـناه السـورس", url="https://t.me/vzo_a")
                ],
                [
                    InlineKeyboardButton("اضغط لاضافتي لمجموعتك⚡", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

# Command to show developer info (M_9_T)
@app.on_message(filters.command(["المطور نور"]))
async def show_developer_info(client: Client, message: Message):
    usr = await client.get_chat("M_9_T")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(
        photo,
        caption=f"معلومات مطور السورس\n\n‍ ¦➻ 𝐍𝐀𝐌𝐄 :{name}\n\n ¦➻ 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n ¦➻ 𝐈𝐃 :`{usr.id}`\n\n ¦➻ 𝐁𝐎𝐈 :{usr.bio}\n\nســورس ميــوزك العـالم",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")
                ]
            ]
        ),
    )

# Command to show developer info (Hokam)
@app.on_message(filters.command(["حكم", "فوكس", "مبرمج السورس"]))
async def show_programmer_info(client: Client, message: Message):
    usr = await client.get_chat("F_o_x_5")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(
        photo,
        caption=f"معلومات مبرمج السورس.\n\n¦➻ 𝐍𝐀𝐌𝐄 :{name}\n\n ¦➻ 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n ¦➻ 𝐈𝐃 :`{usr.id}`\n\n ¦➻ 𝐁𝐎𝐈 :{usr.bio}\n\nسـورس مـيوزك العـالم",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")
                ]
            ]
        ),
    )
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

# Command to show developer info (Hokam)
@app.on_message(filters.command(["حكم", "فوكس", "مبرمج السورس"]))
async def show_programmer_info(client: Client, message: Message):
    try:
        usr = await client.get_chat("F_o_x_5")
        name = usr.first_name
        photo = usr.photo.big_file_id if usr.photo else None
        if photo:
            photo_path = await app.download_media(photo)
            await message.reply_photo(
                photo_path,
                caption=f"معلومات مبرمج السورس.\n\n¦➻ 𝐍𝐀𝐌𝐄 : {name}\n\n¦➻ 𝐔𝐒𝐄𝐑 : @{usr.username}\n\n¦➻ 𝐈𝐃 : `{usr.id}`\n\n¦➻ 𝐁𝐎𝐈 : {usr.bio if usr.bio else 'لا توجد معلومات'}\n\nسـورس مـيوزك العـالم",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")
                        ]
                    ]
                ),
            )
        else:
            await message.reply(
                f"معلومات مبرمج السورس.\n\n¦➻ 𝐍𝐀𝐌𝐄 : {name}\n\n¦➻ 𝐔𝐒𝐄𝐑 : @{usr.username}\n\n¦➻ 𝐈𝐃 : `{usr.id}`\n\n¦➻ 𝐁𝐎𝐈 : {usr.bio if usr.bio else 'لا توجد معلومات'}\n\nسـورس مـيوزك العـالم",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")
                        ]
                    ]
                ),
            )
    except Exception as e:
        await message.reply(f"حدث خطأ: {e}")

# Command to show developer info (Ahmed)
@app.on_message(filters.command(["مطور السورس", "الحاكم", "احمد"]))
async def show_programmer_info_ahmed(client: Client, message: Message):
    try:
        usr = await client.get_chat("N_7_K")
        name = usr.first_name
        photo = usr.photo.big_file_id if usr.photo else None
        if photo:
            photo_path = await app.download_media(photo)
            await message.reply_photo(
                photo_path,
                caption=f"معلومات مبرمج السورس.\n\n¦➻ 𝐍𝐀𝐌𝐄 : {name}\n\n¦➻ 𝐔𝐒𝐄𝐑 : @{usr.username}\n\n¦➻ 𝐈𝐃 : `{usr.id}`\n\n¦➻ 𝐁𝐎𝐈 : {usr.bio if usr.bio else 'لا توجد معلومات'}\n\nسـورس مـيوزك الـعالم",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")
                        ]
                    ]
                ),
            )
        else:
            await message.reply(
                f"معلومات مبرمج السورس.\n\n¦➻ 𝐍𝐀𝐌𝐄 : {name}\n\n¦➻ 𝐔𝐒𝐄𝐑 : @{usr.username}\n\n¦➻ 𝐈𝐃 : `{usr.id}`\n\n¦➻ 𝐁𝐎𝐈 : {usr.bio if usr.bio else 'لا توجد معلومات'}\n\nسـورس مـيوزك الـعالم",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")
                        ]
                    ]
                ),
            )
    except Exception as e:
        await message.reply(f"حدث خطأ: {e}")
