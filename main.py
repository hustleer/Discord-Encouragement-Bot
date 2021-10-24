#Botpic:https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Red_Rose_Photography.jpg/800px-Red_Rose_Photography.jpg

#Botpic:https://commons.wikimedia.org/wiki/File:Red_Rose_Photography.jpg

#reference:https://www.youtube.com/watch?v=SPTfmiYiuok
import discord
import os
import requests
import json
import math, random
from replit import db
from keep_alive import keep_alive

import asyncpraw, asyncprawcore
#import commands

import time, asyncio, datetime
from discord.ext import tasks
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from prawcore import NotFound
import ffmpeg

from discord import FFmpegPCMAudio
from dotenv import load_dotenv
from youtube_search import YoutubeSearch

load_dotenv()

client = discord.Client()


# To cache the every user For on_remove_reaction to be usable
# Also enable members intent from https://discord.com/developers/ in bot secition
intents = discord.Intents.default()
intents.members = True

global playing, stream
global currently_playing_message


def say_hello():
    print(time.ctime())
    #await message.channel.send("hello :-)" + str(joke))


#t1 = threading.Timer(10, say_hello)
#t1.start()

#---------- To keep the bot alive --------------------------
#1. keeping the bot alive
'''

#------------------- adding a background task -----------------
status = cycle(['with Python','JetHub'])

@bot.event
async def on_ready():
  change_status.start()
  print("Your bot is ready")

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))
#--------------------------------------------------------------



3. Setup the Uptime Robot :

create an account on uptime robot.
After creating an account, go to the dashboard and click on Add new monitor (preview)
select monitor type Http(s) (preview)
then go to to ur project on repl.it and copy the url from the top of the console and paste it in url section of the monitor (preview)
now set the monitoring interval to every 5 mins (so that it will ping the bot every 5 mins) and click on create monitor twice (preview)
That’s it…Now go to ur project on repl.it and hit the Run button
'''


class MySchedule:
    async def schedule_message(sth,
                               author='anonymous',
                               message='please provide a message',
                               id=863298114949218324,
                               seconds=0):
        print('received:')
        print(author, message, id, seconds)
        #await ctx.message.delete()
        if author == 'anonymous':
            #author = 'anonymous'
            description = 'command: .anon your_message'
        else:
            author = author + '  <scheduled_message>'
            description = "command: .schedule time_in_seconds your_message"
            time.sleep(seconds)
            print('sleep 10 seconds')
        print('author : ', author)
        #channel = bot.get_channel(id=ctx.channel.id)
        #print('sending {}'.format(message))

        #retStr = str("""```css\nThis is some colored Text```""")
        #embed = discord.Embed(title="Random test")
        #embed.add_field(name="Name field can't be colored as it seems",value=retStr)
        #await ctx.send(embed=embed)

        #message = str(ctx.message.author).split('#')[0] + ' : ' + message
        embed = discord.Embed(title=author, colour=discord.Color.blue())
        embed.add_field(
            name=message,
            value=description,
        )
        channel = bot.get_channel(id=id)
        await channel.send(embed=embed)


reddit = asyncpraw.Reddit(
    client_id="nnhGBCiBxSJysTobl6SLPQ",
    client_secret=os.environ['rd_client_secret'],
    password=os.environ['rd_pass'],
    user_agent="praw_test",
    username="Alternative-Ad-8849",
)


async def sub_exists(subreddit_name):
    exists = True
    if subreddit_name.startswith(('/r/', 'r/')):
        subreddit_name = subreddit_name.split('r/')[-1] # -1 gets the last element in the list
    try:
        subreddit = await reddit.subreddit(subreddit_name, fetch=True)     # by default Async PRAW doesn't make network requests when subreddit is called
        # do something with subreddit
    except asyncprawcore.Redirect: 
        exists=False
    return(exists)
    # Reddit will redirect to reddit.com/search if the subreddit doesn't exist
    #await ctx.send(f"Subreddit {subreddit_name} doesn't exist.")



def get_nude():
    memes_submissions = reddit.subreddit('BustyPetite').hot()
    print('got memes')
    post_to_pick = random.randint(1, 15)
    print('choosen random')
    for i in range(0, post_to_pick):
        print('for loop:{}'.format(i))
        submission = next(x for x in memes_submissions if not x.stickied)
    return (submission.url)


def get_crazy(sub_reddit_name='memes'):
    memes_submissions = reddit.subreddit(sub_reddit_name).hot()
    #print('got memes')
    #post_to_pick = random.randint(1, 15)
    #print('choosen random')

    start = random.randint(100, 1000)
    end = random.randint(start, start + 100)
    print('start:{} end:{}'.format(start, end))
    for i in range(start, end):
        #print('for loop:{}'.format(i))
        submission = next(x for x in memes_submissions if not x.stickied)
        yield (submission.url)


def get_memes_crazy():
    memes_submissions = reddit.subreddit('memes').hot()
    print('got memes')
    #post_to_pick = random.randint(1, 50)
    print('choosen random')
    for i in range(0, 50):  #post_to_pick):
        print('for loop:{}'.format(i))
        submission = next(x for x in memes_submissions if not x.stickied)
        yield (submission.url)
    #return submission


async def get_one(sub_reddit='memes'):
    #Working
    #submission = list(reddit.subreddit(sub_reddit_name).random()#.hot(limit=None))
    #submissions = list(reddit.subreddit('redditdev').hot(limit=None))
    '''urls=[]
    submissions = await list(reddit.subreddit('redditdev').hot(limit=None))
    print(await submissions)'''

    #submissions = await reddit.subreddit("memes").hot(limit=random.randint(1,150))

    #for submission in submissions:
    #  pass

    subreddit = await reddit.subreddit(sub_reddit)
    async for submission in subreddit.random_rising(
            limit=random.randint(1, 150)):
        pass
        #print(submission.title)

        #urls.append([submission.title,submission.url])
        #yield(submission.title, submission.url)
        #print(submission.title)'''

    #submissionn = random.choice(submissions)
    #submission = reddit.subreddit("AskReddit").random()
    #submissions = reddit.subreddit('redditdev').hot(limit=None))
    #submission = random.choice(submissions)
    #print('got memes')
    #post_to_pick = random.randint(1, 50)
    #print('choosen random')
    '''for i in range(0, 50):#post_to_pick):
        print('for loop:{}'.format(i))
        submission = next(x for x in memes_submissions if not x.stickied)'''
    #submission = await random.choice(memes_submissions)
    #return(submission.url)
    #print(submissionn.url)
    #print(submission.title)
    #return('hi')

    embed = discord.Embed(title=submission.title,
                          url=submission.url,
                          description=submission.selftext,
                          colour=discord.Color.red())
    embed.set_image(url=submission.url)
    #await channel.send(embed=embed)

    return (embed)


from discord.ext import commands

bot = commands.Bot(command_prefix='.', help_command=None, intents=intents)
'''
class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(colour=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

bot.help_command = MyHelpCommand()'''


# My sample help command:
@bot.command(name='help',
             brief='`.help` for help',
             help='Plesae enter `.help` for help')
async def help(ctx, args=None):
    """ Check which mods are online on current guild """
    help_embed = discord.Embed(
        title="Encouragement Bot Help!",
        #url="https:ioee.herokuapp.com/",
        description=
        "Type `.help <command name>` for more details about each command. e.g. `.help joke`",
    )
    command_names_list = [x.name for x in bot.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value='value',
            #value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot.commands)]),
            inline=False,
            #colour=discord.Color.blue()
        )
        #bot.get_command(x.name).help
        for i in bot.commands:
            help_embed.add_field(
                name='***{}***'.format(i.name),
                #value='value'
                value='> {}\n\n\n'.format(bot.get_command(i.name).brief),
                inline=False,
                #colour=discord.Color.blue()
            )

            #print(i.name)
            #print(i)
            #print(bot.get_command(i.name).help)
        '''for i,command in enumerate(bot.commands):
            
            help_embed.add_field(
                name = command,
                value = bot.get_command(command),
                inline=True
            )'''
        help_embed.add_field(
            name="Details",
            value=
            "Type `.help <command name>` for more details about each command.",
            inline=False)

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(name=args,
                             value=str(bot.get_command(args).brief) + ' \n' +
                             str(bot.get_command(args).help))

    # If someone is just trolling:
    else:
        help_embed.add_field(name="Nope.",
                             value="Don't think I got that command, boss!")

    await ctx.send(embed=help_embed)


