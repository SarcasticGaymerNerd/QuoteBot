# Twitch Quote Bot

Welcome to the Twitch Quote Bot! This bot allows Twitch users to add, search, and manage quotes directly in the chat. It is designed to enhance community interaction by allowing users to share memorable quotes and moments.

## Features

- **Add Quotes**: Users can add quotes along with their usernames.
- **Search Quotes**: Users can search for quotes by number or keyword.
- **List Quotes**: Users can view all stored quotes in the chat.
- **Count Quotes**: Users can check the total number of quotes available.
- **Persistent Storage**: Quotes are stored in a JSON file, ensuring they persist across bot restarts.

## Installation

### Prerequisites

- Python 3.6 or higher
- A Twitch account and a registered application to obtain your OAuth token

### Steps

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required libraries**:
   Make sure you have Python installed, then install the necessary libraries:
   ```bash
   pip install twitchio
   ```

3. **Set up your Twitch credentials**:
   - Obtain your OAuth token from [Twitch Token Generator](https://twitchtokengenerator.com/) or through the Twitch Developer portal.
   - Replace `YOUR_TWITCH_TOKEN` and `YOUR_CHANNEL` in the `bot.py` file with your actual Twitch token and channel name.

4. **Create the quotes storage file**:
   The bot will automatically create a `quotes.json` file when it first runs if it does not already exist.

## Usage

Run the bot using the command:
```bash
python bot.py
```

Once the bot is running, it will join the specified Twitch channel and respond to commands in the chat.

## Available Commands

- `!addquote <quote>`: 
  - **Description**: Adds a new quote to the list. The quote will be stored with the user's name and a unique quote number.
  - **Example**: 
    ```
    !addquote This is a great quote!
    ```
  - **Response**: 
    ```
    Quote added: "1: UserName: "This is a great quote!""
    ```

- `!quotes`: 
  - **Description**: Lists all stored quotes in the chat.
  - **Example**: 
    ```
    !quotes
    ```
  - **Response**: 
    ```
    Quotes:
    1: UserName: "This is a great quote!"
    2: AnotherUser: "Another memorable quote!"
    ```

- `!searchquote <query>`: 
  - **Description**: Searches for quotes by number or keyword. If a number is provided, it returns the corresponding quote. If a keyword is provided, it returns all matching quotes.
  - **Example**: 
    ```
    !searchquote 1
    ```
    or 
    ```
    !searchquote great
    ```
  - **Response**: 
    ```
    Search results:
    1: UserName: "This is a great quote!"
    Total quotes available: 2
    ```

- `!quote_count`: 
  - **Description**: Displays the total number of quotes available in the bot's storage.
  - **Example**: 
    ```
    !quote_count
    ```
  - **Response**: 
    ```
    Total quotes available: 2
    ```

## Data Storage

Quotes are stored in a JSON file named `quotes.json`. This file will be created automatically when the bot first runs if it does not already exist. The structure of the file is a simple list of strings, where each string represents a quote.

### Example of `quotes.json`:
```json
[
    "1: UserName: \"This is a great quote!\"",
    "2: AnotherUser: \"Another memorable quote!\""
]
```

## Troubleshooting

- **Bot Not Responding**: Ensure that the bot is running and connected to the correct Twitch channel. Check your OAuth token and channel name for accuracy.
- **Quotes Not Saving**: Ensure that the bot has permission to write to the directory where it is running. Check for any file permission issues.
- **Errors in Chat**: If the bot throws errors in the chat, check the console for error messages and ensure that all dependencies are installed correctly.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request. Please ensure that your code adheres to the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Twitch community for their support and feedback.
- Special thanks to the developers of the `twitchio` library for making it easy to interact with Twitch chat.

---

Feel free to reach out if you have any questions or need further assistance!