# spam_telegram_profile

# Telegram Message Automation with Telethon

This script allows users to send automated repetitive messages to a specified friend on Telegram using the Telethon library.

Features:
User Input: The script prompts users for the friend's username, number of repetitions, and the desired message content.
Rate Limit Handling: The script is designed to handle PeerFloodError which is raised when messages are being sent too quickly.
Async Functionality: Utilizes Python's asyncio for asynchronous operations to ensure efficient messaging.
Setup & Requirements:
Python 3.6 or newer.
Install the required modules:
bash
Copy code

pip install telethon

Usage:
Clone the repository.
Fill in the api_id and api_hash with your Telegram app credentials.
Run the script: __main.py__
bash
Copy code
python telegram_auto_message.py
Follow the on-screen prompts.
Caution:
Repeatedly sending automated messages on platforms like Telegram might be against the platform's terms of service and can result in temporary or permanent bans. Use this script responsibly.
