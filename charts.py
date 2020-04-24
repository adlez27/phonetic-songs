"""billboard.py downloads chart data to be used in fetcher.py"""
import os
import sys
# import json
from pathlib import Path
from billboard import ChartData
import yaml

# charts_list = json.loads(open('charts.json').read())
charts_list = yaml.load(open('charts.yaml').read())

print('This scripts allows you to fetch billboard chart data.')
print('It downloads the following charts:')
for key in charts_list:
    print('- ' + key)
print()
print('Press enter to continue to download these charts, or "q" to exit')
permission = input(': ')
if permission != 'q':
    for key, value in charts_list.items():
        chart_name = value
        chart = ChartData(chart_name)
        chart_count = len(chart)
        filename = (key + '.csv')
        # print('Fetching ' +     filename)

        if Path('charts/').exists():
            basepath = Path('charts/')
        else:
            os.mkdir('charts')
            if Path('charts/').exists():
                basepath = Path('charts/')

        with open(basepath/filename, 'w', encoding='utf-8') as export:
            i = 1
            while i < chart_count:
                song = chart[i]
                song_title = song.title
                artist_name = song.artist
                line = (song_title + ';' + artist_name + '\n')
                i = i + 1
                export.write(line)
            export.close()

        print('Downloaded: ' + filename)

sys.exit()
