import korpy
def whats_the_number(text_sound: str):
  text = korpy.from_sound(text_sound)
  return korpy.to_int(text)
def whats_the_sound(number: int):
  text = korpy.from_int(number)
  return korpy.get_sound(text)
print(whats_the_number("cheonsambeggoosibee")) # 1392
print(whats_the_sound(1392)) # "cheonsambeggoosibee"
