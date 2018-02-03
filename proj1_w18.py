import json
import requests

# Media:
# ●	Instance variables: title, author, release year
# ●	Methods: implement the following:
# ●	__len__: returns 0

class Media:
	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", json_dict=None):
		if json_dict is not None:
			self.title = jason_dict["title"]
			self.author = json_dict["writer"]
		else:
			self.title = title
			self.author = author
			self.release = release_year

# ●	__str__: returns "<title> by <author> (<release year>)", filling in the appropriate instance variables. For example "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)."
	def __str__(self):
		printing = self.title + " by " + self.author
		printing += " (" + self.release + ")\n"
		return printing

# ●	__len__: returns 0
	def __len__(self):
		return 0

sample_file_name = "sample_json.txt"
r = requests.get(sample_file_name)


# ●	Additional instance variables: album, track length
# ●	Methods:

class Song(Media):
# ●	__init__: takes title, author, release year, album, genre, and track length as arguments.
# Use named arguments with defaults. Call super( ) to initialize variables that belong to Media
	def __init__(self, album="No Album", genre="None", track_len= "0"):
		pass
# ●	__str__: add "[<genre>]" to the end of the output from Media.__str__( ).
# For example "Hey Jude by The Beatles (1968) [Rock]"
	def __str__(self, genre="No Genre"):
		pass

# ●	__len__: return track length in seconds
	def __len__(self):
		pass

# ●	Additional instance variables: rating, movie length
class Movie(Media):
# ●	__init__: takes title, author, release year, rating,
 # and movie length as arguments. Use named arguments with defaults.
 # Call super( ) to initialize variables that belong to Media.
	def __init__(self):
		pass
# ●	__str__: add "[<rating>]" to the end of the output from Media.__str__( ).
# For example "Jaws by Steven Speilberg (1975) [PG]"
	def __str__(self):
		pass
# ●	__len__: return movie length in minutes (rounded to nearest minute)
	def __len__(self):
		pass


## Other classes, functions, etc. should go here
# Main Code
if __name__ == "__main__": #below this line will run if it is a main
# your control code for Part 4 (interactive search) should go here
	pass