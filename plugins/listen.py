# -*- coding: utf-8 -*-

from slackbot.bot import listen_to
import random


@listen_to('.*')
def listen_func(message):
    message.react('atsumori')
    if random.random() < 0.05:
        if random.random() < 0.5:
            message.send('失礼しました。熱盛と出てしまいました。')
        else:
            message.send('あっ…熱盛が出てしまい…ました失礼しました。')
