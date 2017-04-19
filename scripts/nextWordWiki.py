from __future__ import print_function
import numpy as np
import tensorflow as tf

import argparse
import time
import os
import six.moves.cPickle

from utils import TextLoader
from model import Model

from six import text_type

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default='../allSaves/saveWiki',
                       help='model directory to store checkpointed models')
    parser.add_argument('-n', type=int, default=3000,
                       help='number of characters to sample')
    parser.add_argument('--prime', type=text_type, default=u'Das Actinium wurde im Jahr ',
                       help='prime text')
    parser.add_argument('--sample', type=int, default=1,
                       help='0 to use max at each timestep, 1 to sample at each timestep, 2 to sample on spaces')
    args = parser.parse_args()

    #How many diffrent ways should be explored
    numberOfPaths = 1 #more not working?
    #how far should be explored
    numberOfWords = 150
    #stop at end of sentence
    endWithSentence = True

    results = []
    for i in range(numberOfPaths):
        tmp = sample(args)
        tmp = tmp[len(args.prime):]
        tmp.strip()
        tmp = tmp.split()
        results.append(tmp[0:numberOfWords])

    print('prime text:', args.prime)
    for i in range(numberOfPaths):
        sentence = args.prime + '~ '
        for j in range(numberOfWords):
            sentence = sentence + results[i][j]
            if '.' in results[i][j] and endWithSentence:
                break
            else:
                sentence = sentence + ' '
        print('%d. sentence:' % (i + 1), sentence)


def sample(args):
    with open(os.path.join(args.save_dir, 'config.pkl'), 'rb') as f:
        saved_args = six.moves.cPickle.load(f)
    with open(os.path.join(args.save_dir, 'chars_vocab.pkl'), 'rb') as f:
        chars, vocab = six.moves.cPickle.load(f)
    model = Model(saved_args, True)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(args.save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            retunText = model.sample(sess, chars, vocab, args.n, args.prime, args.sample)
            #print(retunText)
    return retunText

if __name__ == '__main__':
    main()
