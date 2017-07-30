from django.test import TestCase
from myurlshortner.wsgi import *
from myurlshortner.logic import utils


class DataCleanerTestCase(TestCase):
    def test_data_cleaner(self):
        print('In test_data_cleaner')
        self.assertEquals(utils.clean_key('ABcxYz'), 'abcxyz')
        self.assertEquals(utils.clean_key('123abc789'), '123abc789')
        self.assertEquals(utils.clean_key('123a$%^bc789'), '123abc789')
        self.assertEquals(utils.clean_key('#$5^&67xyz'), '567xyz')
        self.assertEquals(utils.clean_key('a bc"\'xyz'), 'abcxyz')
