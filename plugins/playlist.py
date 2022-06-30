from modules.config import BOT_USERNAME
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from pyrogram import Client

from modules.helpers.decorators import authorized_users_only
from modules.clientbot.queues import queues, put
from modules.helpers.filters import command, other_filters
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream



keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 ʙɪɴ", callback_data="set_close")]]
)


@Client.on_message(command(["playlist", f"playlist@{BOT_USERNAME}", "queue", f"queue@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def playlist(client, m: Message):
    chat_id = m.chat.id
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        if len(chat_id) == 1:
            await m.reply(
                f"🔰 **ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ**`:`\n\n" \
                f"🔥 **[{queues[chat_id][0][0]}]({queues[chat_id][0][2]})**\n\n" \
                f"**📱 ǫᴜᴇᴜᴇ sᴏɴɢ ʟɪsᴛ**`:`\n"
         l = len(chat_queue)
         for x in range (1, l):
            for x in range(1, l):
                han = queues[chat_id][x][0]
                hok = queues[chat_id][x][2]
                hap = queues[chat_id][x][3]
                QUE = QUE + "\n" + f"`#{x}` - [{han}]({hok}) | `{hap}`"
            await m.reply(QUE, reply_markup=keyboard, disable_web_page_preview=True)
    else:
        await m.reply("❌ **ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ.**")
            ) 
