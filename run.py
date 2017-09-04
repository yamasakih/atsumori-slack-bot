# -*- coding: utf-8 -*-

from slackbot.bot import Bot
import os
import sys

VERSION = '0.0.1'


def main():
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    libdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    if os.path.exists(libdir):
        sys.path.insert(0, libdir)
    print('Run Atsumoriiiiiiiiiiii Bot Version %s' % VERSION)
    main()
