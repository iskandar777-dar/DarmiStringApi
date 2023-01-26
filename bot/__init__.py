#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Darmi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Telegram Bot"""


from .config import Config  # noqa: F401


INPUT_PHONE_NUMBER, \
    INPUT_TG_CODE = range(2)
GLOBAL_USERS_DICTIONARY = {}

""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from bot.get_config import get_config

# apparently, no error appears even if the path does not exists
load_dotenv("config.env")

# The Telegram API things
# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = get_config("APP_ID", should_prompt=True)
# get a token from @BotFather
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)

# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
#
COMMM_AND_PRE_FIX = get_config("COMMM_AND_PRE_FIX", "/")
# start command
START_COMMAND = get_config("START_COMMAND", "start")
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "SessionMakerBot.log")


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)


# a dictionary to store the currently running processes
AKTIFPERINTAH = {}
# /start message when other users start your bot
START_OTHER_USERS_TEXT = get_config(
    "START_OTHER_USERS_TEXT",
    (
        "Halo Jomblo! ..."
    )
)
INPUT_PHONE_NUMBER = get_config("INPUT_PHONE_NUMBER", (
    "Masukan No Telenya yaa contoh : +628214xxxxx .\n"
))
RECVD_PHONE_NUMBER_DBP = get_config("RECVD_PHONE_NUMBER_DBP", (
    "Mengecek no Hp, Sabar Yee\n"
))
ALREADY_REGISTERED_PHONE = get_config("ALREADY_REGISTERED_PHONE", (
    "Kirim kodenya bre."
))
CONFIRM_SENT_VIA = get_config("CONFIRM_SENT_VIA", (
    "Konfirmasi kode dikirim via {}"
))
RECVD_PHONE_CODE = get_config("RECVD_PHONE_CODE", (
    "Mengecek code, Sabar Yee"
))
NOT_REGISTERED_PHONE = get_config("NOT_REGISTERED_PHONE", (
    "No hp lu ngga kedaftar tele mblo"
))
PHONE_CODE_IN_VALID_ERR_TEXT = get_config(
    "Code ngga valid nih, silahkan klik /start untuk mengulang mblo"
)
TFA_CODE_IN_VALID_ERR_TEXT = get_config(
    "Pwnya salah mblo, silahkan klik /start untuk mengulang"
)
ACC_PROK_WITH_TFA = get_config("ACC_PROK_WITH_TFA", (
    "ada pwnya inimah, isi pwnya bre"
))
SESSION_GENERATED_USING = get_config("SESSION_GENERATED_USING", (
    "Nih udah jadi  👆👆👆"
))