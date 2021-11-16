import numpy
import sympy

class GenLookAndSay():
  """docstring for GenLookAndSay"""
  def __init__(self, chunk_op = (lambda a,n : str(n) + a)):
    super(GenLookAndSay, self).__init__()
    self.chunk_op = chunk_op
    self.sequence = []

  def set_chunk_op(self, chunk_op):
    self.chunk_op = chunk_op

  def get_sequence(self):
    return self.sequence

  def say_what_you_see(self, word):
    if not word: return None # handles empty word, which is falsy
    letter = word[0]
    result = ''
    count = 0
    for ch in word:
      if ch == letter: 
        count += 1
      else:
        result += self.chunk_op(letter, count)
        count = 1
        letter = ch 
    result += self.chunk_op(letter, count)
    return result
   
  def generate_sequence(self, seed, num_iterations):
    if not seed: return None # handles empty seed, which is falsy
    result = [seed]
    for _ in range(num_iterations):
      result.append(self.say_what_you_see(result[-1]))
    self.sequence = result

  def get_length_ratio(self):
    if len(self.sequence) < 2:
      print('Look and say sequence does not have enough rows to compute the ratio of lengths.')
      return None
    return len(self.sequence[-1]) / len(self.sequence[-2])

class LookAndSay():
  """docstring for LookAndSay"""
  def __init__(self, say = (lambda n : str(n))):
    super(LookAndSay, self).__init__()
    self.say = say
    self.sequence = []

  def set_say(self, say):
    self.say = say

  def get_sequence(self):
    return self.sequence

  def say_what_you_see(self, word):
    if not word: return None # handles empty word, which is falsy
    letter = word[0]
    result = ''
    count = 0
    for ch in word:
      if ch == letter: 
        count += 1
      else:
        result += self.say(count) + letter
        count = 1
        letter = ch 
    result += self.say(count) + letter
    return result
   
  def generate_sequence(self, seed, num_iterations):
    if not seed: return None # handles empty seed, which is falsy
    result = [seed]
    for _ in range(num_iterations):
      result.append(self.say_what_you_see(result[-1]))
    self.sequence = result

  def get_length_ratio(self):
    if len(self.sequence) < 2:
      print('Look and say sequence does not have enough rows to compute the ratio of lengths.')
      return None
    return len(self.sequence[-1]) / len(self.sequence[-2])


########### Knave #####################

class LookKnave(LookAndSay):
  """docstring for LookKnave"""
  def __init__(self, say, lie = None):
    super().__init__(say)
    self.lie = lie
    if lie == None:
      def lie_a_bit(bit):
        if bit == '0':
          return '1'
        if bit == '1':
          return '0'

      self.lie = lie_a_bit

  def say_what_you_see(self, word):
    """override"""
    if not word: return None # handles empty word, which is falsy
    letter = word[0]
    result = ''
    count = 0
    for ch in word:
      if ch == letter: 
        count += 1
      else:
        result += self.say(count) + self.lie(letter)
        count = 1
        letter = ch 
    result += self.say(count) + self.lie(letter)
    return result

########### CHEMISTRY #####################

class Chemistry():
  """docstring for Chemistry"""
  def __init__(self, las, splitting_strategy = None, elements = None):
    super(Chemistry, self).__init__()
    self.las = las
    if splitting_strategy == None:
      splitting_strategy = ConwaySplittingStrategy()
    self.splitting_strategy = splitting_strategy
    if elements == None:
      elements = []
    self.elements = elements

  def get_elements(self):
    return self.elements

  def clear_elements(self):
    self.elements = []

  def split_to_elements(self, string): 
    return [Element(chunk, self.las) for chunk in self.splitting_strategy.split(string)]

  def generate_all_elements(self, strings):
    for string in strings:
      for elt in self.split_to_elements(string):
        if elt not in self.elements:
          # add elt to the chemistry:
          self.elements.append(elt)
          # recursively set the decay for elt:
          decay_elts = self.split_to_elements(self.las.say_what_you_see(elt.get_string()))
          self.generate_all_elements(map(lambda e : e.get_string(), decay_elts))
          elt.set_decay(decay_elts)
    # clean up decay for all elements:
    for elt in self.elements:
      dec = []
      for d in elt.get_decay():
        dec += [e for e in self.elements if e == d]
      elt.set_decay(dec)

  def remove_extinct_elements(self): 
    while True:
      common_elements = []
      for elt in self.elements:
        for d in elt.get_decay():
          if d not in common_elements:
            common_elements.append(d)
      if len(common_elements) < len(self.elements):
        self.elements = common_elements[:]
      else: 
        break

  def generate_elements(self, seeds, reset = True):
    if reset:
      self.clear_elements()
    strings = [self.las.say_what_you_see(seed) for seed in seeds] #only look at 2-day-old strings
    self.generate_all_elements(strings)
    self.remove_extinct_elements()

  def get_decay_matrix(self):
    mat = []
    e = self.elements
    for i in range(len(e)):
      row = []
      for j in range(len(e)):
        row.append(e[j].get_decay().count(e[i]))
      mat.append(row)
    return mat

  def get_max_eigenvalue(self):
    eigenstuff = numpy.linalg.eig(numpy.array(self.get_decay_matrix()))
    eigenvalues = eigenstuff[0]
    return max(eigenvalues).real

  def get_char_poly(self, factored = True):
    chi = sympy.Matrix(self.get_decay_matrix()).charpoly()
    if factored:
      return sympy.factor(chi.as_expr())
    else:
      return chi.as_expr()

class BinaryChemistry(Chemistry):
  """docstring for BinaryChemistry"""
  def __init__(self, las, elements = None):
    super().__init__(las, Leading1SplittingStrategy(), elements)

