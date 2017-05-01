# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dataloader import load_data
import numpy as np
import cPickle as pkl


class GenerativeClassifier(object):
    """
        meta class for generative classifiers.
    """

    def __init__(self, preprocessing="", shuffle_train=False, shuffle_test=False):
        self.x_train, self.y_train, self.x_test, self.y_test, self.feature_size = load_data(t=preprocessing)
        self.train_size = len(self.y_train)
        self.test_size = len(self.x_test)

        # TODO: reset the prior distribution
        self.pi_1 = 0

        if shuffle_train:
            idx = np.arange(self.train_size)
            np.random.shuffle(idx)
            self.x_train = [self.x_train[idx[i]] for i in range(self.train_size)]
            self.y_train = [self.y_train[idx[i]] for i in range(self.train_size)]

        if shuffle_test:
            idx = np.arange(self.test_size)
            np.random.shuffle(idx)
            self.x_test = [self.x_test[idx[i]] for i in range(self.test_size)]
            self.y_test = [self.y_test[idx[i]] for i in range(self.test_size)]


"""
    this method using Beta Distribution as the conjuncture prior.
"""


class BetaNaiveBayesClassifier(GenerativeClassifier):

    def __init__(self, alpha=500, preprocessing=""):
        super(BetaNaiveBayesClassifier, self).__init__(preprocessing=preprocessing)
        self.alpha = alpha
        self.beta = np.full((2, self.feature_size), self.alpha, dtype=float)
        self.count = [0, 0]

    def train(self):
        # TODO

    def test(self):
        # TODO




class GaussianNaiveBayesClassifier(GenerativeClassifier):

    def __init__(self, preprocessing=""):
        super(GaussianNaiveBayesClassifier, self).__init__(preprocessing=preprocessing)
        self.ML = None

    def train(self):
        #TODO


    def test(self):
       # TODO