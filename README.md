# Telegram Watchdog

A Bot that Acts as a Watchdog for Telegram Groups.

### Features:

* Deletes messages that are of the following types:
    'hashtag',
    'command',
    'username',
    'email',
    'location',
    'url',
    'forward',
    'longmessages',
    'greeting',
    'phone',
    'comepm'
* Kick/Ban Users from Joining the Group (Channel Discussion Group).
* Custom Types for each group.
* Group Admins are automatically detected.

## Setup
### Telegram API Keys
1. Sign up for Telegram using any application.
2. Log in to your Telegram core: https://my.telegram.org.
3. Go to ‘API development tools’ and fill out the form.
4. You will get the api_id and api_hash needed. Fill them in the keys.py file.

### Telegram Bot
1. You can create a new bot via ([@BotFather](https://telegram.me/BotFather)).
2. Add the Bot token you got to the BOT_TOKEN in the keys.py file.

### Running the Bot
4. `pip install -r requirements.txt`
5. Run it! `python watchdog.py`

## TODO

* Create Heroku Auto Setup.
* Setup Cron Script in order to keep bot running