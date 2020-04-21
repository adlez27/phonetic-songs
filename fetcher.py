import os
import sys
from pathlib import Path
print('Ensuring dependencies exist...\n')
try:
  from azapi import AZlyrics
except ImportError:
  print('Trying to install required module: azapi\n')
  os.system('python3 -m pip install azapi')
  from azapi import AZlyrics
  print()
try:
  import nodejs
except ImportError:
  print('Trying to install required module: nodejs\n')
  os.system('python3 -m pip install nodejs')
  import nodejs
  print()

print('fetcher.py fetches lyrics from various APIs. Please choose which one you would like to use.')
print('1. AZLyrics.com (azapi)')
print('2. VocaDB (currently not available)')
option = input('#: ')
print()

# AZLyrics
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

    lyrics = api.getLyrics(artist = artist_name, title = song_title, save=False)

    filename = (artist_name + ' - ' + song_title + '.txt')

    if Path('in/').exists():
      basepath = Path('in/')
    else:
      os.mkdir('in')
      if Path('in/').exists():
        basepath = Path('in/')

    with open(basepath/filename,'w', encoding='latin-1') as export:
      export.write(lyrics).__str__
      export.close()
    
    print('Downloaded: ' + filename)
  if az_option == 'b':
    search_terms = input('Enter lyrics: ')

    songs = api.search(search_terms, category='songs')   
    artist_name = songs[0]['artist']
    song_title = songs[0]['name']
    song_url = songs[0]['url']

    lyrics = api.getLyrics(url = song_url, save=False)

    filename = (artist_name + ' - ' + song_title + '.txt')

    if Path('in/').exists():
      basepath = Path('in/')
    else:
      os.mkdir('in')
      if Path('in/').exists():
        basepath = Path('in/')

    with open(basepath/filename,'w', encoding='latin-1') as export:
      export.write(lyrics).__str__
      export.close()

    print('Downloaded: ' + filename)
  if az_option == 'c':
    input('This feature is not yet implemented. Try again later.')

# VocaDB
if option == '2':
  print('This feature is not yet implemented. Try again later.\n')    

exit()