# My sample help command:
@bot.command(name='share_info',
             brief='`.share_info` for share_info',
             help='Plesae enter `.share_info` for mero_share_info')
async def info(ctx, args=None):
    response = requests.get('http://ioee.herokuapp.com/meroshare/')
    response = response.text.strip()
    print(response)

    try:
        previous_messages = await ctx.channel.history(limit=1).flatten()
        prev_message = previous_messages[0].content
        print('previous_message:')
        print(prev_message)
    except:
        pass

    if (str(prev_message).strip() != response):
        print('not same messages:prev_message and rseponse')
        await ctx.send(response)

    else:
        print('same message as previous message, so not sending')
        pass


@bot.command(name='ping',
             brief=" short_help:to test if bot responding ",
             help='long_help: e.g. .ping')
async def ping(ctx, subreddit='jokes', no_of_posts=1, user='.'):
    #channel = bot.get_channel(id=int(channel_id))
    '''for n, submission in enumerate(reddit.subreddit('memes').top('day',limit=int(no_of_posts/3))):
      print('Unleash for loop:{}'.format(n))
      title = submission.title
      body = submission.selftext
      embed = discord.Embed(
        title=submission.title,
        url=submission.url,
        description=body,
        colour=discord.Color.green())
      embed.set_image(url=submission.url)
      await ctx.send(embed=embed)'''

    await ctx.send('pong ')
    print('Ping-Pong is invoked: ', user, ctx)


@bot.command(name='embed', help='e.g.`.embed`', brief='embedding help')
async def embed(ctx):
    embed = discord.Embed(title="Text Formatting",
                          url="https://realdrewdata.medium.com/",
                          description="Here are some ways to format text",
                          colour=discord.Color.blue())
    embed.set_author(
        name="RealDrewData",
        url="https://twitter.com/RealDrewData",
        icon_url=
        "https://cdn-images-1.medium.com/fit/c/32/32/1*QVYjh50XJuOLQBeH_RZoGw.jpeg"
    )
    #embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    embed.add_field(name="*Italics*",
                    value="Surround your text in asterisks (\*)",
                    inline=False)
    embed.add_field(name="**Bold**",
                    value="Surround your text in double asterisks (\*\*)",
                    inline=False)
    embed.add_field(name="__Underline__",
                    value="Surround your text in double underscores (\_\_)",
                    inline=False)
    embed.add_field(name="~~Strikethrough~~",
                    value="Surround your text in double tildes (\~\~)",
                    inline=False)
    embed.add_field(name="`Code Chunks`",
                    value="Surround your text in backticks (\`)",
                    inline=False)
    embed.add_field(name="Blockquotes",
                    value="> Start your text with a greater than symbol (\>)",
                    inline=False)
    embed.add_field(name="Secrets",
                    value="||Surround your text with double pipes (\|\|)||",
                    inline=False)
    embed.set_footer(text="Learn more here: realdrewdata.medium.com")
    await ctx.send(embed=embed)


@bot.command(name='schedule',
             brief='to schedule message to be sent in any group.',
             help='e.g. `.schedule 10 scheduled for ten seconds.')
async def schedule(ctx, seconds: int = 3, *, message='Hello There'):
    #print(ctx.channel.id)
    print('Seconds: ', seconds)
    msg = str(message)
    #print(msg)
    await ctx.message.delete()
    id = ctx.channel.id
    author = str(ctx.message.author).split('#')[0]
    #print(author)
    #print(type(id))
    sch = {
        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': '',
    }
    r = random.randint(1, 5)

    sch[str(r)] = MySchedule()
    await sch[str(r)].schedule_message(author=author,
                                       message=msg,
                                       id=id,
                                       seconds=int(seconds))

    #await schedule_message(author=author, message=msg, id=id, seconds=3)
    #print(id)
    #print(channel)
    #await channel.send('hi')


'''@bot.command()
async def schedule(ctx, message='Hello There', seconds = 3):
    #print(ctx.channel.id)
    m=str(message)
    id = ctx.message.id
    print('\n\n\n{}\n\n'.format(m))
    author = str(ctx.message.author).split('#')[0]
    
    await ctx.message.delete()
    #id=ctx.channel.id
    
    channel = bot.get_channel(id=id)
    print(id)
    print(channel)
    #await channel.send('hi')
    #await schedule_message(author, m, id, seconds = seconds)
    #print(ctx.message)
    #await ctx.message.delete(ctx.message)
    #await channel.send('hi')
    #await ctx.send('pong')
    #print('Im invoked')'''


@bot.command(name='anon',
             brief='to send message anonymously',
             help='e.g. `.anon Guess who!`')
async def anon(ctx, *, message='please provide a message'):
    msg = str(message)
    #print(msg)
    await ctx.message.delete()
    id = ctx.channel.id
    a = {'anon': ''}
    a['anon'] = MySchedule()
    await a['anon'].schedule_message('anonymous', msg, id)
    print('send')
    print(msg, id)
    #await schedule_message(author='', message=msg, id=id)


@bot.command(name="echo",
             pass_context=True,
             brief='ehhoes/repeat the message deleting the user\'s message',
             help='e.g. `.echo I am echoed`')
async def echo(ctx, *, message='please provide a message'):
    msg = message
    #print(ctx.message)
    try:
        await ctx.message.delete()
    except:
        pass
    #id=ctx.channel.id
    await ctx.send(msg)


@echo.error
async def echo_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(
            ctx.message.author)
        await bot.send_message(ctx.message.channel, text)


@bot.command(name='unleash',
             brief='unleahes the subreddit to c channel',
             help='e.g.To unleash r/jokes `.unleash jokes`')
async def unleash(ctx, subreddit='none'):
    if subreddit == 'none':
        await ctx.send('Please enter the subreddit to be unleashed')
    else:
        print(ctx.channel.id)
        #if "unleash" not in db.keys():db['unleash']={}
        if await sub_exists(subreddit):
            if str(ctx.channel.id) not in db['unleash']:
                #i.e. channel doesn't exists in database
                db['unleash'][str(ctx.channel.id)] = []
                #db['unleash'][str(ctx.channel.id)].append(str(subreddit))
            else:
                #i.e. channel doesn't exists in database
                
                if str(subreddit) not in db['unleash'][str(ctx.channel.id)]:
                  db['unleash'][str(ctx.channel.id)].append(str(subreddit))
                  await ctx.send('unleashing r/{} to {}'.format(subreddit, ctx.channel))
                else:
                  await ctx.send('r/{} already unleashed to {}'.format(subreddit, ctx.channel))
        else:
            await ctx.send('Sorry! subreddit  r/{} doesnot exists.'.format(
                subreddit, ctx.channel))


@bot.command(name='contain',
             brief='to contain/stop unleashed  subreddit message',
             help='e.g. `.contain jokes`')
async def contain(ctx, subreddit='none'):
    if subreddit == 'none':
        await ctx.send('Please enter the subreddit to be unleashed')
    else:

        print(ctx.channel.id)
        if str(ctx.channel.id) in db['unleash'] and str(
                subreddit) in db['unleash'][str(ctx.channel.id)]:
            db['unleash'][str(ctx.channel.id)].remove(str(subreddit))
            await ctx.send(
                'successfully contained subreddit r/{} from {}'.format(
                    subreddit, ctx.channel))
        else:
            await ctx.send('Subreddit  r/{} not unleashed in .'.format(
                subreddit, ctx.channel))
        #print(ctx.channel.id)
        #await ctx.send(ctx.channel.id)


@bot.command(
    name='go',
    brief='to see memes from r/memes or nude from r/\'BustyPetite\'',
    help='e.g. `.go meme`, `.go meme crazy`, `.go nude`, `.go nude crazy`')
