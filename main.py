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

    if forward == '4' or '5':
        try:
            import torch
            import torchvision
        except ImportError:
            print('torch and/or torchvision are missing and are '
                  'required for training and sampling models.')
            print('Are you going to be training and sampling models?')
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
                print('1. Linux')
                print('2. MacOS')
                print('3. Windows')
                os_choice = input(': ')
                print()

                # Linux
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
                            'pip3 install torch==1.5.1+cpu torchvision==0.6.1+cpu '
                            '-f https://download.pytorch.org/whl/torch_stable.html')
                    if torch_ver == 'b':
                        print('This would download torch and torchvision wheels '
                              'and install them automatically.')
                        print('This may take a while depending on your internet '
                              'connection.')
                        os.system(
                            'pip3 install torch==1.5.1+cu92 torchvision==0.6.1+cu92 '
                            '-f https://download.pytorch.org/whl/torch_stable.html')

                # MacOS
                if os_choice == '2':
                    print('MacOS binaries don\'t support CUDA, install from '
                          'source if CUDA is needed.')
                    print('This would download the CPU binaries for torch and '
                          'torchvision and install them automatically.')
                    print('This may take a while depending on your internet '
                          'connection.')
                    os.system(
                        'pip3 install torch==1.5.1 torchvision==0.6.1')

                # Windows
                if os_choice == '3':
                    print('Please specify if you want the CPU PyTorch '
                          'or GPU (NVIDIA - CUDA) PyTorch.')
                    print('The GPU version allows you to do CPU training as well.')
                    print('a. PyTorch CPU')
                    print('b. PyTorch GPU (CUDA)')
                    torch_ver = input(': ')
                    if torch_ver == 'a':
                        print('This would download torch and torchvision wheels '
                              'and install them automatically.')
                        print('This may take a while depending on your internet '
                              'connection.')
                        os.system(
                            'pip3 install torch==1.5.1+cpu torchvision==0.6.1+cpu '
                            '-f https://download.pytorch.org/whl/torch_stable.html')
                    if torch_ver == 'b':
                        print('This would download torch and torchvision wheels '
                              'and install them automatically.')
                        print('This may take a while depending on your internet '
                              'connection.')
                        os.system(
                            'pip3 install torch==1.5.1+cu92 torchvision==0.6.1+cu92 '
                            '-f https://download.pytorch.org/whl/torch_stable.html')

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
