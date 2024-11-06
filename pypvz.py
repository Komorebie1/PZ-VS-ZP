#!/usr/bin/env python
import logging
import traceback
import os
import pygame as pg
from logging.handlers import RotatingFileHandler
# 由于在后续本地模块中存在对pygame的调用，在此处必须完成pygame的初始化
os.environ["SDL_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR"]="0" # 设置临时环境变量以避免Linux下禁用x11合成器
pg.init()
from source import tool
from source import constants as c
from source.state import mainmenu, screen, level, multiplayer
import socket

if __name__ == "__main__":
    hostname = socket.gethostname()
    ipv4_address = socket.gethostbyname(hostname)
    game = tool.Control()
    state_dict = {  
                    c.MAIN_MENU:    mainmenu.Menu(),
                    # c.GAME_VICTORY: screen.GameVictoryScreen(),
                    # c.GAME_LOSE:    screen.GameLoseScreen(),
                    c.LEVEL:        level.Level(),
                    c.MULTIPLAYER:        multiplayer.Level(False, ipv4_address),
                    c.HOST:        multiplayer.Level(True, ipv4_address),
                    # c.AWARD_SCREEN: screen.AwardScreen(),
                    # c.HELP_SCREEN:  screen.HelpScreen(),
                }
    game.setup_states(state_dict, c.MAIN_MENU)
    game.run()
