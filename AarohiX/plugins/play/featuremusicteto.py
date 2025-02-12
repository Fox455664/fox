import asyncio


import random


from AarohiX import app


from pyrogram.types import (InlineKeyboardButton,


                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client





@app.on_message(
    filters.command(["✨ مميزات"], "")
& filters.group
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**⦿   𝑊𝑂𝑅𝐿𝐷 𝑺𝑂𝑈𝑅𝐶𝐸 قايمه مميزات سورس  :\n
╮⦿  المطور
│᚜⦿ سؤال
│᚜⦿ مين في الكول 
│᚜⦿ تفعيل الاذان
│᚜⦿ كت
│᚜⦿ احكام
│᚜⦿ افتح الكول
│᚜⦿ احرف
│᚜⦿ الرابط
│᚜⦿ البنك 
│᚜⦿ منع تصفيه تلقائي
│᚜⦿ رفع مشرف
│᚜⦿ شعر
│᚜⦿ نادي المطور
│᚜⦿ زخرفه
│᚜⦿ مميزات
│᚜⦿ همسه
│᚜⦿ يوت
│᚜⦿ تحميل
│᚜⦿ لو خيروك
│᚜⦿ معلومات الجروب
│᚜⦿ طرد كتم
│᚜⦿ تلكراف ميديا
│᚜⦿ اسكرين 
│᚜⦿ صراحه
│᚜⦿ صور
│᚜⦿ صور بنات 
│᚜⦿ صور شباب
│᚜⦿ السورس 
│᚜⦿ كتم
│᚜⦿ اقتباس
│᚜⦿ هيدرات
│᚜⦿ اذكار 
╯⦿  بث مباشر للقنوات 
[𝑊𝑂𝑅𝐿𝐷 𝑺𝑂𝑈𝑅𝐶𝐸](https://t.me/vzo_a) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "{مــطور الـسورس}", url=f"https://t.me/nor_o"),                        
                 ],[
                InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
          ]
        ),
    )

