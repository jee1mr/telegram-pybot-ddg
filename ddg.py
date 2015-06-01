import plugintypes
import tgl
from telegrambot.utils.decorators import group_only
import requests
from bs4 import BeautifulSoup
import duckduckgo as ddg


class DDGPlugin(plugintypes.TelegramPlugin):
    """
    DuckDuckGo Search
    """

    patterns = {
        "^/ddg $": "ddg_search",
    }

    usage = [
        "/ddg search_term: get search result",
    ]

    def __init__(self):
        super().__init__()


    @group_only
    def ddg_search(msg):
        msg = msg[5:]
        ans = ddg.query(msg)
        if ans.type != "nothing":
            return str(ans.answer.text)
        else:
            try:
                return str(ddg.get_zci(msg))            
            except ValueError:
                pass
