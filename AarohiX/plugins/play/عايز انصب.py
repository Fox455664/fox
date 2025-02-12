from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config
from pyrogram.errors import FloodWait




@app.on_message(filters.command(["✨ عاوز انصب","✨ عاوز انصب"], ""))
async def maker(client: Client, message: Message):
     await message.reply_video(
        video="https://te.legra.ph/file/dc7f2ebb2dd8656b308d6.mp4",
        caption="◍يمكنك الان التواصل مع المطور ❲ [اطغط هنا](https://t.me/NOR_O) ❳ \n\n√",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
