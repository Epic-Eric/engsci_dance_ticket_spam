import pyautogui
import time
import cv2
import numpy as np

def image_is_red(image, threshold = 0.5):
    img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    b, g, r = cv2.split(img)
    red_mask = (r > g) & (r > b)
    red_percentage = np.sum(red_mask) / (img.shape[0] * img.shape[1])
    return red_percentage > threshold


screen_width, screen_height = pyautogui.size()
time.sleep(1)
pyautogui.click(1000, 270)
time.sleep(0.5)
im = pyautogui.screenshot(region = (936, 520, 5, 5))
im = np.array(im)
while (image_is_red(im)):
    pyautogui.click(1075, 171)
    time.sleep(0.5)
    pyautogui.click(1000, 270)
    time.sleep(1)
    im = pyautogui.screenshot(region = (936, 520, 5, 5))
    im = np.array(im)