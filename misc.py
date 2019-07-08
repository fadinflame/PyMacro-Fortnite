import random
import string
import random
import ctypes
import os
import requests


class Misc:
	def generate_random(self):
		return "".join(random.choice(string.ascii_letters + string.digits) for i in range(18))


	def get_status(self):
		result = requests.get("https://site.com/status?app=pymacro") # here was my website
		if result.text == "0":
			return "Use at own your risk"
		elif result.text == "1":
			return "Undetected"
		elif result.text == "2":
			self.show_message("This version of macro has been detected. We don't recommend you to use it.", "Warning")
			exit(0)


	def check_for_updates(self, version):
		result = requests.get("https://site.com/update?app=pymacro") # here was my website
		if result.text == version:
			return "You are using the latest version"
		else:
			self.show_message("A new version is available on github", "Info")
			exit(0)


	def show_message(self, text, title):
		ctypes.windll.user32.MessageBoxW(0, text, title, 0)


	def check_path(self):
		suspect = ["cheat", "hack", "macro", "fortnite", "Py-Macro", "pymacro"]
		path = os.path.realpath(__file__)
		for name in suspect:
			if name.lower() in path.lower():
				self.show_message("Please change the folder name", "Warning")
				return False
		return True

