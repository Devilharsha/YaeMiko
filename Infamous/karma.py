# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/2f0ed932ee10772d5882b.jpg",
    "https://telegra.ph/file/0b0227c86d6c648618f21.jpg",
    "https://telegra.ph/file/82d3330826f44764b6368.jpg",
    "https://telegra.ph/file/72f60e13ff278d514baf4.jpg",
    "https://telegra.ph/file/6f771483587c03e491688.jpg",
    "https://telegra.ph/file/87dfc535c472259be717f.jpg",
]

HEY_IMG = "https://telegra.ph/file/67de513493b1b3af6871e.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/0a517502311d413d8a780.jpg",
    "https://telegra.ph/file/13d7f3408fef270863a9f.jpg",
    "https://telegra.ph/file/aab890f6b2d22904f6526.jpg",
    "https://telegra.ph/file/e9770f54a3c01c49dd515.jpg",
    "https://telegra.ph/file/aab890f6b2d22904f6526.jpg",
    "https://telegra.ph/file/e9770f54a3c01c49dd515.jpg",
    "https://telegra.ph/file/72f60e13ff278d514baf4.jpg",
    "",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "💥 ɪ ᴀᴍ ᴜᴄʜɪʜᴀ ᴍᴀᴅᴀʀᴀ, ᴀ ᴀɴɪᴍᴇ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ. 🚀"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="DEV", url="t.me/devilharsha_2153"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Doraemon_Telegram_Bots"),
        ib(text="SUPPORT", url="https://t.me/Doraemon_Bots_Chat"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *MADARA UCHIHA* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
