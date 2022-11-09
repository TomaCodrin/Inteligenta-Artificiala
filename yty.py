import pyautogui
import keyboard
import time

def cautare_google():
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_google.png', confidence=0.7) != None:
		camp_google=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_google.png', confidence=0.7)
		pyautogui.click(camp_google)
		time.sleep(3)
		pyautogui.write("https://www.youtube.com/c/ZonaitTvro")
		pyautogui.press('enter')
	else:
		print ("IMAGINEA NU SE AFLA PE ECRAN")
	time.sleep(5)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_subscribe.png', confidence=0.7) != None:
		camp_subscribe=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_subscribe.png', confidence=0.7)
		pyautogui.click(camp_subscribe)
		time.sleep(3)
	else:
		print ("IMAGINEA NU SE AFLA PE ECRAN")

time.sleep(2)
cautare_google()