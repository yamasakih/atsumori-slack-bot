# -*- coding: utf-8 -*-

import random

from slackbot.bot import listen_to
from plugins.parameters import EMOJI_NAME, ATSUMORI_PROBABILITY, NORMAL_PROBABILITY


@listen_to('.*')
def listen_func(message):
    if random.random() < ATSUMORI_PROBABILITY:
        message.react(EMOJI_NAME)
        if random.random() < NORMAL_PROBABILITY:
            message.send('失礼しました。熱盛と出てしまいました。')
        else:
            message.send('あっ…熱盛が出てしまい…ました失礼しました。')
