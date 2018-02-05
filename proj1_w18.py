import json
import requests
import math
# import sample_json.txt

def opening_json_file(url):
	sample_file = open(url, 'r')
	sample_data = sample_file.read()
	sample_load = json.loads(sample_data)

	for text in range(len(sample_load)):
		if sample_load[text]["wrapperType"] == "track":
			if sample_load[text]["kind"] == "song":
				print("This is a song")
				print(Song(json_dict=sample_load[text]))
			elif sample_load[text]["kind"] == "feature-movie":
				print("This is a movie")
				print(Movie(json_dict=sample_load[text]))
			else:
				print("This is a media")
				print(Media(json_dict=sample_load[text]))










# Media:
# ●	Instance variables: title, author, release year
# ●	Methods: implement the following:
# ●	__len__: returns 0
class Media:
	# takes title, author, and release year as arguments.
	# Use named arguments with defaults.
	def __init__(self, title="No Title", author="No Author", release_year="0000", json_dict=None):
		if json_dict is not None:
			self.title = json_dict["collectionName"]
			self.author = json_dict["artistName"]
			self.release = json_dict["releaseDate"]
			self.release = self.release[:4]
		else:
			self.title = title
			self.author = author
			self.release = release_year[:4]

# ●	__str__: returns "<title> by <author> (<release year>)", filling in the appropriate instance variables. For example "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)."
	def __str__(self):
		printing = self.title + " by " + self.author + " (" + self.release + ")"
		return printing

# ●	__len__: returns 0
	def __len__(self):
		return 0

# sample_file_name = "sample_json.txt"
# r = requests.get(sample_file_name)







# ●	Additional instance variables: album, track length
# ●	Methods:

class Song(Media):
# ●	__init__: takes title, author, release year, album, genre, and track length as arguments.
# Use named arguments with defaults. Call super( ) to initialize variables that belong to Media
	def __init__(self, title="No Title", author="No Author", release_year="0000", album="No Album", genre="None", track_len='0', json_dict=None):
		if json_dict is not None:
			super().__init__(title, author, release_year, json_dict)
			self.album = json_dict["collectionName"]
			self.genre = json_dict["primaryGenreName"]
			self.track = json_dict["trackTimeMillis"]
		else:
			super().__init__(title, author, release_year, None)
			self.album = album
			self.genre = genre
			self.track= track_len
# ●	__str__: add "[<genre>]" to the end of the output from Media.__str__( ).
# For example "Hey Jude by The Beatles (1968) [Rock]"
	def __str__(self, genre="No Genre"):
		return super().__str__()+' ['+ self.genre + ']'

# ●	__len__: return track length in seconds
	def __len__(self):
		answer = float(self.track) / 1000
		return round(answer)







# ●	Additional instance variables: rating, movie length
class Movie(Media):
# ●	__init__: takes title, author, release year, rating,
 # and movie length as arguments. Use named arguments with defaults.
 # Call super( ) to initialize variables that belong to Media.
	def __init__(self, title="No Title", author="No Author", release_year="0000", rating="No Rating", movie_len="0", json_dict=None):
		if json_dict is not None:
			super().__init__(title, author, release_year, json_dict)
			self.rat = json_dict["contentAdvisoryRating"]
			self.ml = json_dict["trackTimeMillis"]
		else:
			super().__init__(title, author, release_year, None)
			self.rat = rating
			self.ml = movie_len
# ●	__str__: add "[<rating>]" to the end of the output from Media.__str__( ).
# For example "Jaws by Steven Speilberg (1975) [PG]"
	def __str__(self):
		return super().__str__() + ' ['+ self.rat + ']'
# ●	__len__: return movie length in minutes (rounded to nearest minute)
	def __len__(self):
		answer = float(self.ml) / 60000
		return round(answer)

## Other classes, functions, etc. should go here
# Main Code
if __name__ == "__main__": #below this line will run if it is a main
# your control code for Part 4 (interactive search) should go here
	pass
