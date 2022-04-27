# Telethon
from telethon.tl.types import ChannelParticipantsAdmins
# Import is_functions
from is_functions import (is_hashtag, is_greeting, is_call_to_pm, is_command, is_username,
                            is_email, is_location, is_url, is_phone, is_more_than_1000)
# Import fill
from fill_files import fill_files

# Check New Group Message
async def check_new_group_message(bot, event, groups_config, admins):
    # Init New Group
    if str(event.chat_id) not in groups_config:
        admin_list = await bot.get_participants(event.chat, filter=ChannelParticipantsAdmins)
        fill_files(event, groups_config, admins, admin_list)

# Check Message and delete according to locks
async def check_delete_message(bot, event, text_of_message, groups_config, admins):
    # Check Forwarded
    if event.fwd_from and groups_config[str(event.chat_id)]["locks"]["forward"] and event.sender_id not in admins[
        str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    # Check Greeting
    if is_greeting(text_of_message) and groups_config[str(event.chat_id)]["locks"][
        "greeting"] and event.sender_id not in admins[str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    # Check Location
    elif is_location(event) and groups_config[str(event.chat_id)]["locks"]["location"] and event.sender_id not in \
            admins[str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    # Check Hashtag
    elif is_hashtag(text_of_message) and groups_config[str(event.chat_id)]["locks"][
        "hashtag"] and event.sender_id not in admins[str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    # Check Command
    elif is_command(text_of_message) and groups_config[str(event.chat_id)]["locks"][
        "command"] and event.sender_id not in admins[str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    # Check Email
    elif is_email(text_of_message) and groups_config[str(event.chat_id)]["locks"]["email"] and event.sender_id not in \
            admins[str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    # Check Call to PM
    elif is_call_to_pm(text_of_message) and groups_config[str(event.chat_id)]["locks"][
        "email"] and event.sender_id not in admins[str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    # Check Username
    elif is_username(text_of_message) and groups_config[str(event.chat_id)]["locks"][
        "username"] and event.sender_id not in admins[str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    # Check Phone Number
    elif is_phone(text_of_message) and groups_config[str(event.chat_id)]["locks"]["phone"] and event.sender_id not in \
            admins[str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    # Check Very Large
    elif is_more_than_1000(text_of_message) and groups_config[str(event.chat_id)]["locks"][
        "longmessages"] and event.sender_id not in admins[str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    # Check URL Link
    elif is_url(text_of_message) and groups_config[str(event.chat_id)]["locks"]["url"] and event.sender_id not in \
            admins[str(event.chat_id)]:
        await bot.delete_messages(entity=event.chat_id, message_ids=[event.message.id])
    else:
        pass