# Types
LOCKTYPES = [
            'hashtag',
            'command',
            'username',
            'email',
            'location',
            'url',
            'kick',
            'forward',
            'longmessages',
            'greeting',
            'phone',
            'comepm'
        ]

# Error
NO_LOCKTYPE_ERROR = """🚫 There is no lock type such as `{}`!

ℹ️ To learn all the existing lock types click /locktypes.
"""

# Locks
SUCCESSFULL_LOCK = """✅ `{}` locked successfully."""
SUCCESSFULL_UNLOCK = """✅ `{}` unlocked successfully."""
LOCKTYPE_LIST = """ℹ️ **Currently available lock types:**

{}"""
SPECIFY_LOCK = """⚠️ Please, specify lock type. 
ℹ️ To learn all the existing locktypes click /locktypes.

ℹ️  Usage: /lock <lock type>"""
SPECIFY_UNLOCK = """⚠️ Please, specify lock type. 

ℹ️ To learn the current locktypes click /locktypes.

ℹ️  Usage: /unlock <lock type>"""
ALL_LOCKED = """🔒 All lock types are locked."""
ALL_UNLOCKED = """🔓 All lock types are unlocked."""
LOCK_STATES = """ℹ️ **Current lock states:**

{}

🔄 To change the state use /lock or /unlock command."""

# Help Message
HELP_MESSAGE = """ℹ️ To be fully operational I need the following rights:
- Delete messages
- Ban users

📌 Commands:
/lock - Forbids users to use specified lock type
/unlock - Allows users to use specified lock type
/locktypes - Sends the list of existing lock types
/help - Sends this message
"""

# Use In Group 
USE_IN_GROUP = """❗️ Use this command in group."""