async def go(ctx, what='', what2=''):
    print('wHat:{} what2:{}'.format(what, what2))
    if what == 'nude':
        if what2 == 'crazy':
            print('1')
            urls = get_crazy('BustyPetite')
            for url in urls:
                print('sending nude')
                await ctx.send(url)
        else:
            print('11')
            urls = get_one('BustyPetite')
            await ctx.send(urls)
        #print(urls)

    else:
        if what == 'meme' and what2 == 'crazy':

            urls = get_crazy()
            #print(submission.url)
            for url in urls:
                await ctx.send(url)
        else:
            urls = get_one()
            await ctx.send(urls)


#name='', brief='', help='e.g. `.`'
'''@bot.command(name='', brief='', help='e.g. `.`')
async def h(ctx, what='general'):
  #await ctx.send('pong')
  if str(what).lower()=='general':
    for command in commands:
      await ctx.send(command)
  elif str(what).lower() == 'fuse':
    for command in fuse_help_commands:
      await ctx.send(command)'''


@bot.command(
    name='add_user',
    brief='to activate fuse user\'s auto attendance',
    help='get code from https://ioee.herokuapp.com e.g. `.add_user *code*`')
async def add_user(ctx, pseudo_id):
    add_fuse_user(pseudo_id)
    await ctx.send("User {} has been activated successfully.".format(pseudo_id)
                   )


@bot.command(name='check',
             brief='checks if live class has been started',
             help='e.g. `.check`')
async def check(ctx, pseudo_id):
    add_fuse_user(pseudo_id)
    await ctx.send("Sorry mannual checking is unavailable for a while")
    #await test.start(True)


@bot.command(
    name='remove_user',
    brief='to deactivate fuse auto attadance of specific',
    help='get code from https://ioee.herokuapp.com e.g. `.remove_user *code*`')
async def remove_user(ctx, pseudo_id):
    remove_fuse_user(pseudo_id)
    #users = []
    if "users" in db.keys():
        #pseudocode = pseudo_id.split(".remove_user",1)[1].strip()
        remove_fuse_user(pseudo_id)
    await ctx.send("User {} has been removed successfully.".format(pseudo_id))


#------------------------------------------


@bot.command(name='joke',
             brief='to get jokes',
             help='e.g. `.joke`, `.joke 10`')
async def joke(ctx, n=1):
    if n == 1:
        joke = get_joke()
        await ctx.send("\n\n\nJoke:" + str(joke))
    else:
        jokes = list(get_jokes(n))
        for joke in jokes:
            ctx.send("\n\n\nJoke:" + str(joke))


@bot.command(name='jokes',
             brief='to get jokes',
             help='e.g. `.jokes`, `.jokes 10`')
async def jokes(ctx, n=5, subreddit='jokes'):
    await unleash_reddit(subreddit, str(ctx.channel.id), n)


@bot.command(name='riddle', brief='to get a riddle', help='e.g. `.riddle`')
async def riddle(ctx):
    riddle = get_riddles()
    await ctx.send(riddle)


@bot.command(name='quote', brief='to get an inspiring quote', help='e.g. `.`')
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)


@bot.command(name='inspire',
             brief='To get inspirational message',
             help='e.g. `.inspire`')
async def inspire(ctx):
    inspiration = get_quote()
    await ctx.send(inspiration)


@bot.command(name='puns', brief='To get puns', help='e.g. `.puns`')
async def puns(ctx):
    puns = get_puns()
    await ctx.send(puns)


@bot.command(name='one_liners',
             brief='to get one liner jokes',
             help='e.g. `.one_liners`')
async def one_liners(ctx):
    #add_fuse_user()
    await ctx.send("Sorry mannual checking is unavailable for a while")


@bot.command(name='meme',
             brief='to display meme from r/memes',
             help='e.g. `.meme`')
async def meme(ctx, what='memes'):
    embed = await get_one(what)
    await ctx.send(embed=embed)
    #for i,j in get_one():
    #  await ctx.send(i)
    #  await ctx.send(j)


@bot.command(name='memes',
             brief='to display memes from r/memes',
             help='e.g. `.memes 3`')
async def memes(ctx, n=5, subreddit='memes'):
    await unleash_reddit(subreddit, str(ctx.channel.id), n)
    #embed = await get_one(what)
    #await ctx.send(embed=embed)


@bot.command(name='reddit',
             brief='to display subreddit from r/subreddit',
             help='e.g. `.reddit motivation 3`')
async def memes(ctx, subreddit='motivation', n=3):
    await unleash_reddit(subreddit, str(ctx.channel.id), n)


@bot.command(name='deactivate',
             brief='to deactivate the bot',
             help='e.g. `.deactivate`')
async def deactivate(ctx):
    db["responding"] = False
    await ctx.send(
        "Encouragement bot is deactivated.\nPlease enter: .activate to activate."
    )


@bot.command(name='activate', brief='to activate bot', help='e.g. `.activate`')
async def activate(ctx):
    db["responding"] = True
    #await ctx.send("YaY.. I'm turned on baby...")"
    await ctx.send("Encouragement bot is enabled.. sorry for being rude.")


@bot.command(
    name='mute',
    brief=
    'to mute sucesful/unsuccessful attendance attempts of fuse auto attend.',
    help='e.g. `.mute successful`, `.mute unsuccessful`')
async def mute(ctx, what):
    if what == 'unsuccessful':
        db["unsuccessful_logs"] = False
        await ctx.send("unsuccessful attending_logs are muted.")

    elif what == 'successful':
        db["successful_logs"] = False
        await ctx.send(
            "successful attending_log are muted. to unmute please enter: .unmute successful"
        )


@bot.command(
    name='unmute',
    brief=
    'to unmute sucesful/unsuccessful attendance attempts of fuse auto attend.',
    help='e.g. `.unmute successful`, `.unmute unsuccessful`')
async def unmute(ctx, what):
    if what == 'unsuccessful':
        db["unsuccessful_logs"] = True
        await ctx.send("successful attending_logs are unmuted.")

    elif what == 'successful':
        db["successful_logs"] = True
        await ctx.send(
            "usuccessful attending_log are unmuted. to mute please enter: .mute unsuccessful"
        )
    #print('\n\nwhat==\'\'', end=' ')
    #print(what=='')
    #  db["responding"] = False
    #  await message.channel.send("Encouragement bot is deactivated.\nPlease Enter: .activate to activate")


@bot.command(name='list',
             brief='to list the current encouraging messages',
             help='e.g. `.list`')
async def list(ctx, what='encouragements'):
    if what == 'users':
        users = []
        if "users" in db.keys():
            users = list(db["users"])
        await ctx.send('Users:  ' + str(users))

    else:
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = list(db["encouragements"])
        await ctx.send(encouragements)


@bot.command(name='delete',
             brief='To delete encouragement message',
             help='e.g. `.delete Every passsing second is makingyou better`')
async def delete(ctx, index):
    encouragements = []
    if "encouragements" in db.keys():
        index = index.split(".del", 1)[1].strip()
        delete_encouragment(index)
        encouragements = list(db["encouragements"])
    await ctx.send(encouragements)


@bot.command(name='new',
             brief='To add new encouraging message to database',
             help='e.g. `.new Every passsing second is makingyou better`')
async def new(ctx, msg):
    encouraging_message = msg.strip()
    update_encouragements(encouraging_message)
    await ctx.send("New encouraging message added.")


@bot.command(name='avatar',
             brief='To see avatar of specific member in the group',
             help='e.g. `.avatar @Encouragement Bot`')
