#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/damsyx/zetsumusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/damsyx/zetsumusic/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from ZetsuMusic import LOGGER, app, userbot
from ZetsuMusic.core.call import Zetsu
from ZetsuMusic.plugins import ALL_MODULES
from ZetsuMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("SurgaMusic").error(
            "Tidak Ada Asisten Klien yang Ditentukan Vars!.. Proses Keluar."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("SurgaMusic").warning(
            "Tidak ada Spotify Vars yang ditentukan.  Bot Anda tidak akan dapat memainkan kueri spotify."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ZetsuMusic.plugins" + all_module)
    LOGGER("ZetsuMusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Zetsu.start()
    Zetsu = await app.get_me()
    ZetsuMusic = zetsu.username
    await userbot.one.send_message("surgagrupbut", f"@{ZetsuMusic}")
    try:
        await Zetsu.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("SurgaMusic").error(
            "[ERROR] - \n\nHarap aktifkan Obrolan Suara Grup Logger Anda.  Pastikan Anda tidak pernah menutup/mengakhiri obrolan suara di grup log Anda"
        )
        sys.exit()
    except:
        pass
    await Surga.decorators()
    LOGGER("SurgaMusic").info("Surga Music Bot Started Successfully!")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("SurgaMusic").info("Stopping SurgaMusic! GoodBye")
