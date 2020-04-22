"""fetcher.py allows the user to fetch lyrics from numerous APIs and
save them as a text file in the /in directory.
"""
import os
import sys
from pathlib import Path


class Color:
    """Color definitions"""
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print('fetcher.py fetches lyrics from various APIs. '
      'Please choose which one you would like to use.')
print('1. AZLyrics.com (azapi)')
print('2. VocaDB')
print('3. Genius (currently not available)')
print(Color.BOLD + '4. MetroLyrics (tswift) - RECOMMENDED' + Color.END)
print('To close, type "q"')
option = input(': ')
print()

if not option == 'q':
    # AZlyrics
    if option == '1':
        from azapi import AZlyrics
        az_api = AZlyrics()
        print('You can either get the song with the song title and artist'
              'name, or you can search via lyrics.')
        print('Please choose which method you would like to use.')
        print('a. Artist Name + Song Title')
        print('b. Search by lyrics')
        az_option = input(': ')

        if az_option == 'a':
            artist_name = input('Type in the name of the artist: ')
            song_title = input('Type in the title of the song: ')

            lyrics = az_api.getLyrics(
                artist=artist_name, title=song_title, save=False).strip()

            filename = (artist_name + ' - ' + song_title + '.txt')

            if Path('in/').exists():
                basepath = Path('in/')
            else:
                os.mkdir('in')
                if Path('in/').exists():
                    basepath = Path('in/')

            with open(basepath/filename, 'w', encoding='latin-1') as export:
                export.write(lyrics)
                export.close()

            print('Downloaded: ' + filename)
        if az_option == 'b':
            search_terms = input('Enter lyrics: ')

            songs = az_api.search(search_terms, category='songs')
            artist_name = songs[0]['artist']
            song_title = songs[0]['name']
            song_url = songs[0]['url']

            lyrics = az_api.getLyrics(url=song_url, save=False).strip()

            filename = (artist_name + ' - ' + song_title + '.txt')

            if Path('in/').exists():
                basepath = Path('in/')
            else:
                os.mkdir('in')
                if Path('in/').exists():
                    basepath = Path('in/')

            with open(basepath/filename, 'w', encoding='latin-1') as export:
                export.write(lyrics)
                export.close()

            print('Downloaded: ' + filename)

    # VocaDB
    if option == '2':
        import requests

        vdb_url = 'https://vocadb.net/api/'
        search_type = ['artists', 'songs']
        print('You can get the lyrics by searching with the song title'
              ' and artist name.')

        artist_name = input('Type in the name of the artist: ')
        song_title = input('Type in the title of the song: ')

        artist_payloid = {'query': artist_name,
                          'namematchMode': 'Partial',
                          'preferAccurateMatches': 'true'}
        artist_search = requests.get(vdb_url + search_type[0],
                                     artist_payloid)

        artist_values = artist_search.json()
        artist_title = artist_values['items'][0]['name']
        print('Artist retrieved: ' + artist_title)
        artist_id = artist_values['items'][0]['id']

        song_payload = {'query': song_title, 'lang': 'English',
                        'songTypes': 'Original', 'fields': 'Lyrics',
                        'artistId': artist_id}
        song_search = requests.get(vdb_url + search_type[1],
                                   song_payload)

        song_values = song_search.json()
        song_name = song_values['items'][0]['name']
        print('Song retrieved: ' + song_name)
        lyrics_values = song_values['items'][0]['lyrics']
        lyrics = lyrics_values[0]['value']

        filename = (artist_title + ' - ' + song_name + '.txt')

        if Path('in/').exists():
            basepath = Path('in/')
        else:
            os.mkdir('in')
            if Path('in/').exists():
                basepath = Path('in/')

        with open(basepath/filename, 'w', encoding='latin-1') as export:
            export.write(lyrics)
            export.close()

        print('Downloaded: ' + filename)
    # Genius
    if option == '3':
        print('This feature is not yet implemented. Try again later.\n')

    # MetroLyrics
    if option == '4':
        from tswift import Song
        print('You can either get the song with the song title and artist'
              'name, or you can search via lyrics.')
        print('Please choose which method you would like to use.')
        print('a. Artist Name + Song Title')
        print('b. Search by lyrics')
        ml_option = input(': ')

        if ml_option == 'a':
            artist_name = input('Type in the name of the artist: ')
            song_title = input('Type in the title of the song: ')

            lyrics = Song(title=song_title, artist=artist_name)

            filename = (artist_name + ' - ' + song_title + '.txt')

            if Path('in/').exists():
                basepath = Path('in/')
            else:
                os.mkdir('in')
                if Path('in/').exists():
                    basepath = Path('in/')

            with open(basepath/filename, 'w', encoding='latin-1') as export:
                export.write(lyrics.format())
                export.close()

            print('Downloaded: ' + filename)
        if ml_option == 'b':
            search_terms = input('Enter lyrics: ')

            lyrics = Song.find_song(search_terms)
            song_title = lyrics.title
            artist_name = lyrics.artist

            filename = (artist_name + ' - ' + song_title + '.txt')

            if Path('in/').exists():
                basepath = Path('in/')
            else:
                os.mkdir('in')
                if Path('in/').exists():
                    basepath = Path('in/')

            with open(basepath/filename, 'w', encoding='latin-1') as export:
                export.write(lyrics.format())
                export.close()

            print('Downloaded: ' + filename)
sys.exit()
