from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from modules.config import (
    BOT_USERNAME,
)

@Client.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def assistant(client, message: Message):
  await Client.send_message(message.chat.id,"Hey 👋 I am the assistant of music bot, didn't have a time to talk with you 🙂 kindly join @TgShadow_fighter for getting support\n\nPowered by @TgShadow_fighter")
  return
