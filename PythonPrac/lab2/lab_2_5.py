def only_english(string1):
  english_chars = [char for char in string1 if char.isalpha() and char.isascii()]
  return ''.join(english_chars)