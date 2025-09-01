import korpy

all_syllables = []
for c in korpy.consonants:
  for v in korpy.vowels:
    for f in korpy.finals:
      all_syllables.append(korpy.combine(c+v+f))
print(all_syllables)
