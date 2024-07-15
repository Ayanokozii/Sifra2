import struct
import sys
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot:
    def __init__(self):
        self.one = Client(
            name="SifraAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="SifraAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="SifraAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="SifraAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="SifraAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Getting Assistants Info...")
        await self.start_assistant(self.one, config.STRING1, "Assistant One")
        await self.start_assistant(self.two, config.STRING2, "Assistant Two")
        await self.start_assistant(self.three, config.STRING3, "Assistant Three")
        await self.start_assistant(self.four, config.STRING4, "Assistant Four")
        await self.start_assistant(self.five, config.STRING5, "Assistant Five")

    async def start_assistant(self, assistant, session_string, assistant_name):
        if session_string:
            await assistant.start()
            try:
                await assistant.join_chat("II_ayano_II")
                await assistant.join_chat("II_ayano_II")
            except:
                pass
            assistants.append(assistant)
            get_me = await assistant.get_me()
            assistant.username = get_me.username
            assistant.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                assistant.name = get_me.first_name + " " + get_me.last_name
            else:
                assistant.name = get_me.first_name
            try:
                await assistant.send_message(
                    config.LOGGER_ID,
                    f"**» {assistant_name} started:**\n\n✨ ID: `{assistant.id}`\n❄ Name: {assistant.name}\n💫 Username: @{assistant.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"{assistant_name} has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                sys.exit()
            LOGGER(__name__).info(f"{assistant_name} Started as {assistant.name}")

# Example usage
userbot = Userbot()

# Example of using struct.unpack correctly
# Assuming you have a binary buffer of 271 bytes

def unpack_example():
    format_string = 'I I I 256s ? ?'
    data = b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00' + b'A' * 256 + b'\x01' + b'\x00'

    if len(data) != struct.calcsize(format_string):
        raise ValueError(f"Data length {len(data)} does not match expected length {struct.calcsize(format_string)}")

    dc_id, api_id, test_mode, auth_key, user_id, is_bot = struct.unpack(format_string, data)
    print(dc_id, api_id, test_mode, auth_key, user_id, is_bot)

# Call the unpack example function
unpack_example()
