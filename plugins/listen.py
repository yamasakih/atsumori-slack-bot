# -*- coding: utf-8 -*-

from slackbot.bot import listen_to
import random


@listen_to('.*')
def listen_func(message):
    if random.random() < 0.05:
        message.react('atsumori')
        if random.random() < 0.8:
            message.send('失礼しました。熱盛と出てしまいました。')
        else:
            message.send('あっ…熱盛が出てしまい…ました失礼しました。')
