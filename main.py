"""main.py ensures that the dependencies for converter.py and
fetcher.py are installed, and allows you to start automatically
if need be.

This file should be run before the aforementioned, and updated
whenever the dependencies change.
"""
import os
import sys

print('Installing dependencies...')
os.system('pip3 -q install -r requirements.txt')
print('Dependencies installed...')
print()
print('Welcome to The Phonetic Song Project.')
print('If you encounter any bugs, feel free to report them at '
      'https://github.com/adlez27/phonetic-songs')
print('What would you like to do?')
print('1. Fetch Lyrics')
print('2. Convert Lyrics')
print('3. Fetch Billboard Charts')
print('4. Train Model (This may take a while)')
print('Type "q" to exit.')
forward = input(': ')

while forward != 'q':
    if forward == '1':
        os.system('python3 fetcher.py')

    if forward == '2':
        os.system('python3 converter.py')

    if forward == '3':
        os.system('python3 charts.py')

    if forward == '4':
        os.system('python3 training.py')

    print()
    print('Would you like to continue?')
    print('1. Fetch Lyrics')
    print('2. Convert Lyrics')
    print('3. Fetch Billboard Charts')
    print('Type "q" to exit.')
    forward = input(': ')


print('Have a good day!')
sys.exit()
