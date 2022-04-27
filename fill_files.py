# Python lib
import json
# Import Keys
from keys import GROUPS_PATH, GROUP_ADMIN_PATH
# Locks
from lockTypes import LOCKTYPES

# Fill the Json Files
def fill_files(event, groups_config, admins, admin_list):
    chat = str(event.chat_id)
    groups_config[chat] = {}
    groups_config[chat]["locks"] = {}
    for i in LOCKTYPES:
        groups_config[chat]["locks"][i] = True

    with open(GROUPS_PATH, 'w', encoding='UTF-8') as file:
        json.dump(groups_config, file)

    admin_ids = []
    for i in admin_list:
        admin_ids.append(i.id)

    admins[str(event.chat_id)] = admin_ids
    with open(GROUP_ADMIN_PATH, 'w', encoding='UTF-8') as file:
        json.dump(admins, file)