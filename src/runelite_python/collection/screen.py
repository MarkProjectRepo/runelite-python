import numpy as np
from PIL import Image, ImageGrab
import pyautogui

class ScreenCapture:
    def __init__(self, client):
        self.client = client

    def capture_screen(self, include_mouse=False):
        """
        Capture the screen of the RuneLite client.
        
        Args:
            include_mouse (bool): Whether to include mouse information.
        
        Returns:
            dict: A dictionary containing screen capture information.
        """
        # Get the client's canvas bounds
        canvas = self.client.get_canvas()
        x, y, width, height = canvas.getX(), canvas.getY(), canvas.getWidth(), canvas.getHeight()

        # Capture the screen
        screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
        
        # Convert the image to a numpy array
        screen_array = np.array(screenshot)

        result = {
            "screen": screen_array,
            "width": width,
            "height": height
        }

        if include_mouse:
            mouse_x, mouse_y = pyautogui.position()
            result["mouse_x"] = mouse_x - x
            result["mouse_y"] = mouse_y - y
            result["mouse_buttons"] = pyautogui.mouseInfo()

        return result

    def save_screenshot(self, filename="screenshot.png"):
        """
        Capture and save a screenshot of the RuneLite client.
        
        Args:
            filename (str): The filename to save the screenshot.
        """
        capture = self.capture_screen()
        screenshot = Image.fromarray(capture["screen"])
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")

