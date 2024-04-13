# Python Screenshot Capture Program - Documentation

## Introduction
This program allows you to capture a screenshot of your screen using Python. The program provides a graphical user interface (GUI) created with the `tkinter` library to initiate the screenshot capture. The screenshot is saved to a specified file path using the `Pillow` library's `ImageGrab`.

## Requirements
To run this program, you need the following libraries installed:
- `tkinter`: To create the GUI
- `Pillow`: To capture and process the screenshot

You can install these libraries using `pip`:

``` pip install library_name```

### How to use the code 
1. Run the Screenshot_Program.py script.
2. A window with a button labeled "Capture Screenshot" will appear.
3. Click the "Capture Screenshot" button to initiate the screenshot capture.
4. A file dialog will prompt you to select the directory where the screenshot will be saved.
5. After selecting the directory, the screenshot will be captured and saved as "screenshot.png" in the chosen directory.
6. The program will print a success message if the screenshot is saved successfully.

### Code Overview
The code consists of three main functions and a **`tkinter`** GUI:

1. **`take_screenshot(file_path)`**: This function captures the screenshot and saves it to the specified **`file_path`**.
2. **`capture_screenshot()`**: This function handles the screenshot capture when the "Capture Screenshot" button is clicked. It prompts the user to select a directory using a file dialog and then calls the **`take_screenshot`** function to capture and save the screenshot.
3. **`create_gui()`**: This function creates the main GUI window using **`tkinter`**. It creates a button labeled "Capture Screenshot," which, when clicked, triggers the **`capture_screenshot`** function.

The program also checks for user input validation, such as ensuring that the directory path and filename are provided and not empty.

## Known Issue

In some environments, you might encounter the error: **`'< not supported between instances of 'str' and 'int'`**. This issue is related to the **`pyautogui`** library and its interaction with macOS. To work around this issue, we have replaced **`pyautogui`** with **`Pillow`**'s **`ImageGrab`** to capture the screenshot.