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


def cleanNewlines(lyrics):
    # remove beginning text and ending text that is not part of the lyrics
    lyrics_no_header = lyrics.split("Lyrics")[1]
    lyrics_no_ending = re.sub(r'\d*Embed$', '', lyrics_no_header)

    # standardize open brackets to be able to split with \n\n[
    lyrics_no_newlines = re.sub(r"\n\n", '', lyrics_no_ending)
    lyrics_no_newlines = re.sub(r"\n\[", '[', lyrics_no_newlines)

    lyrics_proper = re.sub(r"\[", "\n\n[", lyrics_no_newlines)

    return lyrics_proper


def createLyricsDict(lyrics):
    lyrics_list = lyrics.split("\n\n")
    lyrics_list = lyrics_list[1:]

    lyrics_by_section = {}
    order = []

    for section in lyrics_list:
        header_end = section.find('\n')
        # Split the text into header and body
        if header_end != -1:
            section_name = section[:header_end].strip()
            body = section[header_end:].strip()

            order.append(section_name)
            lyrics_by_section[section_name] = body

    return order, lyrics_by_section


def main():
    song_name = input("Enter song name: ")
    artist = input("Enter artist name: ")
    try:
        lyrics = search(song_name, artist)
        lyrics_clean = cleanNewlines(lyrics)
        order, lyrics_by_sections = createLyricsDict(lyrics_clean)
        print(order)
        print(lyrics_by_sections)
    except HTTPError as e:
        print(e.errno)
        print(e.args[0])
        print(e.args[1])
    except Timeout:
        pass


main()
