import unittest
import proj1_w18 as proj1 #changed name to proj1

class TestMedia(unittest.TestCase):

    def testConstructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")

    def test_print(self):
        m1 = proj1.Media()
        m2 = proj2.Media()
        self.assertEqual(str(m1), str(m2))

    def test_length(self):
        m1 = proj1.Media()
        m2 = proj1.Media()
        self.assertEqual(len(m1), 0)
unittest.main()  #don't remove this line!
