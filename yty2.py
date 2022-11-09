import pyautogui
import keyboard
import time


def cautare_google():
	i=1
	x=600
	y=300
	z=-450
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_google.png', confidence=0.7) != None:
		camp_google=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_google.png', confidence=0.7)
		pyautogui.click(camp_google)
		time.sleep(3)
		pyautogui.write("https://www.youtube.com/c/ZonaitTvro")
		pyautogui.press('enter')
	else:
		print ("IMAGINEA NU SE AFLA PE ECRAN")
	time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7) != None:
		camp_video=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7)
		pyautogui.click(camp_video)
	else:
		print ("IMAGINEA NU SE AFLA PE ECRAN")
	time.sleep(3)
	while not keyboard.is_pressed('esc'):
		pyautogui.scroll(z)
		while (i>0):
			if (i%5==1):
				pyautogui.moveTo(x, y)
				time.sleep(1)
				pyautogui.click()
				time.sleep(2)
			else:
				pyautogui.scroll(z)
				time.sleep(1)
				pyautogui.moveTo(x, y)
				time.sleep(1)
				x=x+300
				time.sleep(1)
				pyautogui.click()
				time.sleep(2)
			if (i%5==0):
				x=600
				z=z-300
			if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_canal.png', confidence=0.7) != None:
				camp_canal=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_canal.png', confidence=0.7)
				pyautogui.click(camp_canal)
				time.sleep(3)
			if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7) != None:
				camp_video=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7)
				pyautogui.click(camp_video)
			i+=1

			
time.sleep(2)
cautare_google()