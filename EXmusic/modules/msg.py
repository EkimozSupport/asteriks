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

import os
from EXmusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      HELP_MSG = [
        ".",
f"""
Merhabalar tekrar hoş geldiniz. EXMusic
• EXMusic, sesli sohbet gruplarında ve kanalınızda kolayca şarkı çalabilir.
• Assistant Müzik » @TaliaMusicasistant «\n 
""",

f"""
**Ayarlar ✳️**

1. Botu yönetici yapma 
2. Sesli sohbeti başlatma /VCG 
3. Tür `/userbotjoin` ve deneyin /play <nama lagu>
× Assistant Bot katılırsa müziğin tadını çıkarın, 
× Yardımcı botlar katılmazsa lütfen @{ASSISTANT_NAME} Grubunuza gidin ve yeniden deneyin.

**» Üye Gruplarındaki Komutlar:**
/playlist : Untuk Menampilkan daftar putar Lagu sekarang
/current : Untuk Menunjukkan  Lagu sekarang yang sedang diputar
/song <judul lagu> : Untuk Mendownload lagu di YouTube 
/video <judul lagu> : Untuk Mendownload Video di YouTube dengan detail
/vsong <judul lagu> : Untuk Mendownload Video di YouTube dengan detail
/deezer <judul lagu> : Untuk Mendownload lagu dari deezer 
/saavn <judul lagu> : Untuk Mendownload lagu dari website saavn
/search <judul lagu> : Untuk Mencari Video di YouTube dengan detail

**» Yalnızca Yönetici için Komut:**
/play <judul lagu> : Untuk Memutar lagu yang Anda minta melalui youtube
/play <link yt> : Untuk Memutar lagu yang Anda minta melalui link youtube
/play <reply ke audio> : Untuk Memutar lagu yang Anda minta melalui file audio
/dplay : Untuk Memutar lagu yang Anda minta melalui deezer
/splay : Untuk Memutar lagu yang Anda minta melalui jio saavn
/skip : Untuk Menskip pemutaran lagu ke Lagu berikutnya
/pause : Untuk Menjeda pemutaran Lagu
/resume : Untuk Melanjutkan pemutaran Lagu yang di pause
/end : Untuk Memberhentikan pemutaran Lagu
/userbotjoin - Untuk Mengundang asisten ke obrolan Anda
/admincache - Untuk MemRefresh admin list

**» kanal akışı komutları:**
/cplay - streaming musik di obrolan suara channel
/cplayer - tampilkan lagu di streaming
/cpause - jeda musik streaming
/cresume - lanjutkan streaming yang dijeda
/cskip - lewati streaming ke lagu berikutnya
/cend - akhiri streaming musik

**» eğlence için komutlar:**
/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself
"""
      ]
