from scripts import Scripts
from misc import Misc
import time
import keyboard
import winsound
import win32api
import mouse


""" 
	Python-Macro for fortnite
	Features: Fast-Mining, Accuracy Recoil Control
	Author: fdnflm ex FadinFlame ex YourPollution
"""


""" BINDS """
key_grenade = "five" # *throwable weapon, this is really important
key_pickaxe = "f"
key_fastfarm = "alt" 
key_recoil_activation = 0x71 # F2, Set your own if you want. Like: 0x + key. Virtual key codes - https://api.farmanager.com/ru/winapi/virtualkeycodes.html
key_recoil = "]"
recoil_method = 1  # 1 - stable, 2 - unstable


script_version = "1.4"
misc = Misc()
scripts = Scripts()


def logo():
	print("""\
  ____                  __  __                      
 |  _ \ _   _          |  \/  | __ _  ___ _ __ ___  
 | |_) | | | |  _____  | |\/| |/ _` |/ __| '__/ _ \ 
 |  __/| |_| | |_____| | |  | | (_| | (__| | | (_) |
 |_|    \__, |         |_|  |_|\__,_|\___|_|  \___/ 
	|___/                                       
					""")


def general():
	logo()
	print("Checking for updates...")
	print(misc.check_for_updates(script_version))
	print("Getting macro status...")
	print(f"Status: {misc.get_status()}")
	print("\n\nBinds:")
	print("Key grenade slot:", key_grenade)
	print("Key pickaxe slot:", key_pickaxe)
	print("Key fastfarm:", key_fastfarm)
	print("Key recoil:", key_recoil)


def start():          
	recoil_status = False 
	if not misc.check_path():                         ###    Super mega Battle-Eye & EAC bypass   ###
		exit(0)                                                    
	win32api.SetConsoleTitle(misc.generate_random())  ###                                         ###
	general()


	while True:  # main loop
		if keyboard.is_pressed(key_fastfarm):
			scripts.fastfarm(key_pickaxe, key_grenade)


		if win32api.GetAsyncKeyState(key_recoil_activation) and 0x80000:
			recoil_status = not recoil_status
			winsound.Beep(600, 700)
		

		if recoil_status:
			if recoil_method == 1:
				if keyboard.is_pressed(key_recoil):
					scripts.recoil_control(recoil_method=1)
			elif recoil_method == 2:
				while mouse.is_pressed(button="left"):
					scripts.recoil_control(recoil_method=2)
					time.sleep(0.1)


start()