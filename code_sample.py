from typing import List, Tuple


ComparisonsType = List[Tuple[str, str]]


def get_comparisons(word_list: str) -> Tuple[ComparisonsType, List[str]]:
  """Get all relevant comparisons between characters as well as a list of all characters 
    in the given alphabet

    Args:
        word_list: the list of words that contains enough information to decide the order
                    of the alphabet

    Returns:
        comparisons: List of tuples representing the relationships between characters
        characters: List of all characters that occur in the given alphabet

  """
  comparisons: ComparisonsType = []
  characters: List[str] = []

  for i in range(1, len(word_list)):
    word0 = word_list[i-1]
    word1 = word_list[i]
    shortest_word_length = len(word0) if len(word0) < len(word1) else len(word1)

    for i in range(0, len(word0)):
      if (word0[i] not in characters):
        characters.append(word0[i])

    for i in range(0, shortest_word_length):
      
      if (word0[i] != word1[i]):
        comparisons.append((word0[i], word1[i]))
        break

  return (comparisons, characters)


def remove_letter_from_comparisons(letter_to_remove: str, comparisons: ComparisonsType) -> ComparisonsType:
  """Remove all occurances of a certain character from the comparisons list

  Args:
        letter: str, character to remove
        comparisons: List of tuples representing the relationships between characters

    Returns:
        new_comparisons: new List of tuples representing the relationships between characters 
                            without the character that was removed

  """
  for item in comparisons:
    if (item[0] == letter_to_remove):
      comparisons = list(filter(lambda a: a != item, comparisons))

  return comparisons


def is_letter_behind_other_letter(letter: str, comparisons: ComparisonsType) -> bool:
  """Check if a character comes behind any other characters in the comparisons list

  Args:
        letter: str, character to check
        comparisons: List of tuples representing the relationships between characters

    Returns:
        is_letter_behind_other_letter: bool, if the character is behind any other characters in the comparisons list
  
  """
  for item in comparisons:
    if (item[1] == letter):
      return True
  return False


def find_next_letter(comparisons: ComparisonsType) -> str:
  """Find the next character than does not come after any other characters in the list of comparisons.
  
  Args:
        comparisons: List of tuples representing the relationships between characters

    Returns:
        next_letter: str, the character that does not come behind any other characters in the comparisons list
  """
  for item in comparisons:
    if (not is_letter_behind_other_letter(item[0], comparisons)):
      return item[0]


def decide_alphabet(word_list: List[str]) -> List[str]:
  """Decide alphabet from alphabetical list of words

    Algorithm:
        assume the first character of the first word is the first character in the alphabet

        iterate through each word and compare to the following word to generate a 
        complete list of relations between characters, (ex. a comes before b, a comes before c,
        b comes before c). Also generate a complete list of character in the alphabet.

        remove the first character in the alphabet from the list of character comparison relations 
        and remove from the list of characters. This character is the first character in the alphabet.

        loop while there are remaining comparisons. 

        Find the next character than does not come after any other characters in the list of comparisons. 
        remove all comparisons that contain this character, add it to the alphabet as the next character and 
        remove from the characters list. 

        when there are no remaining comparisons, add any remaining characters to the end of the alphabet 
        and return.

    Args:
        word_list: List of strings representing words in alphabetical order, according to
                    any given alphabet. word_list must have enough information to determine
                    the complete order of the alphabet

    Returns:
        alphabet: List of characters that make up the order of the given alphabet

  """
  if (len(word_list) <= 1):
    return []

  alphabet: List[str] = [word_list[0][0]]

  result = get_comparisons(word_list)

  characters = result[1]

  comparisons = remove_letter_from_comparisons(alphabet[0], result[0])
  characters.remove(alphabet[0])

  while (len(comparisons) > 0):
    next_letter = find_next_letter(comparisons)
    alphabet.append(next_letter)
    characters.remove(next_letter)
    comparisons = remove_letter_from_comparisons(next_letter, comparisons)

  return alphabet+characters
