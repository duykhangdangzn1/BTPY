import pyautogui

image = r'C:\Users\Lenovo\Desktop\Selenium\debug.png'
image1 = r'C:\Users\Lenovo\Desktop\Selenium\sec.png'

for i in range(10):
    # Find the location of the first image on the screen
    image_location = pyautogui.locateOnScreen(image)
    
    if image_location:
        # Get the center coordinates of the found location
        x, y = pyautogui.center(image_location)
        
        # Click on the center of the found location
        pyautogui.click(x, y)
    else:
        print(f"Image '{image}' not found on the screen.")
    
    # Find the location of the second image on the screen
    image_location1 = pyautogui.locateOnScreen(image1)
    
    if image_location1:
        # Get the center coordinates of the found location
        x1, y1 = pyautogui.center(image_location1)
        
        # Click on the center of the found location
        pyautogui.click(x1, y1)
    else:
        print(f"Image '{image1}' not found on the screen.")
