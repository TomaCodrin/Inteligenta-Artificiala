import pyautogui
import keyboard
import time
	
def chrome():
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\chrome.png', confidence=0.7) != None:
		camp_chrome=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\chrome.png', confidence=0.7)
		pyautogui.doubleClick(camp_chrome)
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\maximize.png', confidence=0.7) != None:
		camp_maximize=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\maximize.png', confidence=0.7)
		pyautogui.click(camp_maximize)
		time.sleep(1)
	pyautogui.click()
	time.sleep(1)
def youtube():
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_google.png', confidence=0.7) != None:
		camp_google=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_google.png', confidence=0.7)
		pyautogui.click(camp_google)
		time.sleep(3)
		pyautogui.write("https://www.youtube.com/")
		pyautogui.press('enter')
	else:
		print ("IMAGINEA NU SE AFLA PE ECRAN")
	time.sleep(5)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\sign_in.png', confidence=0.7) != None:
		camp_signin=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\sign_in.png', confidence=0.7)
		pyautogui.click(camp_signin)
		time.sleep(3)
		pyautogui.write("addicted92121@gmail.com")
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\next.png', confidence=0.7) != None:
		camp_next=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\next.png', confidence=0.7)
		pyautogui.click(camp_next)
		time.sleep(3)
		pyautogui.write("PIKIkod07")
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\next.png', confidence=0.7) != None:
		camp_next=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\next.png', confidence=0.7)
		pyautogui.click(camp_next)
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\new_tab.png', confidence=0.7) != None:
		camp_newtab=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\new_tab.png', confidence=0.7)
		pyautogui.click(camp_newtab)
		time.sleep(3)	
	time.sleep(1)
def cautare_google():
	i=1
	x=600
	y=300
	z=-450
	pyautogui.write("https://www.youtube.com/c/ZonaitTvro")
	pyautogui.press('enter')
	time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_subscribe.png', confidence=0.7) != None:
		camp_subscribe=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_subscribe.png', confidence=0.7)
		pyautogui.click(camp_subscribe)
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7) != None:
		camp_video=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7)
		pyautogui.click(camp_video)
	time.sleep(2)
	while not keyboard.is_pressed('esc'):
		pyautogui.scroll(z)
		while (i>0):
			if (i%5==1):
				pyautogui.moveTo(x, y)
				time.sleep(2)
				pyautogui.click()
				time.sleep(2)
			else:
				pyautogui.scroll(z)
				time.sleep(2)
				pyautogui.moveTo(x, y)
				time.sleep(2)
				x=x+300
				time.sleep(2)
				pyautogui.click()
				time.sleep(2)
			if (i%5==0):
				x=600
				z=z-300
			if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\like.png', confidence=0.7) != None:
				camp_like=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\like.png', confidence=0.7)
				pyautogui.click(camp_like)
				time.sleep(3)
				pyautogui.scroll(-350)
				time.sleep(3)
			if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\comment.png', confidence=0.7) != None:
				camp_comment=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\comment.png', confidence=0.7)
				pyautogui.click(camp_comment)
				time.sleep(3)
				pyautogui.write("awsome")
				time.sleep(2)
			if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\postcomment.png', confidence=0.7) != None:
				camp_postcomment=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\postcomment.png', confidence=0.7)
				pyautogui.click(camp_postcomment)
				time.sleep(2)
			if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_canal.png', confidence=0.7) != None:
				camp_canal=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_canal.png', confidence=0.7)
				pyautogui.click(camp_canal)
				time.sleep(3)
			if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7) != None:
				camp_video=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7)
				pyautogui.click(camp_video)
			i+=1
	

chrome()
youtube()
cautare_google()