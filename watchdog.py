# Telethon Libs
import telethon
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins

# Python Libs
import json

# Initialize Logging
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Import Keys
from keys import (API_ID, API_HASH, BOT_TOKEN, BOT_NAME,
                    GROUPS_PATH, GROUP_ADMIN_PATH, PM_USERS_PATH)
# Import Lock Messages
from lockTypes import (LOCKTYPES, NO_LOCKTYPE_ERROR, SUCCESSFULL_LOCK, SUCCESSFULL_UNLOCK,
                        LOCKTYPE_LIST, SPECIFY_LOCK, SPECIFY_UNLOCK, ALL_LOCKED, ALL_UNLOCKED,
                        LOCK_STATES, HELP_MESSAGE, USE_IN_GROUP)
# Import fill files
from fill_files import fill_files
# Import Check Message
from check_message import check_new_group_message, check_delete_message

# Read Settings and Configs
with open(GROUPS_PATH, encoding='UTF-8') as json_file:
    groups_config = json.load(json_file)

with open(GROUP_ADMIN_PATH, encoding='UTF-8') as json_file:
    admins = json.load(json_file)

with open(PM_USERS_PATH, encoding='UTF-8') as json_file:
    users = json.load(json_file)

# Initialize Telethon
bot = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
logging.info("Initialized Bot.")

# Delete Action Events
@bot.on(events.ChatAction)
async def delete_events(event):
    await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])

# Event for New Messages From Users
@bot.on(events.NewMessage())
async def delete_messages(event: telethon.events.newmessage.NewMessage.Event):
    text_of_message = event.message.text
    if event.is_private:
        if str(event.sender_id) not in users:
            users[str(event.sender_id)] = 1
            with open(PM_USERS_PATH, 'w', encoding='UTF-8') as file:
                json.dump(users, file)
        return

    # Get Channel ID
    try:
        sender = event.original_update.message.from_id.channel_id
        return
    except:
        pass

    # Init New Group
    await check_new_group_message(bot, event, groups_config, admins)

    # Check Message and Delete
    await check_delete_message(bot, event, text_of_message, groups_config, admins)

# Event for Edited Messages From Users
@bot.on(events.MessageEdited())
async def delete_edited(event: telethon.events.newmessage.NewMessage.Event):
    text_of_message = event.message.text
    if event.is_private:
        if str(event.sender_id) not in users:
            users[str(event.sender_id)] = 1
            with open(PM_USERS_PATH, 'w', encoding='UTF-8') as file:
                json.dump(users, file)
        return

    # Get Channel ID
    try:
        sender = event.original_update.message.from_id.channel_id
        return
    except:
        pass

    # Init New Group
    await check_new_group_message(bot, event, groups_config, admins)

    # Check Message and Delete
    await check_delete_message(bot, event, text_of_message, groups_config, admins)

# Kick/Delete when user joins group
@bot.on(events.ChatAction())
async def delete_actions(event: telethon.events.chataction.ChatAction.Event):
    admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
    # Delete the Join Message
    await event.delete()
    await bot.delete_messages(entity=event.chat_id, message_ids=[event.action_message])

    # Create Admin array
    admin_ids = []
    for i in admin_list:
        admin_ids.append(i.id)

    with open(GROUP_ADMIN_PATH, 'w', encoding='UTF-8') as file:
        json.dump(admins, file)

    try:
        sender = event.action_message.from_id.user_id
    except:
        sender = ''
        pass

    if event.user_joined and groups_config[str(event.chat_id)]["locks"]["kick"]:
        try:
            await bot.kick_participant(entity=event.chat, user=event.user_id)
            return
        except Exception as e:
            pass

    if event.user_added:
        if sender not in admin_ids and groups_config[str(event.chat_id)]["locks"]["kick"]:
            try:
                kick_msg = await bot.kick_participant(entity=event.chat, user=event.user_id)
                await bot.delete_messages(entity=event.chat_id, message_ids=kick_msg)
            except:
                pass

# Locks Command
@bot.on(events.NewMessage(pattern='^/lock '))
async def lock(event: telethon.events.newmessage.NewMessage.Event):
    try:
        sender = event.original_update.message.from_id.channel_id
        return
    except:
        pass

    if event.is_private:
        if str(event.sender_id) not in users:
            users[str(event.sender_id)] = 1
            with open(PM_USERS_PATH, 'w', encoding='UTF-8') as file:
                json.dump(users, file)

        return

    admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
    admin_ids = []
    for i in admin_list:
        admin_ids.append(i.id)

    if event.sender_id not in admin_ids:
        return

    if event.chat_id not in groups_config:
        admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
        fill_files(event, groups_config, admins, admin_list)

    locktype = " ".join(event.raw_text.split()[1:])

    if locktype == "all":
        for i in groups_config[str(event.chat_id)]["locks"]:
            groups_config[str(event.chat_id)]["locks"][i] = True
        await event.respond(ALL_LOCKED)
        return

    if locktype not in LOCKTYPES:
        await event.reply(message=NO_LOCKTYPE_ERROR.format(locktype))
    else:
        groups_config[str(event.chat_id)]["locks"][locktype] = True
        await event.reply(message=SUCCESSFULL_LOCK.format(locktype))

    admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
    admin_ids = []
    for i in admin_list:
        admin_ids.append(i.id)

    admins[str(event.chat_id)] = admin_ids

    with open(GROUP_ADMIN_PATH, 'w', encoding='UTF-8') as file:
        json.dump(admins, file)

