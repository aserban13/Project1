import json
import requests
import math
import webbrowser
# import sample_json.txt

# Media:
# ●	Instance variables: title, author, release year
# ●	Methods: implement the following:
# ●	__len__: returns 0
class Media:
	# takes title, author, and release year as arguments.
	# Use named arguments with defaults.
	def __init__(self, title="No Title", author="No Author", release_year="0000", json_dict=None):
		if json_dict is not None:
			if json_dict["wrapperType"] == "track":
				self.title = json_dict["trackName"]
			else:
				self.title = json_dict["collectionName"]
			self.author = json_dict["artistName"]
			self.release = json_dict["releaseDate"]
			self.release = self.release[:4]
			try:
				self.url = json_dict["collectionViewUrl"]
			except:
				pass
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
			self.url = json_dict['trackViewUrl']
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
			self.url = json_dict["trackViewUrl"]
			try:
				self.ml = json_dict["trackTimeMillis"]
			except:
				pass
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


#Find 50 of the different types of media in itunes using the
# query term
#param: a key search string
#return: a list of the 50 results that show up
result_list = []
song_list = []
movie_list = []
media_list = []

def itunes_search(query="##!!"):
	data = requests.get('https://itunes.apple.com/search?', params = { 'term' : query})
	sample_load = json.loads(data.text)['results']

	num = 0
	del result_list[:]
	del song_list[:]
	del movie_list[:]
	del media_list[:]
	for text in range(len(sample_load)):
		if sample_load[text]["wrapperType"] == "track":
			if sample_load[text]["kind"] == "song":
				found_song = Song(json_dict=sample_load[text])
				num += 1
				tup = (num, found_song, found_song.url)
				song = found_song
				results = found_song
				song_list.append(tup)
				result_list.append(tup)

	for text in range(len(sample_load)):
		if sample_load[text]["wrapperType"] == "track":
			if sample_load[text]["kind"] == "feature-movie":
				found_movie = Movie(json_dict=sample_load[text])
				num += 1
				tup = (num, found_movie, found_movie.url)
				movie = found_movie
				results = found_movie
				movie_list.append(tup)
				result_list.append(tup)

	for text in range(len(sample_load)):
		if sample_load[text]["wrapperType"] != "track":
			found_media = Media(json_dict=sample_load[text])
			num += 1
			tup = (num, found_media, found_media.url)
			media = found_media
			results= found_media
			media_list.append(tup)
			result_list.append(tup)


def print_itunes():
	# if (len(song_list) != 0 and len(media_list) != 0 and len(movie_list) != 0):
	print("\nSONGS")
	for song in song_list:
		print(song[0], song[1])

	print("\nMOVIES")
	for movie in movie_list:
		print(movie[0], movie[1])

	print("\nOTHER MEDIA")
	for media in media_list:
		print(media[0], media[1])
		print("\n\n")
	# else:
	# 	print("There are no results for this search")

def access_itunes_web(inputs):
	try:
		num = int(inputs)
		for result in result_list:
			if result[0] == num:
				print("Launching ", result[2], " in a web browser ...")
				webbrowser.open_new_tab(result[2])
	except:
		pass

def access_itunes_search(inputs):
	try:
		itunes_search(inputs)
		print_itunes()
	except:
		pass


## Other classes, functions, etc. should go here
# Main Code

if __name__ == "__main__": #below this line will run if it is a main
# your control code for Part 4 (interactive search) should go here

	term = input("Enter a search term, or 'exit' to quit: ")
	itunes_search(term)
	print_itunes()

	# term = input("Enter a number for more info, or another search term, or exit: ")
	while term != "exit":
		try:
			term = input("Enter a number for more info, or another search term, or exit: ")
			if term != "exit":
				access_itunes_web(term)
				access_itunes_search(term)
		except:
			print("This is not a proper entry.")
