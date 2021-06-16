from typing import Type
import unittest
import main

class TestMain(unittest.TestCase):
  def setUp(self):
    print('about to test a function')
    
  def test_do_stuff(self):
    '''
    with test_param = 10
    '''
    test_param = 10
    result = main.do_stuff(test_param)
    self.assertEqual(result, 15)
  
  def test_do_stuff2(self):
    '''
    with test_param = 'string'
    '''
    test_param = 'string'
    result = main.do_stuff(test_param)
    self.assertIsInstance(result, ValueError)

  def test_do_stuff3(self):
    '''
    with test_param = None
    '''
    test_param = None
    result = main.do_stuff(test_param)
    self.assertEqual(result, 'provide arg')
  
  def test_do_stuff4(self):
    '''
    with test_param = 0
    '''
    test_param = 0
    result = main.do_stuff(test_param)
    self.assertEqual(result, 5)

  def tearDown(self):
    print('cleanin up')


if __name__ == '__main__':
  unittest.main() # run all the tests defined

