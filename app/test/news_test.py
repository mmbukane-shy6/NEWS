import unittest
from models import News
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to News Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_News = News(12,'Bbc','Good news','https://www.aftenposten.no,8-12-200')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()      