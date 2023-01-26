#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" MtProto Bot """

from pyrogram import (
    Client,
    __version__,
    enums
)
from bot.config import (
    TG_BOT_TOKEN
)

from bot.helper_funcs.helper_steps import (
    api_id,
    api_hash
)


class Bot(Client):
    """ modded client for SessionMakerBot """

    def __init__(self):
        super().__init__(
            name="SessionMakerBot",
            api_hash=api_hash,
            api_id=api_id,
            bot_token=TG_BOT_TOKEN,
            plugins={
                "root": "bot/plugins"
            },
            workers=4,
            parse_mode=enums.ParseMode.HTML
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
            "Try /start."
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("SessionMakerBot stopped. Bye.")