async def avatar(ctx, *, avamember: discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


# _______________________________________________________________________
# ---------------------------- For Music Bot : https://medium.com/pythonland/build-a-discord-bot-in-python-that-plays-music-and-send-gifs-856385e605a1
# _______________________________________________________________________

import os, youtube_dl
import ffmpeg


@bot.command(
    name='join',
    help='Tells the bot to join the voice channel before playing music ')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(
            ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False, download=False):
        SAVE_PATH = os.path.join(os.getcwd(), 'downloads')
        ydl_opts = {
              'format': 'bestaudio/best',
              'restrictfilenames': True,
              'noplaylist': True,
              'nocheckcertificate': True,
              'ignoreerrors': False,
              'logtostderr': False,
              'quiet': True,
              'no_warnings': True,
              'default_search': 'auto',
              'source_address':
              '0.0.0.0',  # bind to ipv4 since ipv6 addresses  cause issues sometimes
              
              'preferredcodec': [{
                  'key': 'FFmpegExtractAudio',
                  'preferredcodec': 'webm',
                  'preferredquality': '192',
              }],
              
              'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',
        }
        #results = YoutubeSearch(url, max_results=3).to_dict()
        #vid_url = 'https://www.youtube.com' +  results[0]['url_suffix']
        #thumbnails = results[0]['thumbnails']
        #title = results[0]['title']
        #print('vid_url:{}, thumbnails:{}, title:{}, download:{},url:{}'.format(vid_url, thumbnails, title, download, url))
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            data = ydl.extract_info(f"ytsearch:{url}", download=download)['entries'][0]
        
        URL = data['url']
        thumbnails = data['thumbnails']
        title = data['title']
        vid_url = data['webpage_url']
        
        print(URL)
        #Renaming files if downloaded
        if download==True:
            files = os.listdir(os.path.join(os.getcwd(), 'downloads'))
            for file_name in files:
                if not file_name.endswith('.part'):
            
                    # To download files as .mp3
                    #mp3_format = os.path.join(os.getcwd(), 'downloads', file_name.replace(file_name.split('.')[-1], 'mp3'))
                    file_name = os.path.join(os.getcwd(), 'downloads', file_name)
                    os.rename(file_name, title + '.mp3')
        return(URL,thumbnails, title, vid_url)

@bot.command(name='p',
             brief='To play song note: Please enter: `.join` first',
             help="example: `.play gangnam style`")
async def play(ctx, *, url):
    global playing
    playing = url
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(
            ctx.message.author.name))
        return
        
    else:
        channel = ctx.message.author.voice.channel
    try:
      global player
      player = await channel.connect()
    except:
        pass  
    #joined the channel
    try:
        server = ctx.message.guild

        voice_channel = server.voice_client
        #print('voice_channel : ' + str(voice_channel))

        async with ctx.typing():
            URL, thumbnails, title, vid_url = await YTDLSource.from_url(url, loop=bot.loop)
            #to stop playing if already playing another
            player.stop()
            player.play(discord.FFmpegPCMAudio(URL))
            
        print('vid_url:{}, thumbnails:{}, title:{}, URL:{},url:{}'.format(vid_url, thumbnails, title, URL, url))
        embed=discord.Embed(title=title,
        #description=stream['longDesc'],
        color=0x00FFFF,
        url=vid_url)
        embed.set_author(name=ctx.message.author)
        embed.set_thumbnail(url=thumbnails[0]['url'])
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'Added by {ctx.author}')
        
        
        message = await ctx.send(embed=embed)
        emos=['⏸️','⏹️', '⬇️']#['⏮️', '⏸️', '⏹️', '⏭️', '⬇️']
        for emoji in emos:
          await message.add_reaction(emoji)
    except Exception as e:
        print(e)
        await ctx.send("The bot is not connected to a voice channel.")
        








#Downloads videb name/url and returns full filename
async def download_from_youtube(url):
    SAVE_PATH = os.path.join(os.getcwd(), 'downloads')

    ydl_opts = {
        'format': 'bestaudio/best',
        'preferredcodec': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'webm',
        'preferredquality': '192',
        }],'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',
    }
  
    print(' downloading!!! ')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except:
            video = ydl.extract_info(f"ytsearch:{url}", download=True)['entries'][0]
        else:
            video = ydl.extract_info(url, download=False)

    #return video
    #print('type_of'+str(type(video)))
    
    # Didnot work for filename we extracted did not match with actual file_name
    '''file_name=str(video['title'] + '-' +video['id'] + '.'  +video['formats'][3]['ext'])
    file_name = file_name.replace('/','_')
    '''

    files = os.listdir(os.path.join(os.getcwd(), 'downloads'))
    for file_name in files:
        if not file_name.endswith('.part'):
            # To download files as .mp3
            mp3_format = os.path.join(os.getcwd(), 'downloads', file_name.replace(file_name.split('.')[-1], 'mp3'))
            file_name = os.path.join(os.getcwd(), 'downloads', file_name)
  
            os.rename(file_name, mp3_format)
            print('file_name: {}'.format(file_name))
            print('mp3_format: {}'.format(mp3_format))
            
            
            return(mp3_format)

@bot.command(name='d',
             brief='To download song note: Please enter: `.d song name` ',
             help="example: `.d gangnam style`")
async def d(ctx, *, url:str):
    if not 'downloads' in os.listdir():
      os.mkdir('downloads')
    print('Try download')
    
    async with ctx.typing():
          URL, thumbnails, title, vid_url = await YTDLSource.from_url(url, loop=bot.loop, download=True)
                
          full_downloaded_file_name = title + '.mp3'
          
          await ctx.send(file=discord.File(full_downloaded_file_name))
          os.remove(full_downloaded_file_name)
          print(' downloaded!!! ')


@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send(
            "The bot was not playing anything before this. Use play_song command"
        )


@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    await ctx.message.add_reaction('🛑')
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
        voice_client
    #os.remove(
    else:
        await ctx.send("The bot is not playing anything at the moment.")


#To make leave voice channel if bot is alone in voice channel
@bot.event
async def on_voice_state_update(member, before, after):
    print('\n\n Fired on_voice_state_update function \n\n')
    voice_state = member.guild.voice_client
    if voice_state is None:
        # Exiting if the bot it's not connected to a voice channel
        return 

    if len(voice_state.channel.members) == 1:
        await voice_state.disconnect()

@bot.command(aliases=['donation', 'support'])
async def donate(ctx, url: str = 'http://stream.radioparadise.com/rock-128'):
    
    embed=discord.Embed(title='Support:',
    description='''Thank you :-) \nesewa/khalti id:\n 9840445934 \n\n Paytreon:\nhttps://www.patreon.com/join/7095305? \n\n Coinbase:\n https://commerce.coinbase.com/checkout/63a4b635-8510-459f-b091-a4f0697993e6
     
     \n\n
     And please vote for me here: https://top.gg/bot/862191340355715093/vote
     ''',
    color=0x00FFFF,
    #url=stream['url']
    )
    embed.set_author(
        name=ctx.message.author,
        )
    #embed.set_thumbnail(url=stream['image'])
    
    #embed.pfp = author.avatar_url
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'Added by {ctx.author}')
    
    message = await ctx.send(embed=embed)

#_______________________________________________________________________
# ----------------------------- ---------------------------------------
# _______________________________________________________________________
# ----------------------------- FM Player -----------------------------



from discord import FFmpegPCMAudio
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()

#To be implemented
global streams
streams = None
def start_load_streams():
    global streams
    try:
        streams[0]
    except:
        with open('test_fm_list.json','r') as F:    
            streams = json.load(F)


#To get current, next, previous streams
def get_stream(which=None, current=None):
    global streams
    try:
        streams[0]
        print('Streams already defined')
    except:
        with open('test_fm_list.json','r') as F:    
            streams = json.load(F)
        streams = streams['stream_links']
        print(streams)
        
        #global streams_url
        
        #streams=streams['stream_links']
        #streams_url = [i['url'] for i in streams]
        
    finally:
        if current==None:
            current={
                "name": "Radio Nepal",
                "city" : "kathmandu",
                "url": "https://radionepal.news/live/audio/mp3",
                "image": "https://radionepal.gov.np/wp-content/themes/rdnp/images/logo-en.png",
                "desc": "am/sw/fm radio",
                "longDesc": "Radio Nepal, oldest radio of nepal."
            }
        if which=='next':
            nxt = streams.index(current) + 1
            
            # Triggred to get next station at the end of stations list 
            if nxt >= len(streams):
                nxt -= len(streams)
            
            current = streams[nxt]
            print(nxt)
        
        elif which=='prev':
            prev = streams.index(current) - 1
            print(prev)
            
            # Triggred to get previous station at the beginning of stations list
            if prev < 0:
                prev += len(streams)
            
            
            print('current:{}, prev:{}'.format(streams.index(current),prev))
            
            current = streams[prev]
            
        return(current)


