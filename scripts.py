import win32api
import win32con
import keyboard
import time
import random
import mouse

class Scripts:
	""" FAST MINING MACROS"""
	def fastfarm(self, pickaxe_key, grenade_key):
		keyboard.send(grenade_key)
		time.sleep(0.04)
		keyboard.send(pickaxe_key)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
		time.sleep(0.35) # this delay actually depends on ping
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)


	""" RECOIL CONTROL MACROS"""
	def recoil_control(self, recoil_method):
		"""
		1st method - stable
		2nd method - unstable
		"""
		if recoil_method == 1:
			time.sleep(0.35)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
		elif recoil_method == 2:
			win32api.mouse_event(0x0001, 0, random.randint(1, 2))
