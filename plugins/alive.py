import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4963e9019e0328075e980.jpg",
        caption=f"""**👋🏻 ʜᴇʟʟᴏ {message.from_user.mention()} ɪᴀᴍ ᴀ ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ᴡɪᴛʜ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ

ɢʀᴏᴜᴘs ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.. ᴀɴʏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀɴᴛ ʜɪᴛ ᴛʜᴇ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ /help..

ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters)**
""",
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ & ʜᴇʟᴘ", callback_data="command_list"), 
            ],[
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/tgshadow_fighters"), 
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/teamshadowprojects"), 
            ],[
            InlineKeyboardButton("✚ ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚", url=f"https://t.me/Amalamusicbot?startgroup=true")
            ]]
            ) 
        ) 
     
    
@Client.on_message(commandpro(["/alive"]) & filters.group & ~filters.edited)
async def alive(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4963e9019e0328075e980.jpg",
        caption=f"""ʜᴇʟʟᴏ {message.from_user.mention()} ɪᴀᴍ ᴀʟɪᴠᴇ ɴᴏᴡ 👻""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="info")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["/repo",]) & filters.group & ~filters.edited)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4963e9019e0328075e980.jpg",
        caption=f"""ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ 🙊""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ", callback_data="source")
                ]
            ]
        ),
    )


@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4963e9019e0328075e980.jpg",
        caption=f""" ✨ **ʜᴇʟʟᴏ {message.from_user.mention()} !**\n
💘 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sᴇᴛᴜᴘ ᴛʜɪs ʙᴏᴛ? ʀᴇᴀᴅ 💖 sᴇᴛᴛɪɴɢ ᴜᴘ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ **\n
💗 **ᴛᴏ ᴋɴᴏᴡ ᴘʟᴀʏ /ᴀᴜᴅɪᴏ? ʀᴇᴀᴅ 💖 ǫᴜɪᴄᴋ ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅs **\n
💝 **ᴛᴏ ᴋɴᴏᴡ ᴇᴠᴇʀʏ sɪɴɢʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏғ ʙᴏᴛ? ʀᴇᴀᴅ 💖 ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs**\n """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_message(command("ghelp") & filters.group & ~filters.edited)
async def gelp(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4963e9019e0328075e980.jpg",
        caption=f""" ✨ **ʜᴇʟʟᴏ {message.from_user.mention()} !**\n
💘 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sᴇᴛᴜᴘ ᴛʜɪs ʙᴏᴛ? ʀᴇᴀᴅ 💖 sᴇᴛᴛɪɴɢ ᴜᴘ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ **\n
💗 **ᴛᴏ ᴋɴᴏᴡ ᴘʟᴀʏ /ᴀᴜᴅɪᴏ? ʀᴇᴀᴅ 💖 ǫᴜɪᴄᴋ ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅs **\n
💝 **ᴛᴏ ᴋɴᴏᴡ ᴇᴠᴇʀʏ sɪɴɢʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏғ ʙᴏᴛ? ʀᴇᴀᴅ 💖 ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs**\n """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_message(command("uptime") & filters.group & ~filters.edited)
async def get_uptime(c: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4963e9019e0328075e980.jpg", 
        caption="💞 ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ʙᴏᴛ sᴛᴀᴛᴜs:\n"
                f"• **ᴜᴘᴛɪᴍᴇ:** **{uptime}**\n"
                f"• **ᴜsᴇʀ:** **{message.from_user.mention()}**\n"
                f"• **sᴛᴀʀᴛ ᴛɪᴍᴇ:** **{START_TIME_ISO}**\n"
                f"• **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** **@tgshadow_fighters**"
              ) 


@Client.on_message(command("ping") & filters.group & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text("💝 `ᴘᴏɴɢ!!`\n" f"💖 `{delta_ping * 1000:.3f} ms`")
