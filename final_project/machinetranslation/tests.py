import unittest

from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    
    def test2(self):
        self.assertEqual(englishToFrench(''), None)
    
    def test3(self):
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    
    def test2(self):  
        self.assertEqual(frenchToEnglish(''), None)
    
    def test3(self):    
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')


if __name__ == "__main__":
    unittest.main()