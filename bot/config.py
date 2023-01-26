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


import os
from dotenv import load_dotenv
from bot.translation import Translation
import logging
from bot.get_config import get_config
from logging.handlers import RotatingFileHandler

# apparently, no error appears even if the path does not exists
load_dotenv("config.env")



class Config:
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
    # required for running on Heroku
    URL = os.environ.get("URL", "")
    PORT = int(os.environ.get("PORT", 5000))
    # Python3 ReQuests CHUNK SIZE
    CHUNK_SIZE = 10280
    # MyTelegram.org
    # configurtion required while creating new application
    APP_TITLE = os.environ.get("APP_TITLE", "darmibot")
    APP_SHORT_NAME = os.environ.get("APP_SHORT_NAME", "darmibot")
    APP_URL = os.environ.get("APP_URL", "https://telegram.dog/darmibot")
    # these platform informations were obtained
    # on 27.01.2020 21:15:50 IST
    APP_PLATFORM = [
        "android",
        "ios",
        "wp",
        "bb",
        "desktop",
        "web",
        "ubp",
        "other"
    ]
    # if any of the platform, does not work
    # please reopen
    # https://github.com/SpEcHiDe/MyTelegramOrgRoBot/issues/3
    APP_DESCRIPTION = os.environ.get(
        "APP_DESCRIPTION",
        "created using https://telegram.dog/darmibot"
    )
    #
    FOOTER_TEXT = os.environ.get("FTEXT", "<b>Managed With ☕️ By @kenapatagdar</b>")
    # the strings used in the different messages
    # in the bot
    START_TEXT = os.environ.get("START_TEXT", Translation.START_TEXT)
    AFTER_RECVD_CODE_TEXT = os.environ.get(
        "AFTER_RECVD_CODE_TEXT",
        Translation.AFTER_RECVD_CODE_TEXT
    )
    BEFORE_SUCC_LOGIN = os.environ.get(
        "BEFORE_SUCC_LOGIN",
        Translation.BEFORE_SUCC_LOGIN
    )
    ERRED_PAGE = os.environ.get("ERRED_PAGE", Translation.ERRED_PAGE)
    CANCELLED_MESG = os.environ.get(
        "CANCELLED_MESG",
        Translation.CANCELLED_MESG
    )
    IN_VALID_CODE_PVDED = os.environ.get(
        "IN_VALID_CODE_PVDED",
        Translation.IN_VALID_CODE_PVDED
    )
    IN_VALID_PHNO_PVDED = os.environ.get(
        "IN_VALID_PHNO_PVDED",
        Translation.IN_VALID_PHNO_PVDED
    )
    
    
    
    # path to store LOG files
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "DarmiStringApi.log")
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
    # String
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
