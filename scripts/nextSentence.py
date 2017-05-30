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
    parser.add_argument('--number_of_sentences', type=int, default=10,
                       help='number of sentences to be suggested')
    parser.add_argument('--sample', type=int, default=2,
                       help='1 for simple, 2 for complex')
    parser.add_argument('--number_of_trys', type=int, default=50,
                       help='number of trys, only used in complex')
    parser.add_argument('--min_len', type=int, default=20,
                        help='minimum length of text being suggested, only used in complex')
    args = parser.parse_args()

    tmp = nextSentence(args)
    print(args.prime)
    #print(tmp)

    if args.sample == 1:
        for i in range(len(tmp)):
            print(str(i+1)+".",tmp[i])
    else:
        for i in range(len(tmp)):
            print(str(i+1)+".",tmp[i][0],str(tmp[i][1])+"%")


def nextSentence(args):
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
            retunText = []
            if args.sample == 1:
                endTokens = ['.', '\n', '?', '!', ';', ':']
                for i in range(args.number_of_sentences):
                    sentence = model.sample(sess, chars, vocab, 500, args.prime, 1)[len(args.prime):]
                    result = ''
                    for char in sentence:
                        result += char
                        if char in endTokens:
                            break
                    retunText.append(args.prime + result)
            else:
                myText = model.nextPart(sess, chars, vocab, args.prime, args.number_of_trys, 1)
                for i in range(args.number_of_sentences):
                    if len(myText[i][0]) >= args.min_len:
                        retunText.append(myText[i])
            #print(retunText)
    return retunText

if __name__ == '__main__':
    main()
