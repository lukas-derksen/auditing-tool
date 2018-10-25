import unittest
from network.nmapscan import analyze

class TestNmapMethods(unittest.TestCase):

    def testAnalyze(self):
        data = None
        with open('nmapscandata', 'r') as file:
            data = file.read().replace('\n', '')
        analyze(data)

if __name__ == '__main__':
    unittest.main()