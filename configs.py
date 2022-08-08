# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk movie/series Search Bot.

🤖 My Name: <a href='http://t.me/Mdisk_search_tg_bot'>mdisk Movie Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/inform_adminzBOT'>huihuihui</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/inform_adminzBOT'>adminszz op</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

Mdisk Search Bot Here.🤖</a>

I Can Search 🔍 What You Want❗

add to to your group and make me admin
i will provide links there too

<a>Made With ❤ By @inform_adminzBOT</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

Mdisk Search Bot Here.🤖</a>

add to to your group and make me admin
i will provide links there too

<a>Made With ❤ By @inform_adminzBOT</a></b>
"""


