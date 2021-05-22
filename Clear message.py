@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=5):
  await ctx.channel.purge(limit = amount)
