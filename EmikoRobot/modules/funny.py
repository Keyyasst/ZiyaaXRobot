import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot



@register(pattern=("/memek"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), RAIMU KOYOK KONTOL.** \n\n"
  TEXT = f"**NGOPO LENG?,RA TERIMO??
  BUTTON = [[Button.url("Help", "https://t.me/amanqss?start=help"), Button.url("KONTOL", "https://xnxx.com)]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
