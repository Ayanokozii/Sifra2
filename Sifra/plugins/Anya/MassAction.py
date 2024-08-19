from Sifra import app
from config import OWNER_ID
from pyrogram import filters, enums
from Sifra.utils.admin_check import admin_filter
from Sifra.misc import SUDOERS

BOT_ID = app.me.id

async def check_bot_permissions(chat_id):
    bot = await app.get_chat_member(chat_id, BOT_ID)
    return bot.privileges.can_restrict_members

@app.on_message(filters.command("banall") & SUDOERS)
async def ban_all(_, msg):
    chat_id = msg.chat.id    
    if await check_bot_permissions(chat_id):
        async for member in app.get_chat_members(chat_id):
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                print(f"Banned: {member.user.mention}")
            except Exception as e:
                print(f"Failed to ban {member.user.mention}: {e}")
    else:
        print("I don't have the right to restrict users or you're not in SUDOERS.")

@app.on_message(filters.command("unbanall") & admin_filter)
async def unban_all(_, msg):
    chat_id = msg.chat.id
    if await check_bot_permissions(chat_id):
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
            try:
                await app.unban_chat_member(chat_id, m.user.id)
                print(f"Unbanned: {m.user.mention}")
            except Exception as e:
                print(f"Failed to unban {m.user.mention}: {e}")
    else:
        print("I don't have the right to unban users or you're not an admin.")

@app.on_callback_query(filters.regex("^stop$"))
async def stop_callback(_, query):
    await query.message.delete()
