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
    parser.add_argument('--prime', type=text_type, default=u'Ich bin der Text, der weiter geführt werden soll. Das Beste am Leben ist der ',
                       help='prime text')
    parser.add_argument('--number_of_words', type=int, default=10,
                       help='number of words')
    parser.add_argument('--number_of_trys', type=int, default=50,
                       help='number of trys')
    args = parser.parse_args()

    tmp = nextWord(args)
    print(args.prime)
    for i in range(len(tmp)):
        print(str(i+1)+".",tmp[i][0],str(round(tmp[i][1],2))+"%")

    print("")
    for i in range(len(tmp)):
        print(str(i + 1) + ".", args.prime + tmp[i][0])


def nextWord(args):
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
            retunText = model.nextPart(sess, chars, vocab, args.prime, args.number_of_words, args.number_of_trys, 0)
            #print(retunText)
    return retunText

if __name__ == '__main__':
    main()