@bot.command(aliases=['fm', 'radio'])
async def playfm(ctx, url: str = 'http://stream.radioparadise.com/rock-128'):
    global playing
    playing = "fm"
    global currently_playing_message
    
    global stream
    stream = get_stream()
    #url = "https://radio-streaming-serv-1.hamropatro.com/radio/8050/radio.mp3"
    #url = 'https://radionepal.news/live/audio/mp3'
    #global channel
    channel = ctx.message.author.voice.channel
    global player
    try:
        player = await channel.connect()
    except:
        pass
    player.play(FFmpegPCMAudio(stream['url']))
    #global message
    
    embed=discord.Embed(title=stream['name'],
    description=stream['longDesc'],
    color=0x00FFFF,
    url=stream['url'])
    embed.set_author(
        name=ctx.message.author,
        )
        #icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=stream['image'])
    
    #embed.pfp = author.avatar_url
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'Added by {ctx.author}')
    

    currently_playing_message = await ctx.send(embed=embed)
    #emojis = [':track_previous:', ':pause_button:', ':stop_button:', ':track_next:', ':record_button:', ':arrow_down:']
    emos=['⏮️', '⏸️', '⏹️', '⏭️']#, '⏺️', '⬇️']
    for emoji in emos:
        await currently_playing_message.add_reaction(emoji)

def get_embed(reaction, user, stream):
  embed=discord.Embed(title=stream['name'],
    #description=stream['longDesc'],
    color=0x00FFFF,
    url=stream['url'])
  embed.set_author(
        name=user,
        )
        #icon_url=ctx.message.author.avatar_url)
  embed.set_thumbnail(url=stream['image'])
    
  #embed.pfp = author.avatar_url
  embed.timestamp = datetime.datetime.utcnow()
  embed.set_footer(text=f'Added by {user}')
  return embed

@bot.event
async def on_reaction_add(reaction, user,a=''):
    #embed = reaction.embeds[0]
    #emoji = reaction.emoji
    #print('hii')
    #await reaction.message.add_reaction('♥️')
    global stream
    if not user.bot:
        
        
        # stop emoji
        if str(reaction.emoji) == "⏹️":
            player.stop()
        
        # pause emoji
        elif str(reaction.emoji) == "⏸️":
            if player.is_playing():
                player.pause()
                print('paused')
            else:
                player.resume()
                print('resume')
        
        # next emoji
        elif str(reaction.emoji) == "⏭️":
            if playing=='fm':
              
              print('Playing next, current:{}'.format(stream))
              stream = get_stream('next',stream)
              player.stop()
              player.play(FFmpegPCMAudio(stream['url']))
              
              embed=get_embed(reaction, user, stream)
              await currently_playing_message.edit(embed=embed)
              
            #message.send('Hello World')
            #play_next()
        
        # previous emoji
        elif str(reaction.emoji) == "⏮️":
            if playing=='fm':
              
              print('Playing next, current:{}'.format(stream))
              stream = get_stream('prev', stream)
              player.stop()
              player.play(FFmpegPCMAudio(stream['url']))
              
              embed=get_embed(reaction, user, stream)
              await currently_playing_message.edit(embed=embed)
            
            print('Playing next')

        # download emoji
        elif str(reaction.emoji) == "⬇️":
          if playing!='fm':  
            if not 'downloads' in os.listdir():
                os.mkdir('downloads')
            print('Try download')
    
            async with reaction.message.channel.typing():
                
                URL, thumbnails, title, vid_url = await YTDLSource.from_url(playing, loop=bot.loop, download=True)
                
                full_downloaded_file_name = title + '.mp3'
                
                await reaction.message.channel.send(file=discord.File(full_downloaded_file_name))
                os.remove(full_downloaded_file_name)
                print(' downloaded!!! ')
        else:
          await reaction.message.add_reaction(reaction)
    #print('hii')
    #print(reaction)
    #print(reaction.message)
    #print(user)

    #if user.bot:
    #    return
    #else:
    #  previous_messages = await channel.history(limit=1).flatten()
    #  prev_message.add_reaction('♥️')
    '''if emoji == "emoji 1":
        fixed_channel = bot.get_channel(channel_id)
        await fixed_channel.send(embed=embed)
    elif emoji == "emoji 2":
        #do stuff
    elif emoji == "emoji 3":
        #do stuff
    else:
        return'''


@bot.event
async def on_reaction_remove(reaction, user):
    print('\nremoved reaction\n')
    global stream
    if not user.bot:
        
        
        # stop emoji
        if str(reaction.emoji) == "⏹️":
            player.stop()
        
        # pause emoji
        elif str(reaction.emoji) == "⏸️":
            if player.is_playing():
                player.pause()
                print('paused')
            else:
                player.resume()
                print('resume')
        
        # next emoji
        elif str(reaction.emoji) == "⏭️":
            if playing=='fm':
              
              print('Playing next, current:{}'.format(stream))
              stream = get_stream('next',stream)
              player.stop()
              player.play(FFmpegPCMAudio(stream['url']))
              
              embed=get_embed(reaction, user, stream)
              await currently_playing_message.edit(embed=embed)
              
            #message.send('Hello World')
            #play_next()
        
        # previous emoji
        elif str(reaction.emoji) == "⏮️":
            if playing=='fm':
              
              print('Playing next, current:{}'.format(stream))
              
              stream = get_stream('prev', stream)
              player.stop()
              player.play(FFmpegPCMAudio(stream['url']))
              
              embed=get_embed(reaction, user, stream)
              await currently_playing_message.edit(embed=embed)
            
            print('Playing next')

        # download emoji
        elif str(reaction.emoji) == "⬇️":
          if playing=='fm':  
            if not 'downloads' in os.listdir():
                os.mkdir('downloads')
            print('Try download')
    
            async with reaction.message.channel.typing():
                full_downloaded_file_name = await download_from_youtube(playing)
                await reaction.message.channel.send(file=discord.File(full_downloaded_file_name))
                os.remove(full_downloaded_file_name)
                print(' downloaded!!! ')
        else:
          await reaction.message.add_reaction(reaction)
# _____________________________________________________
# ///////////////////// FM Player /////////////////////
# _____________________________________________________

@bot.command(aliases=['s', 'sto'])
async def stopfm(ctx):
    player.stop()


@bot.command(
    name='disable_unleashing',
    brief='To disable/stop add unleashing all reddit posts to the server',
    help='e.g. `.disable_unleashing`')
async def disable_unleashing(ctx):
    try:
        unleashing.stop()
        await ctx.send('unleashing disabled successfully.')
    except:
        await ctx.send('already disabled.')


@bot.command(
    name='enable_unleashing',
    brief=
    'To enable/start unleashing previously stopped reddit posts to the server',
    help='e.g. `.enable_unleashing`')
async def enable_unleashing(ctx):
    try:
        unleashing.start()
        await ctx.send('unleashing enabled successfully.')
    except:
        await ctx.send('already enabled.')


@bot.command(name='disable_autoattend',
             brief='To start autoattending in fuse classroom.',
             help='e.g. `.start_unleashing`')
async def disable_autoattend(ctx):
    try:
        auto_attend.stop()
        await ctx.send('fuse auto-attend disabled successfully.')
    except:
        await ctx.send('already disabled.')


@bot.command(name='enable_autoattend',
             brief='To enable/stopsrt autoattending in fuse classroom.',
             help='e.g. `.enable_unleashing`')
async def enable_autoattend(ctx):
    try:
        auto_attend.start()
        await ctx.send('fuse auto-attend enabled successfully.')
    except:
        await ctx.send('already enabled.')


