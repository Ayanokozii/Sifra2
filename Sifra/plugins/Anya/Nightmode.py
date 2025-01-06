import random
from pyrogram import filters, Client, enums
from Sifra import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ChatPermissions
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from Sifra.utils.Databases.nightmodedb import nightdb, nightmode_on, nightmode_off, get_nightchats
import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# Permissions to close the chat
CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_other_messages=False,
    can_send_polls=False,
    can_change_info=False,
    can_add_web_page_previews=False,
    can_pin_messages=False,
    can_invite_users=False
)

# Permissions to open the chat
OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_send_polls=True,
    can_change_info=True,
    can_add_web_page_previews=True,
    can_pin_messages=True,
    can_invite_users=True
)

# Buttons for enabling/disabling night mode
buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("๏ ᴇɴᴀʙʟᴇ ๏", callback_data="add_night"),
        InlineKeyboardButton("๏ ᴅɪsᴀʙʟᴇ ๏", callback_data="rm_night")
    ]
])

# Command to manage night mode
@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/e10f3ce39e10948e20a1c.jpg",
        caption="**ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ɴɪɢʜᴛᴍᴏᴅᴇ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**",
        reply_markup=buttons
    )

# Callback query handler for night mode
@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query: CallbackQuery):
    data = query.data
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id": chat_id})

    administrators = [m.user.id for m in await app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]

    if user_id in administrators:
        if data == "add_night":
            if check_night:
                await query.message.edit_caption("**๏ ɴɪɢʜᴛᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**")
            else:
                await nightmode_on(chat_id)
                await query.message.edit_caption("**๏ ᴀᴅᴅᴇᴅ ᴄʜᴀᴛ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ. ᴛʜɪs ɢʀᴏᴜᴘ ᴡɪʟʟ ʙᴇ ᴄʟᴏsᴇᴅ ᴏɴ 𝟷𝟸ᴀᴍ [IST] ᴀɴᴅ ᴡɪʟʟ ᴏᴘᴇɴ ᴏɴ 𝟶𝟼ᴀᴍ [IST].**")
        elif data == "rm_night":
            if check_night:
                await nightmode_off(chat_id)
                await query.message.edit_caption("**๏ ɴɪɢʜᴛᴍᴏᴅᴇ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ!**")
            else:
                await query.message.edit_caption("**๏ ɴɪɢʜᴛᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**")

# Function to start night mode
async def start_nightmode():
    schats = await get_nightchats()
    chats = [int(chat["chat_id"]) for chat in schats]

    for add_chat in chats:
        try:
            await app.send_photo(
                add_chat,
                photo="https://te.legra.ph/file/e10f3ce39e10948e20a1c.jpg",
                caption="**ᴍᴀʏ ᴛʜᴇ ᴀɴɢᴇʟs ғʀᴏᴍ ʜᴇᴀᴠᴇɴ ʙʀɪɴɢ ᴛʜᴇ sᴡᴇᴇᴛᴇsᴛ ᴏғ ᴀʟʟ ᴅʀᴇᴀᴍs ғᴏʀ ʏᴏᴜ. ɢʀᴏᴜᴘ ɪs ᴄʟᴏsɪɴɢ ɢᴏᴏᴅ ɴɪɢʜᴛ ᴇᴠᴇʀʏᴏɴᴇ!**"
            )
            await app.set_chat_permissions(add_chat, CLOSE_CHAT)
        except Exception as e:
            LOGGER.error(f"Unable to close group {add_chat} - {e}")

# Scheduler to start night mode
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.start()

# Function to close night mode
async def close_nightmode():
    schats = await get_nightchats()
    chats = [int(chat["chat_id"]) for chat in schats]

    for rm_chat in chats:
        try:
            await app.send_photo(
                rm_chat,
                photo="https://telegra.ph/file/14ec9c3ff42b59867040a.jpg",
                caption="**ɢʀᴏᴜᴘ ɪs ᴏᴘᴇɴɪɴɢ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴇᴠᴇʀʏᴏɴᴇ!**"
            )
            await app.set_chat_permissions(rm_chat, OPEN_CHAT)
        except Exception as e:
            LOGGER.error(f"Unable to open group {rm_chat} - {e}")

# Scheduler to close night mode
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1)
scheduler.start()

