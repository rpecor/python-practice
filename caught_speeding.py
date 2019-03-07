# https://codingbat.com/prob/p137202
def caught_speeding(speed, is_birthday):
  if speed < 60 or (speed <= 65 and is_birthday):
    return 0
  else:
    pass