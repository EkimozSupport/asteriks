# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from EXmusic.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from EXmusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME, OWNER, BOT_NAME
logging.basicConfig(level=logging.INFO)
from EXmusic.helpers.filters import command
from pyrogram import Client, filters
from time import time
from datetime import datetime
from EXmusic.helpers.decorators import authorized_users_only


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

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋 **Merhaba** {message.from_user.first_name}**\n
⚡ **[Hatıralar Music](https://t.me/Sancakailesi) Müzik, yeni Telegram'ın Sesli Sohbetleri aracılığıyla gruplarda müzik çalmanıza olanak sağlar!**

💡 **Botun tüm komutlarını ve nasıl çalıştıklarını öğrenin.» 📚 Komutlar düğmesi.**

❓ **Botlar hakkında genel bilgi için, daha fazla** /help
<b>""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Beni grubunuza ekleyin ➕", url=f"https://t.me/HatiralaraMusicBot?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "📣 Resmi group", url=f"https://t.me/SancakAilesi"), 
                    InlineKeyboardButton(
                        "👥 Destek Grubu", url=f"https://t.me/MangoDestek")
                ],[
                    InlineKeyboardButton(
                        "⚡ Oluşturan", url=f"https://t.me/kizilsancakailesi")
                ],[
                    InlineKeyboardButton(
                        "📚 Müzik group", url=f"https://t.me/Smailesi")
                ],[
                    InlineKeyboardButton(
                        "🛠️ Kaynak kodu", url=f"https://t.me/kizilsancaksahibi")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'ɴᴇxᴛ »', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/kizilsancakbilgi"
        button = [
            [InlineKeyboardButton("➕ Beni grubunuza ekleyin ➕", url=f"https://t.me/HatiralaraMusicBot?startgroup=true")],
            [InlineKeyboardButton(text = '📣 Resmi kanal', url=f"https://t.me/kizilsancakbilgi"),
             InlineKeyboardButton(text = '👥 Support Group', url=f"https://t.me/Sancakailesi")],
            [InlineKeyboardButton(text = '🌻 Developer', url=f"https://t.me/kizilsancaksahibi")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '«', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '»', callback_data = f"help+{pos+1}")
            ],
        ]
    return button


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**YouTube bağlantısı bulmak istiyor musunuz.?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Evet", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Kapat", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """Aşağıdaki bot kılavuzunu okuyun""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Bot yapımı için", url="https://t.me/ucretlibotlar"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **başarıyla yeniden başlatıldı!**\n\n• **Yöneticilerin listesi** zaten **Güncelleştirilmiş**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url=f"https://t.me/Sancakailesi"
                    ),
                    InlineKeyboardButton(
                        "ᴄʀᴇᴀᴛᴇᴅ ʙʏ", url=f"https://t.me/Kizilsancak"
                    )
                ]
            ]
        )
   )

@Client.on_message(command(["ping", f"ping@Efsanestar_bot"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("Ping...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🏓 `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@Hatiralaramusicbot"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• 🚀 **Uptime:** `{uptime}`\n"
        f"• ⚡ **start time:** `{START_TIME_ISO}`"
    )
