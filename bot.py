"""
MIT License

Copyright (c) 2023 --卡拉马里毒药..

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import configparser
import os
from colorama import *
import discord
from discord.ext import commands

# ;Files; #
import Engine

os.system('cls')

config = configparser.ConfigParser()
config.read('bot.cfg')
dtoken=config['inf']['token']


intents = discord.Intents.all()
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)
exceptions=['png', 'jpg', 'jpeg', 'gif'] # Put in File Extension without the .

class Menu(discord.ui.View):
    @discord.ui.button(label="🧪 Detections", style=discord.ButtonStyle.green)
    async def menu1(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(s[6])
    @discord.ui.button(label="💉 Signatures", style=discord.ButtonStyle.green)
    async def menu2(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(s[6])
    @discord.ui.button(label="❌ Report", style=discord.ButtonStyle.green)
    async def menu3(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(f'**Report Feature has not been setup by administrator.**')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="📛 10.3k Servers 📛"))

@client.event
async def on_message(message):
    if str(message.attachments) == '[]':
        pass
    else:
        if message.author.bot:
            pass
        else:
            global s
            split_v1 = str(message.attachments).split("filename='")[1]
            filename = str(split_v1).split("' ")[0]
            url=str(message.attachments[0])
            filetype = str(os.path.splitext(filename)[1]).replace('.', '')
            # md5, total, detected, fileType, fileSize, scanDate, scanUrl, cachedir, filename
            #await message.reply(f'**Woah {message.author.mention}! Please wait while we scan your files for any suspicous malware or viruses, Thank you.**')
            s=Engine.Engine.inputFile(filename=filename, filetype=filetype, url=url) # Scan File
            embed = discord.Embed(title=f'Malware Analysis', colour=discord.Colour.blue())
            embed.set_author(name=f"{filename}", url=f"{s[6]}", icon_url=f"{s[6]}")
            embed.set_thumbnail(url=f"{message.author.avatar}")
            embed.add_field(name=f'🦠 Detections', value=f"{s[2]}/{s[1]}")
            embed.add_field(name=f'📁 File Size', value=f"{s[4]}MB")
            embed.add_field(name=f'🔒 File Type', value=f"{s[3]}")
            embed.set_footer(text=f"MD5- {s[0]}")
            #file = discord.File(f"{s[7]}//{s[8]}")
            try:
                view = Menu()
                await message.reply(view=view, embed=embed)
                print(f'{Fore.LIGHTBLACK_EX}{s[5]} FILE {Fore.BLUE}-{Fore.CYAN} {filename} {Fore.GREEN} "{s[7]}"{Fore.WHITE} 200{Fore.MAGENTA} 20107')
                print(f'{Fore.LIGHTBLACK_EX}{s[5]} FILE {Fore.BLUE}-{Fore.LIGHTMAGENTA_EX} Md5 "{s[0]}" Detections "{s[2]}/{s[1]}" FileSize "{s[4]}Mb" FileType "{s[3]}"')
            except:
                await message.reply(f'**Failed to analyze file**')
            # Delete Cache #
            for file in os.scandir(s[7]):
                os.remove(file.path)
            os.rmdir(s[7])
    if '$md5' in str(message.content):
        p=str(message.content).split()
        md5=str(p[1])
        s=Engine.Engine.md5Scan(md5=md5)
        # md5, total, detected, fileType, fileSize, scanDate, scanUrl, cachedir, filename
        #await message.reply(f'**Woah {message.author.mention}! Please wait while we scan your files for any suspicous malware or viruses, Thank you.**')
        embed = discord.Embed(title=f'MD5 Hash Scan', colour=discord.Colour.blue())
        embed.set_author(name=f"{md5}", url=f"{s[6]}", icon_url=f"{s[6]}")
        embed.set_thumbnail(url=f"{message.author.avatar}")
        embed.add_field(name=f'🦠 Detections', value=f"{s[2]}/{s[1]}")
        embed.add_field(name=f'📁 MD5 Length', value=f"{s[4]} Bytes")
        embed.add_field(name=f'🔒 MD5 Type', value=f"128 Bits")
        embed.set_footer(text=f"MD5- {s[0]}")
        #file = discord.File(f"{s[7]}//{s[8]}")
        try:
            view = Menu()
            await message.reply(view=view, embed=embed)
            print(f'{Fore.LIGHTBLACK_EX}{s[5]} MD5  {Fore.BLUE}-{Fore.CYAN} {md5}{Fore.GREEN}  "cache//{md5}.md5"{Fore.WHITE} 200{Fore.MAGENTA} 20107')
            print(f'{Fore.LIGHTBLACK_EX}{s[5]} MD5  {Fore.BLUE}-{Fore.LIGHTMAGENTA_EX} Md5 "{md5}" Detections "{s[2]}/{s[1]}" MD5 Length "{s[4]} Bytes" MD5 Type "128 Bits"')
        except:
            await message.reply(f'**Failed to analyze file**')

client.run(str(dtoken))