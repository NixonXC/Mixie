import discord 
from discord.ext import commands
from webserver import keep_alive
import os

client = commands.Bot(command_prefix=">")
client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "Help❔", descreption = "Use >help <command> for extended information on a command.",color = ctx.author.color)

  em.add_field(name = "Moderation", value = " kick , ban , mute , unmute ")

  em.add_field(name = "About", value = " version , support , sourcecode , AboutEm , ChangeLogs ")

  await ctx.send(embed = em)

@client.group(invoke_without_command=True)
async def AboutEm(ctx):
  em = discord.Embed(title = "About❓", descreption = "Use >help <command> for extended information on a command.",color = ctx.author.color)

  em.add_field(name = "Mixie About", value = " support , sourcecode , About , ChangeLogs ,  developers ")

  await ctx.send(embed = em)

@client.command()
async def ChangeLogs(ctx):
  await ctx.send("Bug Fixing,some secrets :),New Embeds,24/7 BOT BABA BOIIIIIIIIIII ")

@client.command()
async def About(ctx):
  await ctx.send("A Simple Moderation Bot Made by NixonXC 100% open source and you can join our support server do >support :)")

@client.command()
async def support(ctx):
  await ctx.send("Join Our support server - https://discord.gg/RYCYgRnkgP  🍕 ")

@client.command()
async def sourcecode(ctx):
  await ctx.send("join for the link and to support us :) - https://discord.gg/RYCYgRnkgP  💻 ")

@client.command()
async def version(ctx):
  await ctx.send("version - 1.18 rektifine Replit ✅")

@client.group(invoke_without_command=True)
async def developers(ctx):
  em = discord.Embed(title = "Developers", descreption = "Use >help <command> for extended information on a command.",color = ctx.author.color)

  em.add_field(name = "Devs", value = " Bot By NixonXC  ✅ ")

  await ctx.send(embed = em)

@client.group(invoke_without_command=True)
async def website(ctx):
  em = discord.Embed(title = "Websites", descreption = "Use >help <command> for extended information on a command.",color = ctx.author.color)

  em.add_field(name = "Website", value = "  https://mixie.glitch.me/#commands our offical website 💎 ")

  await ctx.send(embed = em)

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=5):
  await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "Reason Not Provided"):
  await member.send("You Have Been kicked from Server🔥  , Because: "+reason)
  await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "Reason Not Provided"):
  await ctx.send(member.name + " has Been BANNED from Server ⚔ , Because: "+reason)
  await member.ban(reason=reason)

@client.command(aliases=['m'])
@commands.has_permissions(manage_messages=True)
async def mute(ctx,member : discord.Member):
  muted_role = ctx.guild.get_role(Your Role ID)

  await member.add_roles(muted_role)

  await ctx.send(member.mention + " Has Been Muted")

@client.command(aliases=['um'])
@commands.has_permissions(manage_messages=True)
async def unmute(ctx,member : discord.Member):
  muted_role = ctx.guild.get_role(Your Role ID)

  await member.remove_roles(muted_role)

  await ctx.send(member.mention + " Has Been Unmuted")

@client.event
async def on_ready():
  activity = discord.Game(name="ᴍɪxɪᴇ | ɴᴏᴡ 24/7 ʙᴏᴛ ʙʏ ɴɪxᴏɴxᴄ", type=3)
  await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
  print("Mixie is now Ready!!")

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)
