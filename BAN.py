@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "Reason Not Provided"):
  await ctx.send(member.name + " has Been BANNED from Server, Because: "+reason)
  await member.ban(reason=reason)
