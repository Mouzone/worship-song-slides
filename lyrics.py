from requests.exceptions import HTTPError, Timeout
from lyricsgenius import Genius
from dotenv import load_dotenv
import re
import os


def search(song_name, artist):
    load_dotenv()
    token = os.getenv('TOKEN')
    genius = Genius(token)
    genius.excluded_terms = ["(Remix)", "(Live)"]

    song = genius.search_song(song_name, artist)
    return song.lyrics

# todo: figure out why second [Verse 2] does not properly add \n before
# -- "You might also like[Verse 2]"
# remove all \n and \n\n before [ then replace [ with \n\n[ for proper
def cleanNewlines(lyrics):
    lyrics_no_header = lyrics.split("Lyrics")[1]
    pattern = r'\d*Embed$'
    lyrics_no_ending = re.sub(pattern, '', lyrics_no_header)
    lyrics_no_newlines = re.sub(r"\n\n", r'\n', lyrics_no_ending)
    lyrics_space_between = re.sub(r"\[", r"\n[", lyrics_no_newlines)
    lyrics_proper = re.sub(r"\n", "", lyrics_space_between, count=1)
    # add new line before every [ if there is no new line
    return lyrics_proper


# todo: store order somehow since verse 2 repeats
def createLyricsDict(lyrics):
    lyrics_list = lyrics.split("\n\n")
    lyrics_by_section = {}
    for section in lyrics_list:
        header_end = section.find('\n')
        # Split the text into header and body
        section_name = section[:header_end].strip()
        body = section[header_end:].strip()
        lyrics_by_section[section_name] = body

    return lyrics_by_section


def clean(lyrics):
    lyrics_clean = cleanNewlines(lyrics)
    return createLyricsDict(lyrics_clean)


def main():
    song_name = input("Enter song name: ")
    artist = input("Enter artist name: ")
    try:
        lyrics = search(song_name, artist)
        lyrics_by_sections = clean(lyrics)
        print(lyrics_by_sections)
    except HTTPError as e:
        print(e.errno)
        print(e.args[0])
        print(e.args[1])
    except Timeout:
        pass

main()
