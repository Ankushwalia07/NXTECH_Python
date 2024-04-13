import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageGrab

def take_screenshot(file_path):
    """
    Function to take a screenshot and save it to the specified file path.

    Parameters:
        file_path (str): The path where the screenshot will be saved.

    Returns:
        None
    """
    try:
        # Take the screenshot using Pillow's ImageGrab
        screenshot = ImageGrab.grab()

        # Save the screenshot to the specified file path
        screenshot.save(file_path)

        print(f"Screenshot saved successfully to {file_path}")
    except Exception as e:
        print(f"Failed to take screenshot: {e}")

def capture_screenshot():
    """
    Function to handle the screenshot capture when the button is clicked.

    Parameters:
        None

    Returns:
        None
    """
    try:
        # Get the directory path from the user where the screenshot will be saved
        directory_path = filedialog.askdirectory(title="Select Directory")

        # Check if the directory path is provided and not empty
        if not directory_path:
            return

        # Get the filename from the user
        filename = "screenshot.png"

        # Concatenate the directory path and filename to form the complete file path
        file_path = os.path.join(directory_path, filename)

        # Call the function to take the screenshot
        take_screenshot(file_path)
    except Exception as e:
        print(f"Error: {e}")

def create_gui():
    """
    Function to create the GUI for the screenshot capture.

    Parameters:
        None

    Returns:
        None
    """
    # Create the main window
    root = tk.Tk()
    root.title("Screenshot Capture")

    # Create the capture button
    capture_button = tk.Button(root, text="Capture Screenshot", command=capture_screenshot)
    capture_button.pack(pady=10)

    # Run the GUI event loop
    root.mainloop()

# Call the function to create the GUI
if __name__ == "__main__":
    create_gui()
