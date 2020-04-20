import os
import re

try:
    import pathlib
except ImportError:
    print("Trying to install required module: pathlib\n")
    os.system('python -m pip install pathlib')

from pathlib import Path

try:
    import pronouncing
except ImportError:
    print("Trying to install required module: pronouncing\n")
    os.system('python -m pip install pronouncing')

import pronouncing

def arpabet_to_xsampa(text):
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
    lyrics = raw_lyrics.split('\n')
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
        converted_lyrics += converted_line + "\r\n"

    converted_lyrics = re.sub(r'\r\n\*\*\r\n', '', converted_lyrics)
    return converted_lyrics


basepath = Path('in/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    item = str(item)
    with open(item, 'r') as input:
        content = input.read()
    input.close()

    with open('out/' + item[3:], 'w') as output:
        output.write(convert_song(content))
    output.close()

    print("Converted: " + item[3:-4])

exit()
