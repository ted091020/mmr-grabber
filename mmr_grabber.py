import numpy
import cv2
import pytesseract
import PIL
import pyautogui
import time
from PIL import Image



def tesser_image(image):
	image = cv2.resize(image, (0,0), fx=2, fy=2)
	ret,image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
	image = PIL.Image.fromarray(image, "L")
	image.save("test.jpg")
	txt = pytesseract.image_to_string(image, config="--psm 6")
	return(txt)

def screengrab_as_numpy_array(location):
	im = numpy.array(PIL.ImageGrab.grab(bbox=(location[0],location[1],location[2],location[3])))
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	return(im)


scrn_txt = tesser_image(screengrab_as_numpy_array((618, 536, 722, 553)))
while True:
	time.sleep(1)
	scrn_txt = tesser_image(screengrab_as_numpy_array((618, 536, 722, 553)))
	if scrn_txt == "LEAGUE":
		mmr = tesser_image(screengrab_as_numpy_array((665, 722, 780, 755)))
		print(mmr)
		time.sleep(60)