@bot.command(name='video_embed_test', brief='', help='e')
async def video(ctx):
    embed = discord.Embed(
        title='title',
        url='https://thumbs2.redgifs.com/WelcomeSweetTadpole-mobile.mp4',
        description='body',
        colour=discord.Color.red())
    embed.set_image(
        url="https://thumbs2.redgifs.com/WelcomeSweetTadpole-mobile.mp4")
    embed.set_video(
        url="https://www.redgifs.com/watch/blissfulimperfectyardant")
    await ctx.send(embed=embed)


'''
async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(id=123456789) # replace with channel_id
    while not client.is_closed():
        counter += 1
        await channel.send(counter)
        print(counter)
        await asyncio.sleep(60) # task runs every 60 seconds''' ''

sad_words = [
    "sad", "depressed", "unhappy", "angry", "miserable", "depressing", "hurt",
    "pain"
]

starter_encouragements = [
    "Cheer up!",
    "You are a great person / bot!",
]

commandss = [
    '\".h fuse\" or \".help fuse\" -> for fuse_auto_attend help',
    'fuse auto-attend registration at: https://ioee.herokuapp.com/',
    '\".inspire\" or \".quote\" -> to display quote ',
    '\".joke\"   -> to display joke',
    '\".meme\"   -> displays best random meme',
    '\".riddle\" -> displays best random riddle',
    '\".puns\"   -> displays best random puns',
    '\".knock knock\" -> displays knock knock joke',
    '\".deactivate\" -> deactivates the bot .activate -> activates the bot',
    '\".new inspirational_message\" -> Adds new inspirationsl message to db',
    '\".del inspirational_message\" -> deletes inspirational message from db',
    '\".list\" -> lists the current inspirational messages',
]

fuse_help_commands = [
    '\".h\" or \".help\" - for general help',
    '----------- ------------------------- -----------',
    'fuse auto-attend registration at: https://ioee.herokuapp.com/',
    '---------------------------------',
    '\".add_user user_token\" -> to add user for auto-fuse attandance',
    '.remove_user user_token -> to remove user',
    '\".list_user\"     -> to list available users',
    '\".check class\" or \".snoop class\" -> checks if live class started.',
    '\".mute unsuccessful\" -> to mute unsuccessful attending_logs. ie. hide \"Live Class not started\" messages',
    '\".mute successful\" -> to mute successful attending_logs ie. hide messages when attended successfully',
    '\".unmute unsuccessful\" -> to unmute unsuccessful attending_logs ie. show \"Live Class not started\" messages',
    '\".umute successful\" -> to unmute successful attending_logs ie. show messages when attended successfully',
]
#from discord.ext import commands

#bot = commands.Bot(command_prefix='.')

#@bot.command()
#async def test(ctx):
#    await ctx.send('I heard you! {0}'.format(ctx.author))
'''print('--------------Test Mode--------------------------------')
print(client.servers)



print('-------------------------------------------------------')'''

if "responding" not in db.keys():
    db["responding"] = True

if "unsuccessful_logs" not in db.keys():
    db["unsuccessful_logs"] = False

