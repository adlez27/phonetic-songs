"""main.py ensures that the dependencies for converter.py and
fetcher.py are installed, and allows you to start automatically
if need be.

This file should be run before the aforementioned, and updated
whenever the dependencies change.
"""
import os
import sys

print('installing dependencies...')
os.system('pip3 install -r requirements.txt')

os.system('cls' if os.name == 'nt' else 'clear')
print('dependencies installed...')
print()
print('Welcome to The Phonetic Song Project.')
print('If you encounter any bugs, feel free to report them at '
      'https://github.com/adlez27/phonetic-songs')
print('What would you like to do?')
print('1. Fetch Lyrics')
print('2. Convert Lyrics')
print('3. Fetch Billboard Charts')
print('Type "q" to exit.')
forward = input(': ')

while forward != 'q':
    if forward == '1':
        os.system('python3 fetcher.py')

    if forward == '2':
        os.system('python3 converter.py')

    if forward == '3':
        os.system('python3 charts.py')

    print()
    print('Would you like to continue?')
    print('1. Fetch Lyrics')
    print('2. Convert Lyrics')
    print('3. Fetch Billboard Charts')
    print('Type "q" to exit.')
    forward = input(': ')


print('Thanks for using.')
sys.exit()
