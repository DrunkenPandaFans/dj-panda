# -*- coding: utf-8 -*-
from unittest import TestLoader, TextTestRunner


try:
    import pymongo
except ImportError:
    print('Pymongo module is required')


if __name__ == "__main__":
    test_loader = TestLoader()
    suit = test_loader.discover('tests/', pattern='test*.py')
    res = TextTestRunner(verbosity=1).run(suit)

    raise SystemExit(not res.wasSuccessful())