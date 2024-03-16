from imports import *

API_ID = API_ID
API_HASH = API_HASH
BOT_TOKEN = BOT_TOKEN


HackerRick = Client("forward", api_id=API_ID, api_hash=API_HASH, bot_token =BOT_TOKEN)

@HackerRick.on_message(filters.command("url"))
def get_message_content(client, message):

    user_id = message.from_user.id
    
    message_url = message.text.split()[1]
    parts = message_url.split("/")
    channel_name = parts[-2]
    message_id = int(parts[-1])

    try:
        message = client.get_messages(channel_name, message_id)
        message_content = message.text
        HackerRick.send_message(user_id,message_content)
    except Exception as e:
        print(f"Error: {e}")

HackerRick.run()
