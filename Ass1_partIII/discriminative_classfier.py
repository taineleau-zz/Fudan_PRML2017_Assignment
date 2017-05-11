from dataloader import *
import numpy as np
from numpy.linalg import pinv, norm


class DiscriminativeClassifier(object):
    def __init__(self,preprocessing="", bias=False):
        self.x_train, self.y_train, self.x_test, self.y_test, self.feature_size = \
            load_data(t=preprocessing, bias=bias)
        self.train_size = len(self.y_train)
        self.test_size = len(self.x_test)

def sigmoid(x):
    return 1.0 / (1.0 + np.exp((-1)*x))


# calc gradient (and/or Hessian matrix)
# TODO: you should implement gradient descent or other optimizer to this
#        so please calculate the gradient (and/or) hessian in this function
#        to help TA undertand your code
#        notice that you are only allow to use numpy here
def calc_grad(W, X, Y):
    # W: weight matrix
    # X: input
    # Y: ground true
    # TODO: write your code here :D
    grad, Hess = None, None
    return grad, Hess


class LogisticRegression(DiscriminativeClassifier):

    def __init__(self, l2norm=1, preprocessing="", eta=1e-4, max_epoch=30, l2_on=False):
        """
        :param l2norm: l2 norm penalty
        :param preprocessing: preprocessing method
        :param eta: learning rate (step size)
        :param max_epoch: how many epochs are you going to train the regression (optional)
        :param l2_on: use l2 or not
        """
        super(LogisticRegression, self).__init__(preprocessing=preprocessing, bias=True)
        self.weight = np.ones((self.feature_size + 1, 1))
        self.L2norm = l2norm
        self.eta = eta
        self.max_epoch = max_epoch
        self.l2_on = l2_on
        # mask is to filter out the weight and discard the bias
        self.mask = np.ones_like(self.weight)
        self.mask[self.feature_size][0] = 0

    def train(self, eps=1e-4):
        epoch = 0
        while True:

            # TODO: calc update here using calc_grad() or anything you want
            update = 0
            # update weight
            self.weight = self.weight

            if norm(update) < self.eta * 0.1: # TODO: you should think about some early stopping scheme here
                break

            epoch += 1

            print "epoch", epoch
            if epoch > self.max_epoch:
                break

    def test(self):
        err = 0
        return err


class KNNClassifier(DiscriminativeClassifier):

    def __init__(self, preprocessing="", K=4):
        """

        :param preprocessing: preprocessing method
        :param K: how much neighbours you want
        """
        super(KNNClassifier, self).__init__(preprocessing=preprocessing)
        self.binary = (preprocessing == "binary")
        self.K = K

    # TODO: implement distance between sample here
    def __calc_distance(self, a, b):
        if self.binary:
            return
        else:
            return

    def train(self):
        # TODO
        return

    def test(self):
        # TODO
        err = 0
        return err
