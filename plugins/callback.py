from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from modules.utils.lang import *             

menu_keyboard = InlineKeyboardMarkup(
    [
        [
            
            InlineKeyboardButton("▷", callback_data="resume_vc"),
            InlineKeyboardButton("II", callback_data="pause_vc"),
            ],[
            InlineKeyboardButton("‣‣I", callback_data="skip_vc"),
            InlineKeyboardButton("▢", callback_data="stop_vc"),
            ],[
            InlineKeyboardButton("🗑 ʙɪɴ", callback_data="set_close"), 
        ], 
     ]
 ) 
    


@Client.on_callback_query(filters.regex("home_start"))
@languageCB
async def start_set(query: CallbackQuery):
    await query.edit_message_text(
        f"""👋🏻 **ʜᴇʟʟᴏ {query.message.from_user.mention()} ɪᴀᴍ ᴀ ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ᴍᴜsɪᴄ ʙᴏᴛ ɪᴀᴍ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ.. 

ɢʀᴏᴜᴘs ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.. ᴀɴʏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀɴᴛ ʜɪᴛ ᴛʜᴇ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ /help..

ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters) !**
""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(_["S_B_1"], callback_data="command_list"), 
            ],[
            InlineKeyboardButton(_["S_B_2"], url="https://t.me/tgshadow_fighters"), 
            InlineKeyboardButton(_["S_B_3"], callback_data="_langs"), 
            ],[
            InlineKeyboardButton(_["S_B_4"], url=f"https://t.me/Amalamusicbot?startgroup=true")
            ]]
            ) 
        )    
     

@Client.on_callback_query(filters.regex("command_list"))
@languageCB
async def commands_set(query: CallbackQuery):
    await query.answer("ᴏᴘᴇɴɪɴɢ ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ", show_alert=True) 
    await query.edit_message_text(
        f"""💗 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 
➠ ʜᴇʟʟᴏ ɴᴀᴍsᴛʜᴇ ᴀɴɴᴀ ᴛʜɪs ɪs ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ɢᴜɪᴅᴇ ᴡʜᴀᴛ ᴄᴏᴍᴍᴀɴᴅ ʏᴏᴜ ɴᴇᴅᴅ sᴇʟᴇᴄᴛ ʜᴇʀᴇ.. 

➠ ᴛʜɪs ʙᴏᴛ ᴍᴀᴅᴇ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters) 
""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅs", callback_data="general_list"), 
            ],[
            InlineKeyboardButton("sᴋɪᴘ", callback_data="skip_list"), 
            InlineKeyboardButton("ᴘᴀᴜsᴇ", callback_data="pause_list"), 
            ],[
            InlineKeyboardButton("ʀᴇsᴜᴍᴇ", callback_data="resume_list"), 
            InlineKeyboardButton("sᴛᴏᴘ", callback_data="stop_list"), 
            ],[
            InlineKeyboardButton("ᴘʟᴀʏ", callback_data="play_list"), 
            InlineKeyboardButton("sᴏᴜʀᴄᴇ", callback_data="source"), 
            ],[
            InlineKeyboardButton("◁", callback_data="home_start"), 
            ]]
            ) 
        ) 
    

@Client.on_callback_query(filters.regex("general_list"))
@languageCB
async def general_list(query: CallbackQuery):
    await query.answer("ᴏᴘᴇɴɪɴɢ ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅs", show_alert=True)
    await query.edit_message_text(
        f"""🥳 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ /play (sᴏɴɢ ɴᴀᴍᴇ/ʟɪɴᴋ) - ᴘʟᴀʏ ᴍᴜsɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ
➠ /song (ǫᴜᴇʀʏ) - ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
➠ /search (ǫᴜᴇʀʏ) - sᴇᴀʀᴄʜ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ
➠ /ping - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛᴜs
➠ /uptime - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ sᴛᴀᴛᴜs
➠ /alive - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴғᴏ (ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ)
➠ /help - ᴛᴏ sʜᴏᴡ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ (ғᴜʟʟ ʙᴏᴛ ɢᴜɪᴅᴇ)
⚡️ __ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs ᴀɪ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("skip_list"))
@languageCB
async def skip_list(query: CallbackQuery):
    await query.answer("skiped current song")
    await query.edit_message_text(
        f"""🚩 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/skip ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ sᴋɪᴘ ᴛᴏ ɴᴇxᴛ sᴏɴɢ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/teamshadowprojects)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("pause_list"))
async def pause_list(query: CallbackQuery):
    await query.answer("pause current playing song")
    await query.edit_message_text(
        f"""💘 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/pause ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ ɪɴ ɢʀᴏᴜᴘ/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("resume_list")) 
async def resume_list(query: CallbackQuery):
    await query.answer("resume current playing song")
    await query.edit_message_text(
        f"""❤ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/resume ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ʀᴇsᴜᴍᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/Team_shadowmusic_bot)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("stop_list"))
async def stop_list(query: CallbackQuery):
    await query.answer("stopping current playing song")
    await query.edit_message_text(
        f"""💓 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/end ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ᴇɴᴅ sᴏɴɢs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("play_list"))
async def play_list(query: CallbackQuery):
    await query.answer("playing song in vc")
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/play ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴘʟᴀʏ ᴀ sᴏɴɢs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("source"))
async def source(query: CallbackQuery):
    await query.answer("team shadow source code")
    await query.edit_message_text(
        f"""❣️ **ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
➠  **sʜᴀᴅᴏᴡ ᴍᴜsɪᴄ ʙᴏᴛ ɪs ᴄᴏᴍᴘʟᴇᴛᴇ ᴄʟᴏsᴇᴅ sᴏᴜʀᴄᴇ ʀᴇᴘᴏʀᴛɪɴɢ ᴀɴʏ ʙᴜɢs ᴏʀ ʀᴇᴘᴏʀᴛs ᴄᴏɴᴛᴀᴄᴛ ᴅᴇᴠ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters)!**""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("info"))
async def info(query: CallbackQuery):
    await query.answer("information")
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

💘 ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ɪs ᴀ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ɪɴ sᴏ ᴍᴀɴʏ sᴇʀᴠᴇʀ's, ɪᴛ's ᴏɴʟɪɴᴇ sɪɴᴄᴇ 𝟷sᴛ ᴊᴜɴᴇ 𝟸𝟶𝟸𝟸 ᴀɴᴅ ɪᴛ's ᴄᴏɴsᴛᴀɴᴛʟʏ ᴜᴘᴅᴀᴛᴇᴅ \n
💝 ᴛʜɪs ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters) \n 
❣️ © ᴏɴ ʙᴇʜᴀʟғ ᴏғ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters)
""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="home_start")]]
        ),
    ) 


@Client.on_callback_query(filters.regex("set_close"))
async def on_close_menu(query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !", show_alert=True)
    await query.message.delete()

@Client.on_callback_query(filters.regex("close_panel"))
async def in_close_panel(query: CallbackQuery):
    await query.message.delete()

@Client.on_callback_query(filters.regex("menu")) 
async def menu(query: CallbackQuery):
    user_id = query.from_user.id
    await query.edit_message_text(
        text=f"""ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs""",
        disable_web_page_preview=True, 
        reply_markup=menu_keyboard
    ) 
