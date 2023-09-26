import discord
import time
import asyncio

# server id = 759049404329361418
messages = joined = 0


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"""Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n""")
            messages = 0
            joined = 0

            await asyncio.sleep(60)
        except Exception as e:
            print(e)
            await asyncio.sleep(60)


@client.event
async def on_member_join(member):
    global joined
    joined += 1
    # This is going to get all the channels that are in the server that the member joined
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(759049404329361418)
    channels = ['general', 'commands']

    if str(message.channel) in channels:
        if message.content== "-hi" != -1:
            await message.channel.send("hello")
        elif message.content == "-users" != -1:
            await message.channel.send(f"""# Number of Members: {id.member_count}""")
        elif message.content == "-help" != -1:
            await message.channel.send("There are currently only 3 commands, but I am upgrading and improving "
                                       "soon:\n-hi = Returns a message saying 'hello'\n-users = Returns number of "
                                       "members in the server\n-help = lists all commands")


client.loop.create_task(update_stats())
client.run(token)
