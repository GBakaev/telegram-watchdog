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
NO_LOCKTYPE_ERROR = """đĢ There is no lock type such as `{}`!

âšī¸ To learn all the existing lock types click /locktypes.
"""

# Locks
SUCCESSFULL_LOCK = """â `{}` locked successfully."""
SUCCESSFULL_UNLOCK = """â `{}` unlocked successfully."""
LOCKTYPE_LIST = """âšī¸ **Currently available lock types:**

{}"""
SPECIFY_LOCK = """â ī¸ Please, specify lock type. 
âšī¸ To learn all the existing locktypes click /locktypes.

âšī¸  Usage: /lock <lock type>"""
SPECIFY_UNLOCK = """â ī¸ Please, specify lock type. 

âšī¸ To learn the current locktypes click /locktypes.

âšī¸  Usage: /unlock <lock type>"""
ALL_LOCKED = """đ All lock types are locked."""
ALL_UNLOCKED = """đ All lock types are unlocked."""
LOCK_STATES = """âšī¸ **Current lock states:**

{}

đ To change the state use /lock or /unlock command."""

# Help Message
HELP_MESSAGE = """âšī¸ To be fully operational I need the following rights:
- Delete messages
- Ban users

đ Commands:
/lock - Forbids users to use specified lock type
/unlock - Allows users to use specified lock type
/locktypes - Sends the list of existing lock types
/help - Sends this message
"""

# Use In Group 
USE_IN_GROUP = """âī¸ Use this command in group."""