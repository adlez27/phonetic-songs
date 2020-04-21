import os
import random
import sys
from pathlib import Path
print('Ensuring dependencies exist...\n')
# for AZlyrics
try:
    from azapi import AZlyrics
except ImportError:
    print('Trying to install required module: azapi\n')
    os.system('python3 -m pip install azapi')
    from azapi import AZlyrics
    print()
# for VocaDB
try:
    import nodejs
except ImportError:
    print('Trying to install required module: nodejs\n')
    os.system('python3 -m pip install nodejs')
    import nodejs
    print()
# for MetroLyrics
try:
    import tswift
except ImportError:
    print('Trying to install required module: tswift\n')
    os.system('python3 -m pip install tswift')
    import tswift

class color:
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

print('fetcher.py fetches lyrics from various APIs. Please choose which one you would like to use.')
print('1. AZLyrics.com (azapi)')
print('2. VocaDB (currently not available)')
print('3. Genius (currently not available)')
print(color.BOLD + '4. MetroLyrics (tswift) - RECOMMENDED' + color.END)
print('To close, type "q"')
option = input(': ')
print()

if not option == 'q':
    # AZlyrics  
    if option == '1': 
        api = AZlyrics()
        print('You can either get the song with the song title and artist name, or you can search via lyrics.')
        print('Please choose which method you would like to use.')
        print('a. Artist Name + Song Title')
        print('b. Search by lyrics')
        az_option = input(': ')

        if az_option == 'a':
            artist_name = input('Type in the name of the artist: ')
            song_title = input('Type in the title of the song: ')

            lyrics = api.getLyrics(artist = artist_name, title = song_title, save=False).strip()

            filename = (artist_name + ' - ' + song_title + '.txt')

            if Path('in/').exists():
                basepath = Path('in/')
            else:
                os.mkdir('in')
                if Path('in/').exists():
                    basepath = Path('in/')

            with open(basepath/filename,'w', encoding='latin-1') as export:
                export.write(lyrics)
                export.close()
            
            print('Downloaded: ' + filename)
        if az_option == 'b':
            search_terms = input('Enter lyrics: ')

            songs = api.search(search_terms, category='songs')   
            artist_name = songs[0]['artist']
            song_title = songs[0]['name']
            song_url = songs[0]['url']

            lyrics = api.getLyrics(url = song_url, save=False).strip()

            filename = (artist_name + ' - ' + song_title + '.txt')

            if Path('in/').exists():
                basepath = Path('in/')
            else:
                os.mkdir('in')
                if Path('in/').exists():
                    basepath = Path('in/')

            with open(basepath/filename,'w', encoding='latin-1') as export:
                export.write(lyrics)
                export.close()

            print('Downloaded: ' + filename)

    # VocaDB
    if option == '2':
        print('This feature is not yet implemented. Try again later.\n')    

    # Genius
    if option == '3':
        print('This feature is not yet implemented. Try again later.\n')    

    # MetroLyrics
    if option == '4':  
        from tswift import Song
        from tswift import Artist
        print('You can either get the song with the song title and artist name, or you can search via lyrics.')
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

            with open(basepath/filename,'w', encoding='latin-1') as export:
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

            with open(basepath/filename,'w', encoding='latin-1') as export:
                export.write(lyrics.format())
                export.close()

            print('Downloaded: ' + filename)
exit()