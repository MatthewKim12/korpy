import korpy

def fix(text: str):
  return korpy.combine(korpy.extend(text))

print(fix("하ㄴ구ㄱㅇㅓ"))
