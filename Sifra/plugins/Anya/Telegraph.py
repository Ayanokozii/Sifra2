import os
import asyncio
from typing import Optional
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from telegraph import upload_file
from Sifra import app

# --------------- FUNCTION --------------- #

def get_file_id(msg: Message) -> Optional[Message]:
    if not msg.media:
        return None

    for message_type in ("photo", "animation", "audio", "document", "video", "video_note", "voice", "sticker"):
        obj = getattr(msg, message_type, None)
        if obj:
            setattr(obj, "message_type", message_type)
            return obj
    return None

# --------------- FUNCTION --------------- #

@app.on_message(filters.command("tgm"))
async def telegraph_upload(client: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("Reply to a photo or video under 5MB.")

    file_info = get_file_id(replied)
    if not file_info:
        return await message.reply_text("Not Supported!")

    text = await message.reply_text("<code>Downloading to my server...</code>", disable_web_page_preview=True)
    media = await replied.download()

    await text.edit_text("<code>Download complete. Uploading to telegra.ph...</code>")

    try:
        loop = asyncio.get_running_loop()
        response = await loop.run_in_executor(None, upload_file, media)

        if not response or not isinstance(response, list):  # Ensure response is a valid list
            raise ValueError("Invalid response from Telegra.ph API")
        
        telegraph_link = f"https://te.legra.ph{response[0]}"
    except Exception as error:
        print(f"Upload Error: {error}")
        return await text.edit_text(f"Error: {error}")

    try:
        os.remove(media)
    except Exception as error:
        print(f"File Removal Error: {error}")

    await text.edit_text(
        text=f"<b>Here is your generated Telegra.ph link:</b>\n\n"
             f"<code>{telegraph_link}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Open Link", url=telegraph_link),
                InlineKeyboardButton("Share Link", url=f"https://telegram.me/share/url?url={telegraph_link}")
            ],
            [InlineKeyboardButton("✗ Close ✗", callback_data="close")]
        ])
    )
