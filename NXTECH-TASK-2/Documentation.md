# Speech Assistant with OpenAI Integration

This is a speech assistant script written in Python that integrates with OpenAI's text-davinci-003 model to provide AI-generated responses to user queries. The assistant can perform various tasks, including browsing websites, opening applications, telling the time, and engaging in a conversation using artificial intelligence.

## Files

The project contains three Python files:

1. `config.py`: This file contains sensitive information, such as the OpenAI API key. It is used to store the API key in a variable named `apikey`.

2. `openai.py`: This file includes a function called `ai(prompt)` that takes a prompt as input and generates a response using OpenAI's text-davinci-003 model. The generated response is then saved to a file in the "Openai" directory.

3. `Speech_Assistant.py`: This is the main file that implements the speech assistant. It uses the `openai.py` file to interact with the OpenAI model and provides various functionalities.

## Features

The speech assistant can perform the following tasks:

1. **Chatting with AI**: The user can engage in a conversation with the AI using voice commands. The assistant sends the user's queries to the OpenAI model and reads out the AI-generated response.

2. **Browsing Websites**: The user can ask the assistant to open specific websites like YouTube, Wikipedia, or Google, and the assistant will open the corresponding website using the default web browser.

3. **Playing Music**: The assistant can open and play a specific music file located at a pre-defined path.

4. **Telling the Time**: The assistant can tell the current time in hours and minutes.

5. **Opening Applications**: The assistant can open applications like FaceTime and Passky (assuming specific paths are set for these applications).

6. **Resetting Chat**: The assistant can reset the conversation history with the AI, clearing the chat history.

7. **Exiting the Assistant**: The assistant can be terminated by asking it to "Jarvis Quit."

## Dependencies

The project relies on the following Python libraries:

- `speech_recognition`: For speech recognition functionality.
- `webbrowser`: To open websites.
- `os`: For interacting with the operating system (opening applications and files).
- `openai`: To interact with the OpenAI model.
- `datetime`: For retrieving the current time.
- `random`: For generating random file names.
- `numpy`: Used by OpenAI for internal processing.

Please make sure these libraries are installed before running the script.

## How to Use

1. Before running the script, ensure you have the required Python libraries installed.

2. Make sure you have obtained an API key from OpenAI and replaced the placeholder API key in the `config.py` file.

3. Execute the `Speech_Assistant.py` script. The assistant will greet you with a welcome message.

4. You can then interact with the assistant using voice commands. The assistant will respond to various queries and perform tasks as mentioned in the Features section.

5. To exit the assistant, say "Jarvis Quit."

6. To reset the conversation history with the AI, say "reset chat."

## Note

The project is based on the OpenAI text-davinci-003 model. Depending on the usage, there might be limitations to the number of API calls and tokens allowed by OpenAI.

Ensure you comply with OpenAI's terms of service and API usage guidelines while using this script.

Please note that the information in this documentation is based on the content available in the provided files and might not cover any external dependencies or future updates.

For more details about the OpenAI API and its capabilities, refer to the official OpenAI documentation.

---

*Disclaimer: The content of the Python files and this documentation are provided by the user, and the accuracy and completeness of the information are not guaranteed. Please verify and review the code before running it on your system.*
