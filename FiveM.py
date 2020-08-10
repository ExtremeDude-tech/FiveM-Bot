try:
    import requests, re, discord, asyncio, json, os; from discord.ext import commands
    bot = commands.Bot(command_prefix='?', selfbot=False)
    try:
        setup = json.load(open('config.json'))
    except:
        print("Exception found -> Cannot open 'config.json' | File Not Exist / Other Error")
        input('\nPress ENTER to exit!')
        os._exit(1)
    def get_members():
        r = requests.get('http://{}:{}/players.json'.format(setup['ip'], setup['port']))
        f = re.findall('"name":"(.*?)"', str(r.content))
        return len(f)
    @bot.event
    async def on_ready():
        os.system('title Coded by ExtremeDev.')
        print("Bot is up")
        
    @bot.command(aliases=['members'])
    async def members_fivem(ctx):
        await ctx.send(f'Online Members: `{get_members()}`')
    @bot.command(aliases=['serverinfo', 'infoserver'])
    async def info(ctx):
        await ctx.send('Members(Discord): `{}`\nOnline Members(FiveM): `{}`'.format(len(ctx.guild.members), get_members()))
    try:
        bot.run(setup['token'], bot=True)
    except:
        print("Exception found -> Invalid Token")
        input('\nPress ENTER to exit!')
        os._exit(1)
except Exception as e:
    print("Exception in code:\n\n{}".format(e))
