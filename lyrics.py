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


def clean(lyrics):
    lyrics_no_header = lyrics.split("Lyrics")[1]
    pattern = r'\d*Embed$'
    lyrics_no_ending = re.sub(pattern, '', lyrics_no_header)
    # add new line before every [ if there is no new line
    print(lyrics_no_ending)

    lyrics_list = lyrics_no_ending.split("\n\n")
    lyrics_by_section = {}
    for section in lyrics_list:
        header_end = section.find('\n')
        # Split the text into header and body
        section_name = section[:header_end].strip()
        body = section[header_end:].strip()
        lyrics_by_section[section_name] = body

    return lyrics_by_section


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
