import itertools
import random
import time

timer = 30
score = 0
dictionary = [i.strip('\n') for i in open('dictionary.txt')]

words_2 = []
words_2 = [word for word in words_2 if len(word) > 2]

def get_words(new_s, word_list):
    if not new_s:
       return word_list
    else:
        possibilities = [i for i in dictionary if all(new_s.count(b) >= i.count(b) for b in i)]
        for word in possibilities:
          words_2.append(word)
        if not possibilities:
              return get_words([], word_list)
        else:
           word = random.choice(possibilities)
           word_list.append(word)
           word_dict = {i:word.count(i) for i in word}
           new_final_word = list(itertools.chain.from_iterable([[a for i in range(abs(s.count(a)-b))] for a, b in word_dict.items()]))

found_words = []
while True:
  print('Anagrams!')
  print('A: Play')
  print('B: Rules')
  print('Q: Quit')
  print()
  
  answer = input()
  if answer == 'A' or answer == 'a':
    print()
    print('A: 6 letters')
    print('B: 7 letters')
    print()
    answer_3 = input()
    if answer_3 == 'A' or answer_3 == 'a':
      word_bank = []
      for words in dictionary: 
        if len(words) == 6:
          word_bank.append(words)
      selected = random.choice(word_bank)
      s = ''.join(random.sample(selected, len(selected)))
      final_words = get_words(s, [])
      start_time = time.time()
      while time.time() - start_time < timer:
        print()
        print('Letters: ' + s)
        print()
        guess = input('Unscramble: ')
        if guess in words_2:
          if len(guess) == 6:
            print('+2000')
            score = score + 2000
            found_words.append(guess)
          elif len(guess) == 5:
            print('+1200')
            score = score + 1200
            found_words.append(guess)
          elif len(guess) == 4:
            print('+400')
            score = score + 400
            found_words.append(guess)
          elif len(guess) == 3:
            print('+100')
            score = score + 100
            found_words.append(guess)
      print()
      print('Times up!')
      print('Your score: ' + str(score))
      print('Words you found:', end=' ')
      for word in found_words:
        print(word, end=' ')
      break
    elif answer_3 == 'B' or answer_3 == 'b':
      word_bank = []
      for words in dictionary: 
        if len(words) == 7:
          word_bank.append(words)
      selected = random.choice(word_bank)
      s = ''.join(random.sample(selected, len(selected)))
      words_2.clear()
      final_words = get_words(s, [])
      start_time = time.time()
      while time.time() - start_time < timer:
        print()
        print('Letters: ' + s)
        print()
        guess = input('Unscramble: ')
        if guess in words_2:
          if len(guess) == 6:
            print('+2000')
            score = score + 2000
            found_words.append(guess)
          elif len(guess) == 5:
            print('+1200')
            score = score + 1200
            found_words.append(guess)
          elif len(guess) == 4:
            print('+400')
            score = score + 400
            found_words.append(guess)
          elif len(guess) == 3:
            print('+100')
            score = score + 100
            found_words.append(guess)
      print()
      print('Times up!')
      print('Your score: ' + str(score))
      print('Words you found:', end=' ')
      for word in found_words:
        print(word, end=' ')
    break
  elif answer == 'B' or answer == 'b':
    print()
    print('To play anagrams, you need to rearrange the random letters given to you into words by typing in your guesses. You only have 30 seconds to type as many words as you can! Two letter words will not count.')
    print('A: Back')
    while True:
      answer_2 = input()
      if answer_2 == 'A' or answer_2 == 'a':
        print()
        break
  elif answer == 'Q' or answer == 'q':
    print()
    print('Thank you for playing!')
    break
  else:
    print()
    print('Not a valid answer.')
    break