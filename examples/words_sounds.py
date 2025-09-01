import korpy

words = korpy.words() # options: source and filter

sounds = list(map(korpy.get_sound, words))
print(sounds[:50]) # only first 50
