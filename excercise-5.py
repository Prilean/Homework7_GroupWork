#SOEUNG_Phearaneron_2022296
def backward_string_by_word(words):
  return ' '.join(word[::-1] for word in words.split(' '))
