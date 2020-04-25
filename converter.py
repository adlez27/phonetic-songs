"""converter.py allows the user to convert English words to X-SAMPA
from text files in /in with the use of the module pronouncing, and
converts ARPABET phonemes to X-SAMPA before saving the output in
a text  file in the /out directory.
"""
import os
import re
import sys
from pathlib import Path
import pronouncing


def clean_lyrics(text):
    """Removes unnecessary characters."""
    text = re.sub(r'[^a|A-z|Z;^0-9;^ ;^\';^\-;^\n]', '', text)
    return text


def arpabet_to_xsampa(text):
    """Converts ARPABET phonemes to X-SAMPA"""
    text = text.replace(' aa ', ' A ')
    text = text.replace(' ae ', ' { ')
    text = text.replace(' ah ', ' V ')
    text = text.replace(' ao ', ' O ')
    text = text.replace(' ax ', ' @ ')
    text = text.replace(' eh ', ' E ')
    text = text.replace(' er ', ' 3 ')
    text = text.replace(' ih ', ' I ')
    text = text.replace(' iy ', ' i ')
    text = text.replace(' uh ', ' U ')
    text = text.replace(' uw ', ' u ')

    text = text.replace(' ey ', ' eI ')
    text = text.replace(' ay ', ' aI ')
    text = text.replace(' oy ', ' OI ')
    text = text.replace(' ow ', ' oU ')
    text = text.replace(' aw ', ' aU ')

    text = text.replace(' ch ', ' tS ')
    text = text.replace(' jh ', ' dZ ')
    text = text.replace(' th ', ' T ')
    text = text.replace(' dh ', ' D ')
    text = text.replace(' sh ', ' S ')
    text = text.replace(' zh ', ' Z ')
    text = text.replace(' ng ', ' N ')
    text = text.replace(' dx ', ' 4 ')
    text = text.replace(' y ', ' j ')
    text = text.replace(' hh ', ' h ')

    return text


def convert_song(raw_lyrics):
    """Conversion of text files in /in to /out"""
    lyrics = clean_lyrics(raw_lyrics).split('\n')
    for i in range(0, len(lyrics)):
        lyrics[i] = lyrics[i].split(' ')

    converted_lyrics = ""
    for line in lyrics:
        converted_line = " "
        for word in line:
            pronunciations = pronouncing.phones_for_word(word)
            if len(pronunciations) == 0:
                converted_line += "*" + word.upper() + "* "
            else:
                phonemes = pronunciations[0].lower()
                phonemes = phonemes.replace('0', '')
                phonemes = phonemes.replace('1', '')
                phonemes = phonemes.replace('2', '')
                converted_line += phonemes + " "
        converted_line = arpabet_to_xsampa(converted_line)
        converted_line = converted_line[1:-1]
        if converted_line != "**":
            converted_lyrics += converted_line + "\r\n"
    return converted_lyrics


if Path('in/').exists():
    basepath = Path('in/')
    files_in_basepath = (entry for entry in basepath.iterdir() if
                         entry.is_file())
    for item in files_in_basepath:
        item = str(item)
        with open(item, 'r', encoding='utf-8') as Input:
            print('Opening: ' + item[3:-4])
            content = Input.read()
        Input.close()

        if not Path('out/').exists():
            os.mkdir('out')
        with open('out/' + item[3:-4] + " T.txt", 'w') as output:
            output.write(convert_song(content))
        output.close()

        if not Path('in/converted').exists():
            os.mkdir('in/converted')
        os.rename('in/' + item[3:-4] + '.txt', 'in/converted/' + item[3:-4] + '.txt')

        print("Converted: " + item[3:-4])
else:
    print('No songs to convert.')

sys.exit()
