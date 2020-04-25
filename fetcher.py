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


print('fetcher.py fetches lyrics from various sources. '
      'Please choose which one you would like to use.')
print('If you experience any bugs, feel free to report '
      'at https://github.com/adlez27/phonetic-songs')
print()
print(Color.BOLD + '1. MetroLyrics (tswift) - RECOMMENDED' + Color.END)
print('2. Genius')
print('3. AZLyrics.com (azapi) - ' +
      Color.UNDERLINE + 'NOT RECOMMENDED' + Color.END)
print('4. VocaDB')
print('5. UtaiteDB')
print('6. TouhouDB')
print('7. Piapro (currently not implemented)')
print('To close, type "q"')
option = input(': ')
print()

if not option == 'q':
    # MetroLyrics
    if option == '1':
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

            with open(basepath/filename, 'w', encoding='utf-8') as export:
                export.write(lyrics.format())
                export.close()

            print('Downloaded: ' + artist_name + ' - ' + song_title)
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

            with open(basepath/filename, 'w', encoding='utf-8') as export:
                export.write(lyrics.format())
                export.close()

            print('Downloaded: ' + artist_name + ' - ' + song_title)

    # Genius
    if option == '2':
        import requests
        from bs4 import BeautifulSoup

        def lyric_fetcher_genius(song_api_path):
            '''Lyric Fetching from Genius using API and HTML scraping'''
            song_url = base_url + song_api_path
            response = requests.get(song_url, headers=headers)
            json = response.json()
            song_path = json["response"]["song"]["path"]

            page_url = site_url + song_path
            page = requests.get(page_url)
            html = BeautifulSoup(page.text, 'html.parser')
            [h.extract() for h in html('script')]
            [h.extract() for h in html('[]')]
            lyrics_get = html.find(
                "div", class_="lyrics").get_text()
            return lyrics_get

        site_url = 'https://genius.com'
        base_url = 'https://api.genius.com'
        search_path = '/search'

        with open('token.txt', 'r') as token:
            genius_token = token.read()
        headers = {'Authorization': 'Bearer ' + genius_token}

        print('You can get the lyrics by searching with the song title'
              ' and the artist name. You can also mass fetch based on '
              'the Billboard charts.')
        print('Please choose which method you would like to use.')
        print('a. Artist Name + Song Title')
        print('b. Chart Conversion')
        g_option = input(': ')

        if g_option == 'a':
            # Adapted: https://bigishdata.com/2016/09/27/getting-song-lyrics-from-geniuss-api-scraping/
            artist_name = input('Type in the name of the artist: ')
            song_title = input('Type in the title of the song: ')
            params = {'q': song_title}

            response = requests.get(base_url + search_path,
                                    params=params, headers=headers)
            json = response.json()
            song_info = None

            for hit in json['response']['hits']:
                if hit['result']['primary_artist']['name'] == artist_name:
                    song_info = hit
                    break
            if song_info:
                pass

            if __name__ == "__main__":
                search_url = base_url + "/search"
                data = {'q': song_title}
                response = requests.get(search_url, data=data, headers=headers)
                json = response.json()
                song_info = None
                for hit in json["response"]["hits"]:
                    if hit["result"]["primary_artist"]["name"] == artist_name:
                        song_info = hit
                        break
                if song_info:
                    song_api_path = song_info["result"]["api_path"]
                    lyrics = lyric_fetcher_genius(song_api_path)

            filename = (artist_name + ' - ' + song_title + '.txt')

            if Path('in/').exists():
                basepath = Path('in/')
            else:
                os.mkdir('in')
                if Path('in/').exists():
                    basepath = Path('in/')

            with open(basepath/filename, 'w', encoding='utf-8') as export:
                export.write(lyrics)
                export.close()

            print('Downloaded: ' + artist_name + ' - ' + song_title)
        if g_option == 'b':
            import csv

            chart_name = input('Type in the name of the chart: ')
            chart_path = ('charts/' + chart_name + '.csv')
            with open(chart_path) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=';')
                for row in readCSV:
                    artist_name = row[1]
                    song_title = row[0]
                    params = {'q': song_title}

                    response = requests.get(base_url + search_path,
                                            params=params, headers=headers)
                    json = response.json()
                    song_info = None

                    for hit in json['response']['hits']:
                        if hit['result']['primary_artist']['name'] == artist_name:
                            song_info = hit
                            break
                    if song_info:
                        pass

                    if __name__ == "__main__":
                        search_url = base_url + "/search"
                        data = {'q': song_title}
                        response = requests.get(
                            search_url, data=data, headers=headers)
                        json = response.json()
                        song_info = None
                        for hit in json["response"]["hits"]:
                            if hit["result"]["primary_artist"]["name"] == artist_name:
                                song_info = hit
                                break
                        if song_info:
                            song_api_path = song_info["result"]["api_path"]
                            lyrics = lyric_fetcher_genius(song_api_path)

                    filename = (artist_name + ' - ' + song_title + '.txt')

                    if Path('in/').exists():
                        basepath = Path('in/')
                    else:
                        os.mkdir('in')
                        if Path('in/').exists():
                            basepath = Path('in/')

                    with open(basepath/filename, 'w', encoding='utf-8') as export:
                        export.write(lyrics)
                        export.close()

                    print('Downloaded: ' + artist_name + ' - ' + song_title)
    # AZlyrics
    if option == '3':
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

            with open(basepath/filename, 'w', encoding='utf-8') as export:
                export.write(lyrics)
                export.close()

            print('Downloaded: ' + artist_name + ' - ' + song_title)
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

            with open(basepath/filename, 'w', encoding='utf-8') as export:
                export.write(lyrics)
                export.close()

            print('Downloaded: ' + artist_name + ' - ' + song_title)

    # VocaDB
    if option == '4':
        import requests

        vdb_url = 'https://vocadb.net/api/'
        search_type = ['artists', 'songs']
        print('You can get the lyrics by searching with the song title'
              ' and artist name.')

        artist_name = input('Type in the name of the artist: ')
        song_title = input('Type in the title of the song: ')
        print()
        print('Specify whether the song is an "Original", "Remix", '
              '"Cover", or "Arrangement" to help filter results.')
        print('You can leave this field blank.')
        song_type = input(': ')
        print()

        artist_payloid = {'query': artist_name,
                          'namematchMode': 'Auto',
                          'preferAccurateMatches': 'true'}
        artist_search = requests.get(vdb_url + search_type[0],
                                     artist_payloid)

        artist_values = artist_search.json()
        artist_title = artist_values['items'][0]['name']
        print('Artist retrieved: ' + artist_title)
        artist_id = artist_values['items'][0]['id']

        song_payload = {'query': song_title, 'lang': 'English',
                        'songTypes': song_type, 'fields': 'Lyrics',
                        'artistId': artist_id,
                        'defaultNameLanguage': 'English'}
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

        with open(basepath/filename, 'w', encoding='utf-8') as export:
            export.write(lyrics)
            export.close()

        print('Downloaded: ' + artist_name + ' - ' + song_title)

    # UtaiteDB
    if option == '5':
        import requests

        udb_url = 'https://utaitedb.net/api/'
        search_type = ['artists', 'songs']
        print('You can get the lyrics by searching with the song title'
              ' and artist name.')

        artist_name = input('Type in the name of the artist: ')
        song_title = input('Type in the title of the song: ')
        print()
        print('Specify whether the song is an "Original", "Remix", '
              '"Cover", or "Arrangement" to help filter results.')
        print('You can leave this field blank.')
        song_type = input(': ')
        print()

        artist_payloid = {'query': artist_name,
                          'namematchMode': 'Auto',
                          'preferAccurateMatches': 'true'}
        artist_search = requests.get(udb_url + search_type[0],
                                     artist_payloid)

        artist_values = artist_search.json()
        artist_title = artist_values['items'][0]['name']
        print('Artist retrieved: ' + artist_title)
        artist_id = artist_values['items'][0]['id']

        song_payload = {'query': song_title, 'lang': 'English',
                        'songTypes': song_type, 'fields': 'Lyrics',
                        'artistId': artist_id}
        song_search = requests.get(udb_url + search_type[1],
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

        with open(basepath/filename, 'w', encoding='utf-8') as export:
            export.write(lyrics)
            export.close()

        print('Downloaded: ' + artist_name + ' - ' + song_title)

    # TouhouDB
    if option == '6':
        import requests

        tdb_url = 'https://touhoudb.com/api/'
        search_type = ['artists', 'songs']
        print('You can get the lyrics by searching with the song title'
              ' and artist name.')

        artist_name = input('Type in the name of the artist: ')
        song_title = input('Type in the title of the song: ')
        print()
        print('Specify whether the song is an "Original", "Remix", '
              '"Cover", or "Arrangement" to help filter results.')
        print('You can leave this field blank.')
        song_type = input(': ')
        print()

        artist_payloid = {'query': artist_name,
                          'namematchMode': 'Auto',
                          'preferAccurateMatches': 'true'}
        artist_search = requests.get(tdb_url + search_type[0],
                                     artist_payloid)

        artist_values = artist_search.json()
        artist_title = artist_values['items'][0]['name']
        print('Artist retrieved: ' + artist_title)
        artist_id = artist_values['items'][0]['id']

        song_payload = {'query': song_title, 'lang': 'English',
                        'songTypes': song_type, 'fields': 'Lyrics',
                        'artistId': artist_id}
        song_search = requests.get(tdb_url + search_type[1],
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

        with open(basepath/filename, 'w', encoding='utf-8') as export:
            export.write(lyrics)
            export.close()

        print('Downloaded: ' + artist_name + ' - ' + song_title)

    # Piapro
    if option == '7':
        print('This feature is not yet implemented, please try again later.')
sys.exit()
