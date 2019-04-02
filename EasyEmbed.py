import discord
from discord.ext import commands
import requests
from dhooks import Webhook

TOKEN = 'NTYwNTgxODAyODU1NDk3ODYz.D32CBA.VPJ8XhJ54j_9kGBDNnmn7_xvCPM'

Bot = commands.Bot(command_prefix='!')

@Bot.event
async def on_ready():
   print("The Bot is Booting...")
   print("---------------------")
   print("Boot successful")
   print("Logged in as: {0.user}".format(Bot))

@Bot.event
async def on_message(message):
   etitle = None
   edescription = None
   eurl = None
   eimageurl = None
   sendyorn = None
   hookweburl = None
   if message.author == Bot.user:
       return
   if message.content.startswith("!embed"):
       await Bot.send_message(message.channel, "`Creating embed, what would you like to title your embed? This will also be where your link will be displayed to be clicked on.`")
       responsetitle = await Bot.wait_for_message(author=message.author)
       etitle = ("**"+responsetitle.content+"**")
       await Bot.send_message(message.channel, "`Ok the title of your embed is set, now what who would you like the embed to say?`")
       responsecontent = await Bot.wait_for_message(author=message.author)
       edescription = responsecontent.content
       await Bot.send_message(message.channel, "`Ok now  what url would you like the embed to have linked to it?`")
       responseurl = await Bot.wait_for_message(author=message.author)
       eurl = responseurl.content
       await Bot.send_message(message.channel, "`Last step, please put the image url that you would like your embed to display.`")
       responseimage = await Bot.wait_for_message(author=message.author)
       eimageurl = responseimage.content
       
       myembed = discord.Embed(title = etitle, description = edescription, color = 0xe74c3c, url = eurl,)
       
       myembed.set_image(url = eimageurl)

       myembed.set_footer(text="EasyEmbed, by Camjo#0001", icon_url="https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Peter_Griffin.png/220px-Peter_Griffin.png")
       
       await Bot.send_message(message.channel, "`Is this the embed that you would like to send? Reply yes or no.`")
       await Bot.send_message(message.channel, embed=myembed)
       sendyorn = await Bot.wait_for_message(author=message.author)
       responseyorn = await Bot.wait_for_message(author=message.author)
       sendyorn = responseyorn.content
       if sendyorn == "yes":
           await Bot.send_message(message.channel, "Ok great, what is the webhook url that you would like to send the embed to?")
           responseweburl = await Bot.wait_for_message(author=message.author)
           hookweburl = responseweburl.content
           hook = Webhook(hookweburl)
           print(hook)
           hook.send(embed=myembed)
           await Bot.send_message(message.channel, "Your embed has been sent to that webhook address!")
       if sendyorn == "no":
           await Bot.send_message(message.channel, "Okay you can restart the setup by typing the original command")
           return
       else:
           await Bot.send_message(message.channel, "This is an invalid response")
           return
           


      
       
  

#@Bot.event
#async def on_message(message):
    #if message.author == Bot.user:
      # return
   # elif message.content.startswith("!ehelp"):
  #      helptitle = "Below is a list of commands and guides to use the bot"
  #      helpdescription = None
  #      helpembed = discord.Embed(title = helptitle, description = helpdescription, color = helpcolor, url = helpurl)
#
   #     helpembed.set_footer(text="EasyEmbed, by Camjo#0001", icon_url="https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi3r8PZiLDhAhWFY98KHRWbDqQQjRx6BAgBEAU&url=https%3A%2F%2Ftenor.com%2Fsearch%2Fhula-gifs&psig=AOvVaw2G5QB1VWxwYFIx6IoNgYDY&ust=1554248419984057")
  #      await Bot.send_message(message.channel, embed=helpembed)

Bot.run(TOKEN)
