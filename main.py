"""main.py ensures that the dependencies for all scripts are
installed, and allows you to start automatically if need be.

This file should be run before the aforementioned, and updated
whenever the dependencies change.
"""
import os
import sys

print('Installing dependencies...')
os.system('pip3 install -r requirements.txt')

print('Dependencies installed.')
print()
print('Welcome to The Phonetic Song Project.')
print('If you encounter any bugs, feel free to report them at '
      'https://github.com/adlez27/phonetic-songs')
print()
print('What would you like to do?')
print('1. Fetch Lyrics')
print('2. Convert Lyrics')
print('3. Fetch Billboard Charts')
print('4. Train Model')
print('5. Sample Output from Model')
print('Type "q" to exit.')
forward = input(': ')

while forward != 'q':
    if forward == '1':
        os.system('python3 fetcher.py')

    if forward == '2':
        os.system('python3 converter.py')

    if forward == '3':
        os.system('python3 charts.py')

    if forward in ['4', '5']:
        print('torch and/or torchvision may be missing or may '
              'be out of date and are required for training '
              'and sampling models.')
        print('Choosing "yes" will update the version of torch '
              'used to the required version.')
        print('Choosing "no" will bypass the installation check '
              'sending you to the chosen script.')
        torch_choice = input('y/n: ')
        print()

        while not torch_choice in ['y', 'n']:
            print('Please specify.')
            torch_choice = input('y/n: ')
            if torch_choice == 'n':
                print()
                continue
            print()

        if torch_choice == 'y':
            print('Please specify the operating system you\'re using')
            print('1. Linux/Windows')
            print('2. MacOS')
            os_choice = input(': ')
            print()

            # Linux/Windows
            if os_choice == '1':
                print('Please specify if you want the CPU PyTorch '
                      'or GPU (NVIDIA - CUDA) PyTorch.')
                print('The GPU version allows you to do CPU training as well.')
                print('a. PyTorch CPU')
                print('b. PyTorch GPU (CUDA)')
                torch_ver = input(': ')
                print()

                if torch_ver == 'a':
                    print('This would download torch and torchvision wheels '
                          'and install them automatically.')
                    print('This may take a while depending on your internet '
                          'connection.')
                    os.system(
                        'pip3 install -r torch-winux-cpu.txt')
                if torch_ver == 'b':
                    print('This would download torch and torchvision wheels '
                          'and install them automatically.')
                    print('This may take a while depending on your internet '
                          'connection.')
                    os.system(
                        'pip3 install -r torch-winux-cuda92.txt')

            # MacOS
            if os_choice == '2':
                print('MacOS binaries don\'t support CUDA, install from '
                      'source if CUDA is needed.')
                print('This would download the CPU binaries for torch and '
                      'torchvision and install them automatically.')
                print('This may take a while depending on your internet '
                      'connection.')
                os.system(
                    'pip3 install -r torch-mac-cpu.txt')

    if forward == '4':
        os.system('python3 trainer.py')

    if forward == '5':
        os.system('python3 sampler.py')

    print()
    print('Would you like to continue?')
    print('1. Fetch Lyrics')
    print('2. Convert Lyrics')
    print('3. Fetch Billboard Charts')
    print('4. Train Model')
    print('5. Sample Output from Model')
    print('Type "q" to exit.')
    forward = input(': ')

print('Have a good day!')

sys.exit()