if "successful_logs" not in db.keys():
    db["successful_logs"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def get_joke():
    response = requests.get("https://imao.herokuapp.com/jokes/api/random/")
    json_data = response.json()
    joke = str(json_data['title']) + ' : ' + str(
        json_data['body']) + ' - ' + str(json_data['author'])
    return (joke)


def get_jokes(no_of_jokes):
    response = requests.get("https://imao.herokuapp.com/jokes/api/{}/".format(
        int(no_of_jokes)))
    jokes = []
    for joke in response.json()['jokes']:
        jokes.append(
            str(joke['title']) + ' : ' + str(joke['body']) + ' - ' +
            str(joke['author']))
    return (jokes)


def get_puns():
    return ('Puns are comming very very soon!')


def get_riddles():
    return ('Riddles are comming very very soon!')


def add_fuse_user(pseudoid):
    if "users" in db.keys():
        users = db["users"]
        if pseudoid not in users:
            users.append(pseudoid)
        db["users"] = users
    else:
        db["users"] = [pseudoid]


def remove_fuse_user(pseudoid):
    users = list(db["users"])
    #if len(encouragements) > index:
    if pseudoid in users:
        #del encouragements[index]
        users.remove(pseudoid)
        db["users"] = users


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
    encouragements = list(db["encouragements"])
    #if len(encouragements) > index:
    if index in encouragements:
        #del encouragements[index]
        encouragements.remove(index)
        db["encouragements"] = encouragements


def sanitize_db():

    users = list(set(list(db["users"])))
    users_sanitized = []
    for user in users:
        users_sanitized.append(
            user.replace('\'', '').replace('\"', '').strip())
    db["users"] = users_sanitized
    print('Users sanitized. \n Users:')
    print(list(db["users"]))


def attend_each(usr):
    custom_url = 'https:ioee.herokuapp.com/attend/{}/'.format(usr)
    response = requests.get(custom_url)
    return (response.text)


#---------------Working------------------------

# For scrapping quotes every 1 min.

@tasks.loop(minutes=1)
async def start_scrapping():
    with open('quotes.json','r') as f:
        saved_quotes = json.load(f)
    
    # Got saved quotes
    saved_quotes = saved_quotes['quotes']
    
    new_quotes=requests.get('https://zenquotes.io/api/quotes').json()
    
    
    # To combine new and old quotes
    n=0
    for quote in new_quotes:
        if quote not in saved_quotes:
            saved_quotes.append(quote)
            n+=1
    total_quotes = len(saved_quotes)
    with open('quotes.json','w') as file:
        json.dump({'quotes' : saved_quotes}, file, indent = 4)
    print('Saved {} quotes, total:{}'.format(n,total_quotes))



@tasks.loop(minutes=30)
async def auto_attend(mannual_attempt=False):
    intents = discord.Intents.default()
    intents.members = True

    #user= await client.get_user("487904509670337509")
    #await client.send_message(user, "Your message goes here")
    #client.get_user(487904509670337509).send('hi')

    #sanitize_db()
    print("Users: ")
    users = list(db['users'])
    print(users)
    # To limit attend time from 9 am to 5:45
    # i.e. (03:15 to 11:45) UTC

    now = datetime.datetime.now()
    morning = now.replace(hour=3, minute=5, second=0, microsecond=0)
    evening = now.replace(hour=11, minute=45, second=0, microsecond=0)

    #print('hello fella')
    if (now.strftime("%A") != "Saturday") and (now >= morning
                                               and now <= evening):

        channel = bot.get_channel(id=862205194283253763)
        #user = client.get_user("487904509670337509")
        #await user.send_message('hi')
        #username = bot.get_user('861131196779331624')
        #print('bot:')
        #print(username)
        users = []

        if "users" in db.keys():
            users = db["users"]
        for user in users:
            #response = str(attend_each(user))
            custom_url = 'https://ioee.herokuapp.com/attend/{}/'.format(user)
            print(custom_url)
            response = requests.get(str(custom_url))
            response = response.text.strip()
            print(response)
            print(response)

            if response == "Live Class not started" and db[
                    "unsuccessful_logs"] == False and mannual_attempt == False:
                continue

            elif db["successful_logs"] == False and mannual_attempt == False:
                await channel.send(
                    "Successful attending attempt_logs are muted. to unmute please enter: .unmute unsuccessful"
                )

            else:
                try:
                    previous_messages = await channel.history(
                        limit=1).flatten()
                    prev_message = previous_messages[0].content
                    print('previous_message:')
                    print(prev_message)
                except:
                    prev_message = "Your Attendance is done.Discord prevened previous message view"

                if (str(prev_message).strip() != response):
                    #print("mannual_attempt:{} db[\"successful_logs\"]:{}  db[\"unsuccessful_logs\"]:{}  response=={}, response:{}".format(mannual_attempt, db["successful_logs"],db["unsuccessful_logs"], response == "Live Class not started", response ) )

                    print('not same messages:prev_message and rseponse')

                    await channel.send(response)

                    #await channel.send('user:'+str(user))
                else:
                    print('same message as previous message, so not sending')
                    #print(prev_message)
                    #print(response)
                    #print(str(prev_message)==str(response))
                    #print(type(response))
                    pass


#----------- To list discord servers ---------


@tasks.loop(hours=25)
async def share_info():
    intents = discord.Intents.default()
    intents.members = True

    channel = bot.get_channel(id=882664470692909056)
    response = requests.get('http://ioee.herokuapp.com/meroshare/')
    response = response.text.strip()
    print(response)

    try:
        previous_messages = await channel.history(limit=1).flatten()
        prev_message = previous_messages[0].content
        print('previous_message:')
        print(prev_message)
    except:
        pass
    if (str(prev_message).strip() != response):
        print('not same messages:prev_message and rseponse')
        await channel.send(response)

    else:
        print('same message as previous message, so not sending')
        pass


@tasks.loop(hours=25)
async def meroshare(mannual_attempt=False):
    intents = discord.Intents.default()
    intents.members = True

    #user= await client.get_user("487904509670337509")
    #await client.send_message(user, "Your message goes here")
    #client.get_user(487904509670337509).send('hi')

    #sanitize_db()
    #print("Users: ")
    #users=list(db['users'])
    #print(users)
    # To limit attend time from 9 am to 5:45
    # i.e. (03:15 to 11:45) UTC

    now = datetime.datetime.now()
    morning = now.replace(hour=1, minute=00, second=0, microsecond=0)
    evening = now.replace(hour=10, minute=15, second=0, microsecond=0)

    #print('hello fella')
    if (now.strftime("%A") != "Saturday") and (now >= morning
                                               and now <= evening):

        channel = bot.get_channel(id=882655060050444288)
        #user = client.get_user("487904509670337509")
        #await user.send_message('hi')
        #username = bot.get_user('861131196779331624')
        #print('bot:')
        #print(username)
        users = []

        if "users" in db.keys():
            users = db["users"]
        for user in users:
            #response = str(attend_each(user))
            custom_url = 'https://ioee.herokuapp.com/attend/{}/'.format(user)
            print(custom_url)
            response = requests.get(str(custom_url))
            response = response.text.strip()
            print(response)
            print(response)

            if response == "Live Class not started" and db[
                    "unsuccessful_logs"] == False and mannual_attempt == False:
                continue

            elif db["successful_logs"] == False and mannual_attempt == False:
                await channel.send(
                    "Successful attending attempt_logs are muted. to unmute please enter: .unmute unsuccessful"
                )

            else:
                try:
                    previous_messages = await channel.history(limit=1
                                                              ).flatten()
                    prev_message = previous_messages[0].content
                    print('previous_message:')
                    print(prev_message)
                except:
                    prev_message = "Your Attendance is done.Discord prevened previous message view"

                if (str(prev_message).strip() != response):
                    #print("mannual_attempt:{} db[\"successful_logs\"]:{}  db[\"unsuccessful_logs\"]:{}  response=={}, response:{}".format(mannual_attempt, db["successful_logs"],db["unsuccessful_logs"], response == "Live Class not started", response ) )

                    print('not same messages:prev_message and rseponse')

                    await channel.send(response)

                    #await channel.send('user:'+str(user))
                else:
                    print('same message as previous message, so not sending')
                    #print(prev_message)
                    #print(response)
                    #print(str(prev_message)==str(response))
                    #print(type(response))
                    pass


#----------- To list discord servers ---------


class OwnerCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("OwnerCommands Is Ready")

    @bot.command()
    async def servers(ctx):

        discord.Intents.members = True
        activeservers = bot.guilds
        embed = discord.Embed(
            title='Servers and members',
            description='',
            colour=discord.Color.green(),
        )
        '''for guild in activeservers:
            print('guild.channels')
            print(guild.channels)
            embed.add_field(
            name = str(guild.name) + ' ({}) own({})'.format(guild.member_count, guild.owner),
            value=str([i.name  for i in guild.members]),
            )
        '''
        print('members:')
        for i in bot.guilds[1:]:
            a = i.fetch_members(limit=None)

            aa = []
            async for ii in a:
                aa.append(ii.name)
                #print(i, ii)

            embed.add_field(name=str(i) +
                            ' ({}) own({})'.format(i.member_count, i.owner),
                            value=str(aa))
        await ctx.send(embed=embed)
        #print(a)
        #  print(channel)

        #await ctx.send(guild.name)
        #print(guild.name)


def setup(client):
    bot.add_cog(OwnerCommands(bot))


#-------------------------


async def unleash_reddit_jokes(subreddit, channel_id, no_of_posts=7):
    channel = bot.get_channel(id=int(channel_id))
    for n, submission in enumerate(
            reddit.subreddit('jokes').top('day', limit=int(no_of_posts / 2))):
        print('Unleash for loop:{}'.format(n))
        title = submission.title
        body = submission.selftext
        embed = discord.Embed(title=title,
                              url=submission.url,
                              description=body,
                              colour=discord.Color.blue())
        embed.set_image(url=submission.url)
        await channel.send(embed=embed)

    for n, submission in enumerate(
            reddit.subreddit('jokes').hot(limit=no_of_posts -
                                          int(no_of_posts / 4))):
        print('Unleash for loop:{}'.format(n))
        title = str(submission.title)[:256]
        body = submission.selftext
        embed = discord.Embed(title=title,
                              url=submission.url,
                              description=body,
                              colour=discord.Color.blue())
        await channel.send(embed=embed)

    for n, submission in enumerate(
            reddit.subreddit('jokes').new(limit=no_of_posts -
                                          math.ceil(no_of_posts / 4))):
        print('Unleash for loop:{}'.format(n))
        title = submission.title
        body = submission.selftext
        embed = discord.Embed(title=title,
                              url=submission.url,
                              description=body,
                              colour=discord.Color.blue())
        await channel.send(embed=embed)


async def unleash_reddit(subreddit, channel_id, no_of_posts=5):
    channel = bot.get_channel(id=int(channel_id))
    submissions = await reddit.subreddit(subreddit)
    donot_proceed = 0
    #To display hot post if only one is to be fetched
    if no_of_posts == 1:
        donot_proceed = 1
        no_of_posts = 2

    async for submission in submissions.hot(limit=int(no_of_posts / 4)):
        print('Unleash for loop:{}'.format(0))
        title = submission.title
        body = submission.selftext
        embed = discord.Embed(title=title,
                              url=submission.url,
                              description=body,
                              colour=discord.Color.red())
        embed.set_image(url=submission.url)
        print('Submission_url: ', submission.url)
        try:
            #To filter lenthy messages > 2500 letters
            if len(str(body)) < 2500:
                image_formats = ['jpg', 'jpeg', 'png']

                #checks if image_format in submission.url
                if sum([(i in str(submission.url)) for i in image_formats]):
                    await channel.send(embed=embed)
                else:
                    await channel.send(submission.url)
        except:
            pass

    if donot_proceed != 1:
        async for submission in submissions.top('day',
                                                limit=int(no_of_posts / 2)):
            print('Unleash for loop:{}'.format('n'))
            title = submission.title
            body = submission.selftext
            embed = discord.Embed(title=title,
                                  url=submission.url,
                                  description=body,
                                  colour=discord.Color.red())
            embed.set_image(url=submission.url)
            print('Submission_url: \"', submission.url, '\"')
            if submission.url == '':
                print('Guess What')
            try:
                if len(str(body)) < 2500:
                    image_formats = ['jpg', 'jpeg', 'png']
                    #checks if image_format in submission.url
                    if sum([(i in str(submission.url))
                            for i in image_formats]):
                        await channel.send(embed=embed)
                else:
                    await channel.send(submission.url)
            except:
                pass
        async for submission in submissions.new(limit=no_of_posts -
                                                math.ceil(no_of_posts / 4)):
            print('Unleash for loop:{}'.format(0))
            title = submission.title
            body = submission.selftext
            embed = discord.Embed(title=title,
                                  url=submission.url,
                                  description=body,
                                  colour=discord.Color.red())
            embed.set_image(url=submission.url)
            print('Submission_url: ', submission.url)
            try:
                if len(str(body)) < 2500:
                    image_formats = ['jpg', 'jpeg', 'png']
                    #checks if image_format in submission.url
                    if sum([(i in str(submission.url))
                            for i in image_formats]):
                        await channel.send(embed=embed)
                else:
                    await channel.send(submission.url)
            except:
                pass


'''
async def unleash_reddit(subreddit, channel_id, no_of_posts=5):
  channel = bot.get_channel(id=int(channel_id))
  submissions_top = await reddit.subreddit(subreddit)
  submissions_hot = await reddit.subreddit(subreddit)
  submissions_new = await reddit.subreddit(subreddit)
  
  #30% top, 40%hot, 30%new
  for i in range(0, no_of_posts):
    print('Unleash for loop:{}'.format(i))
    
    if i < int(no_of_posts/3):
      submission=random.choice([x async for x in submissions_top.top(limit=25)])
      print(a)
      ''async for x in submissions_top.top(limit=15):
        if not x.stickied:
          submission = x
      #submission = next(x async for x in submissions_top.top('all') if not x.stickied)''
    
    elif i < int(no_of_posts/7):
      #submission = next(x async for x in submissions_hot.hot('all') if not x.stickied)
      submission=random.choice([x async for x in submissions_top.hot(limit=35)])
    else:
      #submission = next(x async for x in submissions_new.new('all') if not x.stickied)
      submission=random.choice([x async for x in #submissions_top.new(limit=15)])
    embed=discord.Embed(
    title=submission.title,
    description=submission.selftext,
        
    #description=submission.title,
    colour=discord.Color.green())
    embed.set_image(url=submission.url)  
    await channel.send(embed=embed)'''


@tasks.loop(hours=6)
async def unleashing():
    print('\nstart Unleashing')
    intents = discord.Intents.default()
    #discord.Intents.members = True
    intents.members = True
    intents.all()

    for channel_id in dict(db['unleash']).keys():
        for each_subreddit in db['unleash'][str(channel_id)]:
            await unleash_reddit(each_subreddit, str(channel_id), 10)
            print('Unleashed')






@bot.event
async def on_ready():
    print('We have logged in as \"{0.user.name}\"'.format(bot))
    print(bot.user.id)

    #For fuse attendance trying
    #auto_attend.start()

    #For viewing share_info
    #share_info.start()

    #for unleashing from reddit
    unleashing.start()
    start_scrapping.start()
    game = discord.Game("Chilling out.")
    streaming = discord.Streaming(name='pubg lite',
                                  url="https://www.twitch.tv/caterpileer")
    #movie.url="https://thumbs2.redgifs.com/WelcomeSweetTadpole-mobile.mp4"
    await bot.change_presence(status=discord.Status.online, activity=streaming)
    #await bot.process_commands(message)


@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('.guess'):
        await message.channel.send('Guess a number between 1 to 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await bot.wait_for('message', timeout=5.0, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await message.channel.send(fmt.format(answer))
            return
        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send(
                'Sorry. It is actually {}.'.format(answer))
    else:

        if message.guild is None and message.author != bot.user:
            #await channel.send(str(message.author) + str(message.content))

            embed = discord.Embed(title=message.author,
                                  description=message.content)
            channel = bot.get_channel(id=873477235477184522)
            await channel.send(embed=embed)

        print(str(message.content))
        if any(word in str(message) for word in sad_words):
            options = starter_encouragements
            if "encouragements" in db.keys():
                #print(list(db["encouragements"]))
                options = options  #+ list(db["encouragements"])
                await message.channel.send(random.choice(options))

    await bot.process_commands(message)
    #await message.channel.send('hello')
    #if message!='fuck':
    #  await message.add_reaction('♥️')
    #  return
    '''print('Author_id:')
  print(message.author.id)
  #message.author.send_message('hi')
  print('Hello')

  msg = message.content.strip()
  if msg==".help" or msg == '.h':
    for command in commands:
      await message.channel.send(command)
  
  elif msg==".help fuse" or msg == '.h fuse':
    for command in fuse_help_commands:
      await message.channel.send(command)

  elif msg.startswith(".add_user"):
    pseudocode = msg.split(".add_user",1)[1].replace('\"','').replace('\'','').strip()
    add_fuse_user(pseudocode)
    await message.channel.send("User {} has been added/activated successfully.".format(pseudocode))
  elif msg.startswith(".remove_user"):
    users = []
    if "users" in db.keys():
      pseudocode = msg.split(".remove_user",1)[1].strip()
      remove_fuse_user(pseudocode)
    await message.channel.send("User {} has been removed successfully.".format(pseudocode))
  elif msg==".snoop class" or msg==".check class" or message == ".check live-class" or message == ".check live_class" or message == ".check live class":
    await message.channel.send("Sorry mannual checking is unavailable for a while");
    await test.start(True)
    
    \'''if db["successful_logs"] == False:
      await message.channel.send("Successful attending attempt_logs are muted. to unmute please enter: .unmute unsuccessful")

    await message.channel.send("Checking Live Classes: ")
    m = test_mannual()
    await message.channel.send(m)\'''

  elif msg.startswith(".deactivate"):
    #switch = msg.split(".deac ",1)[1].lower()
    db["responding"] = False
    await message.channel.send("Encouragement bot is deactivated.\nPlease Enter: .activate to activate")
  elif  msg.startswith(".activate"):
    db["responding"] = True
    await message.channel.send("Encouragement bot is activated.\nPlease enter: .deactivate to deactivate.")
  
  elif msg == (".mute unsuccessful") or msg == (".mute unsuccessful logs"):
    db["unsuccessful_logs"] = False
    await message.channel.send("unsuccessful attending_logs are muted.")
  
  elif msg == (".unmute unsuccessful") or msg == (".unmute unsuccessful logs"):
    db["unsuccessful_logs"] = True
    await message.channel.send("unsuccessful attending_logs are unmuted.")

  elif msg == (".mute successful") or msg == (".mute successful logs"):
    db["successful_logs"] = False
    await message.channel.send("successful attending_log are muted. to unmute please enter: .unmute successful")
  
  elif msg == (".unmute successful") or msg == (".unmute successful logs"):
    db["successful_logs"] = True
    await message.channel.send("successful attending_logs are unmuted.")
  
  if db["responding"]:
    if msg == ".list_users" or msg == ".list_user":
      users = []
      if "users" in db.keys():
        users = list(db["users"])
      await message.channel.send('Users:  '+str(users))

    elif msg.startswith('.inspire') or msg.startswith('.quote'):
      quote = get_quote()
      await message.channel.send(quote)
    elif msg.startswith('.joke'):
      if msg == '.joke':
        joke = get_joke()
        await message.channel.send("\n\n\nJoke:" + str(joke))
      else:
        try:
          n = int(msg.split(' ')[1].strip())
        except:
          n = int(msg.split(' ')[2].strip())
        jokes = list(get_jokes(n))
        for joke in jokes:
          await message.channel.send("\n\n\nJoke:" + str(joke))
    
    elif msg.startswith('.riddle'):
      riddle = get_riddles()
      await message.channel.send(riddle)
     
    elif msg.startswith('.puns'):
      puns = get_puns()
      await message.channel.send(puns)
    elif msg.startswith('.memes') or msg.startswith('.knock knock'):
      await message.channel.send('Sorry! ' + str(msg) + ' are comming very very soon!' )
  
    



    
    elif msg.startswith(".new"):
      encouraging_message = msg.split(".new ",1)[1].strip()
      update_encouragements(encouraging_message)
      await message.channel.send("New encouraging message added.")
    elif msg.startswith(".del"):
      encouragements = []
      if "encouragements" in db.keys():
        index = msg.split(".del",1)[1].strip()
        delete_encouragment(index)
        encouragements = list(db["encouragements"])
      await message.channel.send(encouragements)
    elif msg.startswith(".list"):
      encouragements = []
      if "encouragements" in db.keys():
        encouragements = list(db["encouragements"])
      await message.channel.send(encouragements)'''


keep_alive()
bot.run(os.environ['TOKEN'])
#client.loop.create_task(my_background_task())
bot.run('token')  #
