from dotenv import load_dotenv
from lyricsgenius import Genius
import os


def search(song_name, artist):
    load_dotenv()
    token = os.getenv('TOKEN')
    genius = Genius(token)
    song = genius.search_song(song_name, artist)
    return song.lyrics


def main():
    song_name = input("Enter song name: ")
    artist = input("Enter artist name: ")
    lyrics = search(song_name, artist)
    lyrics_by_sections = lyrics.split("\n\n")
    print(lyrics_by_sections)


main()