class Leading1Chemistry(Chemistry):
  """docstring for Leading1Chemistry"""
  def __init__(self, las, elements = None):
    super().__init__(las, Leading1SplittingStrategy(), elements)

class Leading0Chemistry(Chemistry):
  """docstring for Leading1Chemistry"""
  def __init__(self, las, elements = None):
    super().__init__(las, Leading0SplittingStrategy(), elements)

class Ending0Chemistry(Chemistry):
  """docstring for Ending0Chemistry"""
  def __init__(self, las, elements = None):
    super().__init__(las, Ending0SplittingStrategy(), elements)

class EndingWithCharsChemistry(Chemistry):
  """docstring for EndingWithCharsChemistry"""
  def __init__(self, las, ending_characters, elements = None):
    super().__init__(las, EndingWithCharsSplittingStrategy(ending_characters), elements)

class Element():
  """docstring for Element"""
  def __init__(self, string, las, decay = []):
    super(Element, self).__init__()
    self.string = string
    self.las = las
    self.name = string
    self.decay = decay

  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name

  def __eq__(self, other):
    """Overrides the default implementation"""
    if isinstance(other, Element):
        return self.string == other.string and self.las == other.las
    return NotImplemented

  def __hash__(self):
    """Overrides the default implementation"""
    return hash(tuple(sorted(self.__dict__.items())))

  def set_decay(self, elements):
    self.decay = elements

  def get_decay(self):
    return self.decay

  def set_name(self, name):
    self.name = name

  def get_name(self):
    return self.name

  def get_string(self):
    return self.string

########### SPLITTING STRATEGY #####################

class SplittingStrategy():
  """docstring for SplittingStrategy"""
  def __init__(self, splitting_function):
    self.splitting_function = splitting_function

  def split(self, string):
    self.splitting_function(string)


class SplittingStrategyBySplittablePairs(SplittingStrategy):
  """docstring for SplittingStrategyBySplittablePairs"""
  def __init__(self):
    super().__init__(None)
  
  def is_split(self, L, R):
    pass

  def split(self, string):
    chunks = []
    start = 0
    for i in range(1, len(string)):
      if self.is_split(string[start:i], string[i:]):
        chunks.append(string[start:i])
        start = i
    chunks.append(string[start:])
    return chunks


class Ending0SplittingStrategy(SplittingStrategyBySplittablePairs):
  """docstring for Ending0SplittingStrategy"""
  def __init__(self):
    super().__init__()

  def is_split(self, L, R):
    if L == '' or R == '':
        return True
    return L[-1] == '0' and R[0] != '0'

class EndingWithCharsSplittingStrategy(SplittingStrategyBySplittablePairs):
  """docstring for EndingWithCharsSplittingStrategy"""
  def __init__(self, ending_characters):
    super().__init__()
    self.ending_characters = ending_characters

  def is_split(self, L, R):
    if L == '' or R == '':
        return True
    return L[-1] in self.ending_characters and R[0] not in self.ending_characters

class LeadingCharSplittingStrategy(SplittingStrategyBySplittablePairs):
  """docstring for LeadingCharSplittingStrategy"""
  def __init__(self, leading_chars):
    super().__init__()
    self.leading_chars = leading_chars

  def is_split(self, L, R):
    if L == '' or R == '':
        return True
    return L[-1] not in self.leading_chars and L[-1] != R[0]

class Leading1SplittingStrategy(LeadingCharSplittingStrategy):
  """docstring for Leading1SplittingStrategy"""
  def __init__(self):
    super().__init__('1')

class Leading0SplittingStrategy(LeadingCharSplittingStrategy):
  """docstring for Leading1SplittingStrategy"""
  def __init__(self):
    super().__init__('0')

class ConwaySplittingStrategy(SplittingStrategyBySplittablePairs):
  """docstring for ConwaySplittingStrategy"""
  def __init__(self):
    super().__init__()

  def is_split(self, L, R):
    # Implementing Conway's Splitting Theorem:
    if L == '' or R == '':
        return True
    if L[-1] not in ['1', '2', '3'] and R[0] in ['1', '2', '3']: # n] and [m
        return True
    if L[-1] == '2': # 2]
        if len(R) > 1 and R[0] == '1' and R[1] != '1' and (len(R) == 2 or R[2] != R[1]): #[1^1X^1
            return True
        if len(R) > 2 and R[0] == '1' and R[1] == '1' and R[2] == '1' and (len(R) == 3 or R[3] != '1'): #[1^3
            return True
        if R[0] == '3' and (len(R) == 1 or (R[1] != '3' and (len(R) < 4 or R[2] != R[1] or R[3] != R[1]))): #[3^1X^\not=3
            return True
        if R[0] not in ['1', '2', '3'] and (len(R) == 1 or R[1] != R[0]): #[n^1
            return True
    if L[-1] != '2' and len(R) > 1 and R[0] == '2' and R[1] == '2': # \not=2]
        if len(R) > 3 and R[2] == '1' and R[3] != '1' and (len(R) == 4 or R[4] != R[3]): #[2^21^1X^1
            return True
        if len(R) > 4 and R[2] == '1' and R[3] == '1' and R[4] == '1' and (len(R) == 5 or R[5] != '1'): #[2^21^3
            return True
        if len(R) > 2 and R[2] == '3' and (len(R) == 3 or (R[3] != '3' and (len(R) < 6 or R[4] != R[3] or R[5] != R[3]))): #[2^23^1X^\not=3
            return True 
        if len(R) == 2 or (len(R) > 2 and R[2] not in ['1', '2', '3'] and (len(R) == 3 or R[3] != R[2])): #[2^2n^(0 or 1)
            return True
    return False


