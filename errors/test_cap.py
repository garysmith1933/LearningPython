# test simple first, then complicated things

import unittest
import cap

class TestCap(unittest.TestCase):

  def test_one_word(self):
    text = 'python'
    result = cap.cap_text(text)
    #result should be equal to whatever text is captialized, in this case. Python
    self.assertEqual(result, 'Python')

  def test_multiple_words(self):
    text = 'monty python'
    result = cap.cap_text(text)
    self.assertEqual(result, 'Monty Python')

if __name__=='__main__':
  unittest.main()