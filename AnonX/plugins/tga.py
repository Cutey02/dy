from AnonX import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **I love you 🤗** ",
           "Im waiting for u 😒🫂",
           "I miss u 🚶‍♀️",
           "Ur always mine 🤗",
           "Who r u? 🤔",
           "Shutup! ☀️",
    "ur looking beautiful 𓆩🥰𓆪 ",
    "lets go for ride 🏍 "
    "go and sleep 💤",
    "call the owner ☎️ it's urgt", 
    "work out 🏋🚴💪 panu body healthy ah iruku",
    "same pinch hifi🙌",
    "vanakam 🙏🏼",
    "𝙥𝙤𝙙𝙖𝙖 𝙥𝙖𝙣𝙞𝙞𝙞 ᥬ🤣",
    " A true love story never ends🥰",
    "Come near now, and kiss me 👩‍❤️‍👨",
    "𝙒𝙝𝙖𝙩 𝙙𝙤 𝙪 𝙚𝙭𝙥𝙚𝙘𝙩𝙖𝙩𝙞𝙤𝙣𝙨 𝙞𝙣 𝙡𝙤𝙫𝙚? ❤️",
    "Love is being stupid together🤗👭",
    "Love is sharing your popcorn🍿",
    "𝙎𝙤𝙢𝙚𝙩𝙞𝙢𝙚𝙨 𝙮𝙤𝙪 𝙟𝙪𝙨𝙩 𝙣𝙚𝙚𝙙 𝙖 𝙗𝙧𝙚𝙖𝙠 😔💔",
    "𝙤𝙞𝙞 𝗜 𝘄𝗮𝗻𝘁 𝘂"
    " 𝙊𝙞𝙞 𝙈𝙖𝙢𝙖𝙠𝙪𝙩𝙩𝙮𝙮𝙮",
    "𝙄 𝙣𝙚𝙚𝙙 𝙮𝙤𝙪 𝙡𝙞𝙠𝙚 𝙖 𝙝𝙚𝙖𝙧𝙩 𝙣𝙚𝙚𝙙𝙨 𝙖 𝙗𝙚𝙖𝙩 💖",
    "My wish is that you may be loved to the point of madness 😊😄",
    "All you need is love! 👏🎉",
    "He is not a lover who does not love forever 🥺💗",
    "Love is the magician that pulls man out of his own hat 💕✨",
    "Romance is the glamour which turns the dust of everyday life into a golden haze 😍👀",
    "Love is an ocean of emotions entirely surrounded by expenses! 🌈🌟",
    "Let the beauty of what you love be what you do🌹💖",
    "Your crazy matches my crazy🤭😅",
    "Life is the flower for which love is the honey 😌🌸",
    "Besides chocolate🍫 you r my favorite💓💞",
    "We can only learn to love by loving 😊🌼",
    "Tell me whom you love and I will tell you who you are 🌞😄",
    "Sometimes your cuteness kills me 💘",
    "You stole my heart at first sight 💭💖",
    "OMG your eyes are beautiful 😍❤️",
    "Tumhare pyar mein doobne ka ahsas advitiya hai 💕🌊",
    "Hey beautiful 😍 I love your sense of humour? 😃✨",
    "Your eyes are gorgeous 😍 they kill me! 💖",
    "Pain of love lasts a lifetime 😔💔",
    "Do a favour for me by keeping that beautiful smile 🌱💗",
    "Can you take me on an adventure?",
    "My heart stops when you look at me💞",
    "Dont make the process harder than it is 🙏💪",
    "I look at you and see the rest of my life in front of my eye 💖💭",
    "The sadness will last forever 💔💕",
    "Our greatest joy and our greatest pain come in our relationships with others 💁‍♀️💖",
    "Love is composed of a single soul inhabiting two bodies😍🔥",
    "If I know what love is, it is because of you🌈💫",
    "My name sounds even cuter with your last name added to it💪❤️",
    "I like to be alone But I would rather be alone with you 😄✨",
    "Love is not only something you feel, it is something you do👀💞",
    "Your love shines in my heart as the sun that shines upon the earth🌈🌍",
    "Sometimes I look at you and I wonder how I got to be so damn lucky 💖🏡",
    "My soul sees its equal in you🙏🥰",
    "Absence makes the heart grow fonder, but it sure makes the rest of you lonely🌙💫",
    "I love you right up to the moon and back 💖⏳",
    "i carry your heart with me 🌞😊",
    "Love will travel as far as you let it It has no limits💓💓",
    "Being with you and not being with you is the only way I have to measure time 🌈💕",
    "Love is a friendship set to music🎶💗",
    "Close together or far apart you r forever in my heart 💔😔",
    "Always follow your heart but remember to bring your brain along! 💭💖",
    "I want someone who will look at me the same way I look at chocolate cake 😄💓",
    "Tumhare pyar mein doobna advitiya hai 💕🌊",
    "If you think missing me is hard, you should try missing you💔😔",
    "Tum mere dil ki raani ho, main tumhara rajkumari 💖👑",
    "I lost my teddy bear, can I sleep with you?👀🔍",
    "Do you believe in love at first sight or should I walk by again?💖🌟",

    "Everything I do, I do it for you 🤗💞",

    "I think you are suffering from a lack of vitamin ME💖",
    "Tumhare bina jeena adhura hai 💔😔",
    "Are you a magician? Because whenever I look at you everyone else disappears!💖",
    "Everyday I fall in love with you more and more😊💓",
    "I want to be the reason you look down at your phone and smile 💖📲",
    "Tumhare bina mera jeevan adhura hai 🌈💔",
    "You are just like bacon beer and chocolate you make everything better😃✨",
    "Together with you is my favorite place to be 💖🌹",
    "Her idea of a romantic setting is one that has a diamond in it👀🌿",
    "Make yourself ready for love to overflow in your life ❤️",
    "Let's be weird and wonderful together 💕🌟",
    "When someone elses happiness is your happiness that is love 💖🌈",
    "Good thing I brought my library card because I'm totally checking you out 💓😄",
    "One day the plane ticket will be one way! 🌍✈️",
    "Folks are usually about as happy as they make their minds up to be! 🤗❓",
    "Love means to see the one you love happy",
    "Happiness is holding someone in your arms and knowing you hold the whole world🥰",
    "Happiness is the nectar love is the Bee",
    "I always wish to be with you 🤗💕",
    "Your smile makes my day beautiful 😊🌺",
    "Everything seems small in front of your love 💖✨",
    "My dreams are incomplete without you 💭💔",
    "Listening to the words of your heart increases my brightness 💓🕯️",
    "Every day with your love is a special gift 🎁💞",
    "Your laughter brightens up my life 😃💖",
    "My life is incomplete without you 📖💔",
    "Your love has found a place in my heart 💖❤️",
    "I want to always be happy with you 😊💞",
    "My dream comes true in your eyes 👀✨",
    "My life becomes colorful with your love 🌈💖",
    "My world is empty without you 😔🌙",
    "I wish to be the star of your eyes 💫💕",
    "I want to make every moment spent with you memorable 🥰🌺",
    "Your laughter brings brightness to the day 😄✨",
    "Your love gives peace to my heart 💖😌",
    "My life is incomplete without you 💔🌸",
    "Your eyes show true love for me 👀❤️",
    "Every dream of mine comes true with your love 💞🌟",
    "I will always remember the moments spent with you 😊💖",
    "Your smile is the greatest joy of my life 😃🌈",
    "I want to always have a place in your heart 💓💞",
    "Your love is a blessing from God to my life 💖🙏",
    "My life is nothing without you 😔💔",
    "You are the heartbeat of my heart, there is nothing without you 💖❤️",
    "I lose myself in your love 💕🌟",
    "I want to always stay happy with you 😊💃",
    "Your laughter is very dear to my heart 😄💖",
    "My life is incomplete without your love 💔🌹",
    "The twinkle in your eyes surprises my heart ✨💓",
    "I feel complete in your love 💖😍",
    "My life feels empty without you 😔💔",
    "Your smile brightens up the day 😊✨",
    "I find the joy of heaven in your love 💖🌟",
    "I will always remember the moments spent with you 🥰💞",
    "Your laughter is the sweetness of my life 😄💖",
    "Your love will always remain connected to my heart 💓🔗",
    "My life is incomplete without you 💔🌸",
    "Your eyes reflect true love 👀🌍",
    "With your love, I write a new story every day 💖📖",
    "Your laughter gives happiness to my heart 😃💓",
    "I feel the completeness of my life in your love 💕🌟",
    "My life becomes meaningless without you 😔💔",
    "You are the most important part of my life 💖❤️",
    "Every dream of mine comes true with your love 🌈💞",
    "Every moment spent with you is filled with happiness 😊🌺",
    "Your laughter gives peace to my heart 😄💖",
    "Your love has made my life colorful 🌟🎨",
    "My life is barren without you 💔🌸",
    "Your eyes show true love 👀💖",
    "With your love, I feel complete 💕😍",
    "I want to always stay in happiness with you 😊💞",
    "Your laughter is the rain of my heart 🌧️💓",
    "Your love will always remain connected to my heart 💖😌",
    "My life is incomplete without you 💔🌹",
    "Your eyes show true love 👀❤️",
    "With your love, every day is a special gift 💖🎁",
    "Your smile brightens up my life 😃💖",
    "Everything seems small in front of your love 💖✨",
    "My dreams are incomplete without you 💭💔",
    "Listening to the words of your heart increases my brightness 💓🕯️",
    "Every day with your love is a special gift 🎁💞",
    "Your laughter brightens up my life 😃💖",
    "My life is incomplete without you 💔🌸",
    "Your love has found a place in my heart 💖❤️",
    "I want to always be happy with you 😊💞",
    "My dream comes true in your eyes 👀✨",
    "My life becomes colorful with your love 🌈💖",
    "My world is empty without you 😔🌙",
    "I wish to be the star of your eyes 💫💕",
    "Every dream of mine comes true with your love 💞🌟",
    "I will always remember the moments spent with you 😊💖",
    "Your smile is the greatest joy of my life 😃🌈",
    "I want to always have a place in your heart 💓💞",
    "Your love is a blessing from God to my life 💖🙏",
    "My life is nothing without you 😔💔",
    "You are the heartbeat of my heart, there is nothing without you 💖❤️",
    "I lose myself in your love 💕🌟",
    "I want to always stay happy with you 😊💃", 
         ]

@app.on_message(filters.command(["all"], prefixes=["@"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        return await message.reply("This command can be used in groups and channels!")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("**ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!**")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall hello 👈** ᴛʀʏ ᴛʜɪs ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...*")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall hii 👈 **ᴛʀʏ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ...**")
    else:
        return await message.reply("/tagall hii 👈 **ᴛʀʏ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ...**")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["cancel", "stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("**ɴᴏ ᴀᴄᴛɪᴠᴇ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss ɪs sᴛᴀʀᴛᴇᴅ ʙʏ ᴍᴇ...**")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs. ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ...**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("**ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ**")
