"""training.py preprocesses and trains basedd on lyrics
provided. It takes lyrics from the /out directory, and
preprocesses them and the output files are placed in
the /data directory. It then trains a model based
on the the data in /data and outputs a model in
/model which can then be used for samples.

Currently only compatible with pytorch 1.1 so download
that version.

https://pytorch.org/get-started/previous-versions/#v110
"""

import os
import sys
import glob
from pathlib import Path

print('training.py preprocesses and trains a model based '
      'on lyrics provided.')
print('Click enter to continue or "q" to exit.')
option = input(': ')
print()

if not option == 'q':
    # Add code to check for if lyrics are rhotic and the
    # style of the song to help divide before model
    # preprocessing and model training is done.
    print()

    if Path('out/').exists():
        read_files = glob.glob('out/*.txt')

        if not Path('model/').exists():
            os.mkdir('model/')

        with open('model/source.txt', 'wb') as source_file:
            for f in read_files:
                with open(f, 'rb') as raw_file:
                    source_file.write(raw_file.read())

    print('Source file complete.')
    print()

    print('Preprocessing...')
    print('----------')
    os.system('python3 torch-rnn/scripts/preprocess.py '
              '--input_txt model/source.txt '
              '--output_h5 model/source.h5 '
              '--output_json model/source.json')
    print('----------')
    print('Preprocessing complete.')
    print()

    print('Are you training on a CPU or on a NVIDIA GPU?')
    print('1. CPU')
    print('2. NVIDIA GPU')
    train_config = input(': ')

    # while train_config not in [1, 2]:
    #     print('Please specify.')
    #     train_config = input(': ')

    if train_config == '1':
        print('How many threads would you like to use?')
        threads = input(': ')
        print('Training...')
        os.system('set OMP_NUM_THREADS={args.threads} '
                  '| python3 -B pytorch-rnn/train.py '
                  '--input-h5 model/source.h5 '
                  '--input-json model/source.json '
                  '--checkpoint-name model/model')
        print('Training complete.')

    if train_config == '2':
        print('Training...')
        os.system('python3 -B pytorch-rnn/train.py '
                  '--input-h5 model/source.h5 '
                  '--input-json model/source.json '
                  '--checkpoint-name model/model '
                  '--device cuda')
        print('Training complete.')

sys.exit()