# Unlock Command
@bot.on(events.NewMessage(pattern='^/unlock '))
async def unlock(event: telethon.events.newmessage.NewMessage.Event):
    if event.is_private:
        if str(event.sender_id) not in users:
            users[str(event.sender_id)] = 1
            with open(PM_USERS_PATH, 'w', encoding='UTF-8') as file:
                json.dump(users, file)
        await event.reply(USE_IN_GROUP)
        return
    try:
        sender = event.original_update.message.from_id.channel_id
        return
    except:
        pass

    if event.chat_id not in groups_config:
        admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
        fill_files(event, groups_config, admins, admin_list)

    admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
    admin_ids = []
    for i in admin_list:
        admin_ids.append(i.id)

    if event.sender_id not in admin_ids:
        return

    locktype = " ".join(event.raw_text.split()[1:])

    if locktype == "all":
        for i in groups_config[str(event.chat_id)]["locks"]:
            groups_config[str(event.chat_id)]["locks"][i] = False
        await event.respond(ALL_UNLOCKED)
        return

    if locktype not in LOCKTYPES:
        await event.reply(message=NO_LOCKTYPE_ERROR.format(locktype))
    else:
        groups_config[str(event.chat_id)]["locks"][locktype] = False
        await event.reply(message=SUCCESSFULL_UNLOCK.format(locktype))

    with open(GROUPS_PATH, 'w', encoding='UTF-8') as file:
        json.dump(groups_config, file)

    admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
    admin_ids = []
    for i in admin_list:
        admin_ids.append(i.id)

    admins[str(event.chat_id)] = admin_ids

    with open(GROUP_ADMIN_PATH, 'w', encoding='UTF-8') as file:
        json.dump(admins, file)

# Return List of LockTypes
@bot.on(events.NewMessage(pattern='^/locktypes'))
async def locktypes_func(event: telethon.events.newmessage.NewMessage.Event):
    try:
        sender = event.original_update.message.from_id.channel_id
        return
    except:
        pass

    if event.is_private:
        if str(event.sender_id) not in users:
            users[str(event.sender_id)] = 1
            with open(PM_USERS_PATH, 'w', encoding='UTF-8') as file:
                json.dump(users, file)

    admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
    admin_ids = []
    for i in admin_list:
        admin_ids.append(i.id)

    if event.sender_id not in admin_ids:
        return

    list_of_locktypes = ""
    if event.raw_text == "/locktypes" or event.raw_text == "/locktypes" + BOT_NAME:
        for i in LOCKTYPES:
            list_of_locktypes += "- `{}`\n".format(i)

    await event.reply(message=LOCKTYPE_LIST.format(list_of_locktypes))

# Unlocking Error
@bot.on(events.NewMessage(pattern='^/'))
async def unlock_error(event: telethon.events.newmessage.NewMessage.Event):
    try:
        sender = event.original_update.message.from_id.channel_id
        return
    except:
        pass

    if event.raw_text.startswith("/locktypes"):
        return

    if event.is_private:
        if str(event.sender_id) not in users:
            users[str(event.sender_id)] = 1
            with open(PM_USERS_PATH, 'w', encoding='UTF-8') as file:
                json.dump(users, file)
        await event.reply(USE_IN_GROUP)
        return

    admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
    admin_ids = []

    for i in admin_list:
        admin_ids.append(i.id)

    if event.sender_id not in admin_ids:
        return

    if event.raw_text == "/lock" or event.raw_text == "/lock" + BOT_NAME:
        await event.reply(message=SPECIFY_LOCK)
    elif event.raw_text == "/unlock" or event.raw_text == "/unlock" + BOT_NAME:
        await event.reply(message=SPECIFY_UNLOCK)
    elif event.raw_text == "/locks" or event.raw_text == "/locks" + BOT_NAME:
        global groups_config
        result = ""
        for i in groups_config[str(event.chat_id)]["locks"]:
            result += "`{}` - {}\n".format(i, groups_config[str(event.chat_id)]["locks"][i])
        await event.reply(message=LOCK_STATES.format(result))

# Return Helper Function
@bot.on(events.NewMessage(pattern='^/help'))
async def helper_func(event: telethon.events.newmessage.NewMessage.Event):
    try:
        sender = event.original_update.message.from_id.channel_id
        return
    except:
        pass

    admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
    admin_ids = []
    for i in admin_list:
        admin_ids.append(i.id)

    # If Not An Admin
    if event.sender_id not in admin_ids:
        return

    list_of_locktypes = ""
    if event.raw_text == "/locktypes" or event.raw_text == "/locktypes" + BOT_NAME:
        for i in LOCKTYPES:
            list_of_locktypes += "- `{}`\n".format(i)

    # Send the Help
    if event.raw_text == "/help" or event.raw_text == "/help" + BOT_NAME:
        await event.reply(message=HELP_MESSAGE)

    await event.reply(message=LOCKTYPE_LIST.format(list_of_locktypes))

# Run bot Until Disconnected
bot.run_until_disconnected()