import discord
from discord.ext import commands
import random, time, os



# client= discord.Client()
bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print(f"connected as {bot.user}")

    for guild in bot.guilds:
        print(guild.name)
        print(" ".join([members.name for members in guild.members]))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print('err')
        await ctx.send('Please pass in all required arguements :rolling_eyes:')
    if isinstance(error, commands.MissingPermissions):
        print('err')
        await ctx.send('You do not have all required permissions')

# @bot.event
# async def on_member_join(member)
#     await bot.getchannel(WELCOMER_CHANNEL).send(f'Welcome {member.name}')
@bot.command(name='raise', help='Raises an exception and shuts down the bot')
async def raise_except(ctx, msg):
    await ctx.send(f'Raised Exception :{str(msg)}')
    raise discord.DiscordException

# @bot.command(name='isadmin')
# @has_permission(administrator=True)
# async def is_admin(ctx):
#     await ctx.send(f"You are an Admin {ctx.message.author.mention}")

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#
#     if message.content[0:7] == '.raise':
#         await message.channel.send(f'Raised Exception :{message.content[7:]}')
#         raise discord.DiscordException


@bot.command(name='diceroll', help='Rolls a die and outputs random numbers[1,6]')
async def dice_roll(ctx):
    roll = ['one','two','three','four','five','six']
    await ctx.send(f'You got :{roll[random.randint(0,5)]}:')

@bot.command(name='cointoss', help='tosses a coin and outputs the result')
async def dice_roll(ctx):
    roll = [':regional_indicator_h::regional_indicator_e::regional_indicator_a::regional_indicator_d::regional_indicator_s:',':regional_indicator_t::regional_indicator_a::regional_indicator_i::regional_indicator_l::regional_indicator_s:']
    await ctx.send(f'You got {roll[random.randint(0,1)]}')

@bot.command(name='clear',help='Clears "n" messages')
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'`Cleared {amount} messages`', delete_after=5)

@bot.command(name='msg',help='Messages a user')
async def msg(ctx ,member=None , msg=""):
    await ctx.send(f'{member}\n`{msg}`')

@bot.command(name='kick', help='kicks a user with a reason')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member=None, reason=None):
    await member.kick(reason=reason)


@bot.command(name='ban', help='bans a user with a reason')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member=None, reason=None):
    await member.ban(reason=reason)

@bot.command(name='unban', help='unbans a member')
@commands.has_permissions(administrator=True)
async def unban(ctx, member:discord.Member=None):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split("#")

    for banned in banned_users:
        user = banned.user

        if (user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')

def bot_run():
    bot.run(os.environ["TOKEN"])

if '__main__' == __name__:
    bot_run()
