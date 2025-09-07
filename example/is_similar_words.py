import korpy

def is_similar_words(word1: str, word2: str) -> bool:
  return korpy.similarity(word1, word2)>0.8

# test
print(is_similar_words('한니발', '하이라이스')) # True
print(is_similar_words('다밭다', '잡두리')) # False
