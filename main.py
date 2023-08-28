import asyncio
from telethon.sync import TelegramClient
from telethon.errors import PeerFloodError

api_id = 'id' #replace with ur values
api_hash = 'hash'

# Prompt user for the target friend's username
friend_username = input("Enter the username of your friend (with @: ")

# Ensure the username is in the correct format
friend_username = friend_username

num_times = int(input("How many times would you like to send the birthday message? (max 500): "))

# Set a limit to 500 times
num_times = min(500, num_times)

# Construct the birthday message
message = str(input("Enter Message :- "))

async def send_message_to_friend_async(client, friend_username):
    try:
        for _ in range(num_times):
            await client.send_message(friend_username, message)
            print(f"Message sent to {friend_username}")
            await asyncio.sleep(1)  # Adding a small delay to avoid hitting limits quickly
    except PeerFloodError:
        print("You're sending messages too quickly. Try again later or adjust the number of repetitions.")
    except Exception as e:
        print(f"Could not send message to {friend_username}. Error: {e}")

async def main_async():
    async with TelegramClient('anon', api_id, api_hash) as client:
        if not await client.is_user_authorized():
            await client.start()
        
        await send_message_to_friend_async(client, friend_username)

if __name__ == "__main__":
    asyncio.run(main_async())
