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
    print('What would you like to do?')
    print('1. Start from scratch')
    print('2. Start from a preprocessed set')
    choice = input(': ')
    print()

    # Preprocessing
    if choice == '1':
        # Add code to check for if lyrics are rhotic and the
        # style of the song to help divide before model
        # preprocessing and model training is done.

        print('What would you like to name this run?')
        model_name = input(': ')

        if Path('out/').exists():
            read_files = glob.glob('out/*.txt')

            if not Path('model/' + model_name + '/').exists():
                os.mkdir('model/' + model_name + '/')

            model_path = ('model/' + model_name + '/')

            with open(model_path + model_name + '.txt', 'wb') as source_file:
                for f in read_files:
                    with open(f, 'rb') as raw_file:
                        source_file.write(raw_file.read())

        print('Source file complete.')
        print()

        print('Preprocessing...')
        print('----------')
        os.system('python3 torch-rnn/scripts/preprocess.py '
                  '--input_txt ' + model_path + model_name + '.txt '
                  '--output_h5 ' + model_path + model_name + '.h5 '
                  '--output_json ' + model_path + model_name + '.json')
        print('----------')
        print('Preprocessing complete.')
        print()
        print('Would you like to continue to train a model, or '
              'would you like to exit?')
        print('Press enter to continune, or type "q" to exit.')
        to_train = input(': ')
        if to_train == 'q':
            sys.exit()
        choice = '1'

    # Training
    if choice == '2':
        try:
            model_name
        except NameError:
            print('What is the name of the model?')
            model_name = input(': ')
            print()
            model_path = ('model/' + model_name + '/')
            model_verify = Path(model_path + model_name + '.h5')

            while not model_verify.is_file():
                print(model_name + '.h5 does not exist.')
                print('Are you sure you typed it correctly?')
                print('Try again, or type "q" to exit.')
                model_name = input(': ')
                model_path = ('model/' + model_name + '/')
                model_verify = Path(model_path + model_name + '.h5')
                print()
                if model_name == 'q':
                    sys.exit()

        print('Are you training on a CPU or on a NVIDIA GPU?')
        print('If you would like to exit, type "q".')
        print('1. CPU')
        print('2. NVIDIA GPU')
        train_config = input(': ')
        print()

        if train_config == 'q':
            sys.exit()

        while train_config not in [1, 2]:
            print('Please specify the device.')
            print('Or type "q" to exit.')
            train_config = input(': ')
            print()
            if train_config == 'q':
                sys.exit()

        # take note of the amount of epochs used
        # this would be used for sample.py in specifying the model

        print('The follow variables have defaults. You can leave '
              'the field blank and click enter to accept these '
              'defaults if you don\'t want to change them.')
        print()

        print('Batch size?')
        print('Number of sequences to use in a minibatch.')
        print('The default is 50.')
        batch_size = input(': ')
        print()
        if batch_size == '':
            batch_size = '64'

        print('Sequence length?')
        print('Number of timesteps for which the recurrent '
              'network is unrolled for backpropagation through time.')
        print('The default is 64.')
        seq_length = input(': ')
        print()
        if seq_length == '':
            seq_length = '64'

        print('How many epochs?')
        print('The amount of epochs used for optimisation.')
        print('The default is 50.')
        num_epochs = input(': ')
        print()
        if num_epochs == '':
            num_epochs = '50'

        print('How many RNN layers?')
        print('The number of layers present in the RNN.')
        print('The default is 2.')
        num_layers = input(': ')
        print()
        if num_layers == '':
            num_layers = '2'

        # Is this the same as torch-rnn -wordvec_size?
        print('How many embedded dimensions?')
        print('Large multiples are used for larger datasets.')
        print('Specify in multiples of 64.')
        print('The default is 128.')
        embedding_dim = input(': ')
        print()
        if embedding_dim == '':
            embedding_dim = '128'

        print('How many hidden dimensions?')
        print('Large multiples are used for larger datasets.')
        print('Specify in multiples of 64.')
        print('The default is 128.')
        hidden_dim = input(': ')
        print()
        if hidden_dim == '':
            hidden_dim = '128'

        print('Zoneout?')
        print('This is a value between 0 and 1.')
        print('The default is 0.')
        zoneout = input(': ')
        print()
        if zoneout == '':
            zoneout = '0'

        print('Dropout?')
        print('This is a value between 0 and 1.')
        print('The default is 0.')
        dropout = input(': ')
        print()
        if dropout == '':
            dropout = '0'

        print('Learning Rate?')
        print('This is for optimisation.')
        print('The default is 0.002.')
        learning_rate = input(': ')
        print()
        if learning_rate == '':
            learning_rate = '0.002'

        print('How often to decay the learning rate?')
        print('This is in epochs')
        print('The default is 5.')
        lr_decay_every = input(': ')
        print()
        if lr_decay_every == '':
            lr_decay_every = '5'

        print('How much to decay the learning rate?')
        print('After every decay of the learning rate, the '
              'learning rate will be multiplied by this factor.')
        print('The default is 0.5.')
        lr_decay_factor = input(': ')
        print()
        if lr_decay_factor == '':
            lr_decay_factor = '0.5'

        print('Maximum value for gradients?')
        print('Set to 0 to disable gradient clipping.')
        print('The default is 5.')
        grad_clip = input(': ')
        print()
        if grad_clip == '':
            grad_clip = '0'

        # write model name and number of epochs to a json/csv/yaml file

        if train_config == '1':
            print('How many threads would you like to use?')
            print('It is recommended to use less than all '
                  'threads available as causes a slowdown.')
            print('Not specifying a value will use all '
                  'available threads.')
            threads = input(': ')
            print()
            print('Training...')
            os.system('set OMP_NUM_THREADS={args.threads} '
                      '| python3 -B pytorch-rnn/train.py '
                      '--input-h5 ' + model_path + model_name + '.h5 '
                      '--input-json ' + model_path + model_name + '.json '
                      '--batch-size ' + batch_size + ' '
                      '--seq-length ' + seq_length + ' '
                      '--num-epochs ' + num_epochs + ' '
                      '--num-layers ' + num_layers + ' '
                      '--embedding-dim ' + embedding_dim + ' '
                      '--hidden-dim ' + hidden_dim + ' '
                      '--zoneout ' + zoneout + ' '
                      '--dropout ' + dropout + ' '
                      '--learning-rate ' + learning_rate + ' '
                      '--lrdecay-every ' + lr_decay_every + ' '
                      '--lrdecay-factor ' + lr_decay_factor + ' '
                      '--grad-clip ' + grad_clip + ' '
                      '--checkpoint-name ' + model_path + model_name + ' '
                      '--device cpu')
            print('Training complete.')

        if train_config == '2':
            print('Training...')
            os.system('python3 -B pytorch-rnn/train.py '
                      '--input-h5 ' + model_path + model_name + '.h5 '
                      '--input-json ' + model_path + model_name + '.json '
                      '--batch-size ' + batch_size + ' '
                      '--seq-length ' + seq_length + ' '
                      '--num-epochs ' + num_epochs + ' '
                      '--num-layers ' + num_layers + ' '
                      '--embedding-dim ' + embedding_dim + ' '
                      '--hidden-dim ' + hidden_dim + ' '
                      '--zoneout ' + zoneout + ' '
                      '--dropout ' + dropout + ' '
                      '--learning-rate ' + learning_rate + ' '
                      '--lrdecay-every ' + lr_decay_every + ' '
                      '--lrdecay-factor ' + lr_decay_factor + ' '
                      '--grad-clip ' + grad_clip + ' '
                      '--checkpoint-name ' + model_path + model_name + ' '
                      '--device cuda')
            print('Training complete.')

sys.exit()
