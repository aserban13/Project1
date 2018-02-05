import unittest
import proj1_w18 as proj1 #changed name to proj1

class TestMedia(unittest.TestCase):

# This tests the __init__ function in the Media Class
    def testConstructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince", "1999")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.release, "0000")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m2.release, "1999")

# This tests the __str__ function in the Media Class
    def test_print(self):
        m1 = proj1.Media()
        m2 = proj1.Media()
        self.assertEqual(str(m1), str(m2))

        m3 = proj1.Media()
        m4 = proj1.Media("1999", "Prince", "1999")
        self.assertFalse(str(m3) == str(m4))

        self.assertEqual(str(m3), "No Title by No Author (0000)")
        self.assertEqual(str(m4), "1999 by Prince (1999)")

# This tests the __len__ function in the Media Class
    def test_length(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")
        self.assertEqual(len(m1), 0)
        self.assertEqual(len(m2), 0)

        m3 = proj1.Media("1999", "Prince", "3:19")
        self.assertEqual(len(m3), 0)
# Tests out json file and if it is extracting all the data
# and outputs the correct information
    def test_sample_med(self):
        url_name = "sample_json.json"
        m1 = proj1.opening_json_file(url_name)










class TestSong(unittest.TestCase):
# This tests the __init__ function in the Song Class
    def testSonginit(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Blank Space","Taylor Swift", "2014", "1989","pop","3:50")

        self.assertEqual(s1.title, "No Title")
        self.assertEqual(s1.author, "No Author")
        self.assertEqual(s1.release, "0000")
        self.assertEqual(s1.album, "No Album")
        self.assertEqual(s1.genre, "None")
        self.assertEqual(s1.track, "0")

        self.assertEqual(s2.title, "Blank Space")
        self.assertEqual(s2.author, "Taylor Swift")
        self.assertEqual(s2.release, "2014")
        self.assertEqual(s2.album, "1989")
        self.assertEqual(s2.genre, "pop")
        self.assertEqual(s2.track, "3:50")
# This tests the __str__ function in the Song Class
    def testSongstr(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Blank Space","Taylor Swift", "2014", "1989","pop","3:50")
        s3 = proj1.Song("Welcome to New York","Taylor Swift", "2014", "1989","pop","3:50")
        same_3 = proj1.Song("Welcome to New York","Taylor Swift", "2014", "1989","pop","3:50")

        self.assertFalse(str(s1) == str(s2))
        self.assertFalse(str(s2) == str(s3))
        self.assertEqual(str(s3), str(same_3))

        self.assertEqual(str(s2), "Blank Space by Taylor Swift (2014) [pop]")
        self.assertEqual(str(s1), "No Title by No Author (0000) [None]")

# ISSUE: Can only round to full numbers,
# not to decimal places
# This tests the __len__ function in the Song Class
    def testSonglen(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Blank Space","Taylor Swift", "2014", "1989","pop", '186600')

        # print(len(s1))
        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 187)
# Tests out json file and if it is extracting all the data
# and outputs the correct information
    def test_json(self):
        pass









class TestMovie(unittest.TestCase):

    def testMovieinit(self):
        m1 = proj1.Movie()
        m2 = proj1.Movie("Jaws", "Steven Speilberg", "1975", "PG", "2.4")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.release, "0000")
        self.assertEqual(m1.rat, "No Rating")
        self.assertEqual(m1.ml, "0")

        self.assertEqual(m2.title, "Jaws")
        self.assertEqual(m2.author, "Steven Speilberg")
        self.assertEqual(m2.release, "1975")
        self.assertEqual(m2.rat, "PG")
        self.assertEqual(m2.ml, "2.4")

    def testMoviestr(self):
        m1 = proj1.Movie()
        m2 = proj1.Movie("Jaws", "Steven Speilberg", "1975", "PG", "7451455")

        self.assertFalse(str(m1) == str(m2))
        self.assertEqual(str(m1), "No Title by No Author (0000) [No Rating]")
        self.assertEqual(str(m2), "Jaws by Steven Speilberg (1975) [PG]")

    def testMovielen(self):
        m1 = proj1.Movie()
        m2 = proj1.Movie("Jaws", "Steven Speilberg", "1975", "PG", "7451455")

        self.assertEqual(len(m1), 0)
        self.assertEqual(len(m2), 124)
# Tests out json file and if it is extracting all the data
# and outputs the correct information
    def test_json(self):
        pass
unittest.main()  #don't remove this line!
