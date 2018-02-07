import unittest
import json
import proj1_w18 as proj1 #changed name to proj1





class TestMedia(unittest.TestCase):

# This tests the __init__ function in the Media Class
    def testConstructor(self):
        m1 = proj1.Media(json_dict=None)
        m2 = proj1.Media("1999", "Prince", "1999", json_dict=None)

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.release, "0000")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m2.release, "1999")

# This tests the __str__ function in the Media Class
    def test_print(self):
        m1 = proj1.Media(json_dict=None)
        m2 = proj1.Media(json_dict=None)
        self.assertEqual(str(m1), str(m2))

        m3 = proj1.Media(json_dict=None)
        m4 = proj1.Media("1999", "Prince", "1999", json_dict=None)
        self.assertFalse(str(m3) == str(m4))

        self.assertEqual(str(m3), "No Title by No Author (0000)")
        self.assertEqual(str(m4), "1999 by Prince (1999)")

# This tests the __len__ function in the Media Class
    def test_length(self):
        m1 = proj1.Media(json_dict=None)
        m2 = proj1.Media("1999", "Prince", json_dict=None)
        self.assertEqual(len(m1), 0)
        self.assertEqual(len(m2), 0)

        m3 = proj1.Media("1999", "Prince", "3:19", json_dict=None)
        self.assertEqual(len(m3), 0)


# Part Two Testing:
# Tests out json file and if it is extracting the correct information
# from the sample file for a media.


    def test_sample_med(self):
        url_name = "sample_json.json"
        sample_file = open((url_name), 'r')
        sample_data = sample_file.read()
        sample_load = json.loads(sample_data)
        m1 = proj1.Media(json_dict=sample_load[2])
        self.assertEqual(m1.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(m1.author, "Helen Fielding")
        self.assertEqual(m1.release, "2012")
        sample_file.close()
















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


# Part Two Testing:
# Tests out json file and if it is extracting the correct information
# from the sample file for a song.



    def test_sample_song(self):
        url_name = "sample_json.json"
        sample_file = open((url_name), 'r')
        sample_data = sample_file.read()
        sample_load = json.loads(sample_data)
        s1 = proj1.Song(json_dict=sample_load[1])
        self.assertEqual(s1.title, "Hey Jude")
        self.assertEqual(s1.author, "The Beatles")
        self.assertEqual(s1.release, "1968")
        self.assertEqual(s1.album, "TheBeatles 1967-1970 (The Blue Album)")
        self.assertEqual(s1.genre, "Rock")
        self.assertEqual(s1.track, 431333)
        sample_file.close()









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

# Part Two Testing:
# Tests out json file and if it is extracting the correct information
# from the sample file for a movie.



    def test_sample_movie(self):
        url_name = "sample_json.json"
        sample_file = open((url_name), 'r')
        sample_data = sample_file.read()
        sample_load = json.loads(sample_data)
        m1 = proj1.Movie(json_dict=sample_load[0])
        self.assertEqual(m1.title, "Jaws")
        self.assertEqual(m1.author, "Steven Spielberg")
        self.assertEqual(m1.release, "1975")
        self.assertEqual(m1.rat, "PG")
        self.assertEqual(m1.ml, 7451455)
        sample_file.close()






# Part Three Testing:
# With a list of terms will run the fucntion and the assert statemnt
# makes sure that there is less than 50 results.
# Since the expected behavior of the itunes API is return a max of
# 50 results.




    def test_json_itunes(self):
        terms = {"baby", "sweet", "love", "moana",
                "helter skelter", "Andreea", "##!!"
                " ", "   "}
        for term in terms:
            proj1.itunes_search(term)
            self.assertTrue(len(proj1.result_list) <= 50)


unittest.main()  #don't remove this line!
