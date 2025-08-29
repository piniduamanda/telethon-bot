import asyncio
from telethon import TelegramClient
from datetime import datetime

# Your Telegram API credentials
api_id = 17710882
api_hash = '99ae11f963472b96e36275c7fec85fc3'
phone_number = '+94 72 319 5565'

# Message to be shared
message_to_send = """Hey Join Our VIP Channel💯✔
⭕️ Hey join Our VIP Channel !
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
⭕️ Hey join Our VIP Channel !
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
⭕️ Hey join Our VIP Channel !
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
⭕️ Hey join Our VIP Channel !
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
⭕️ Hey join Our VIP Channel !
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
⭕️ Hey join Our VIP Channel !
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
⭕️ Hey join Our VIP Channel !
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
⭕️ Hey join Our VIP Channel !
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1
🔠 https://t.me/+PhC_2mygRq5kNmQ1

Join All of this"""

# All target groups
target_groups = [ "@fantacy_link_share","@link_share_24hrs","@linksharprohub","@reflinkposters","@LinkShare_Earn","@LinksharegroupLk2","@LinksharegroupLk1","@aiteslarobot"
    
]

# Create the Telegram client
client = TelegramClient('test_session', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    while True:
        for group in target_groups:
            try:
                print(f"[{datetime.now()}] Sending message to {group}...")
                await client.send_message(group, message_to_send)
            except Exception as e:
                print(f"❌ Error sending to {group}: {e}")
        print("✅ All messages sent. Waiting 30 minute...\n")
        await asyncio.sleep(1800)  # Wait 30 minute

# Run the script
with client:
    client.loop.run_until_complete(main())
