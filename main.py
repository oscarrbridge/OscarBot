from secret import *
import discord
import time

client = discord.Client()

TARGET_CHANNEL = 871292302482636826


@client.event
async def on_ready():
    channel = client.get_channel(TARGET_CHANNEL)
    await client.change_presence(status=discord.Status.online)
    await channel.connect()
    print('Logged in as {0.user}'.format(client))

    print(channel.on_voice_state_update)

    """
        while True:
        print("top")
        channel = client.get_channel(TARGET_CHANNEL)
        usrs_list = {}
        usrs_id = channel.voice_states
        for usrs in usrs_id:
            usrs_list[len(usrs_list) + 1] = usrs
        if len(usrs_id) >= 2:
            for voice in client.voice_clients:
                await voice.disconnect()
        print(usrs_list)
        time.sleep(2)
    """


async def on_voice_state_update(member, before, after):
    channel = client.get_channel(TARGET_CHANNEL)
    channel.on_voice_state_update



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!test'):
        await message.channel.send('running!')

client.run(TOKEN)
