from dotenv import load_dotenv
from lyricsgenius import Genius

import os

load_dotenv()

token = os.getenv('TOKEN')
genius = Genius(token)
song = genius.search_song("Build My Life", None)
print(song.lyrics)
# connect to genius api

# take search terms

# query

# look at results

# select the best

# return the lyrics of the best