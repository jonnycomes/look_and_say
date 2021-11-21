"""
    A module for playing with look and say sequences in the spirit of John Conway.
"""

import numpy
import sympy

################## Conway's Conventions ############################

def split_Conway(string):
    """
    Splits a string into a list of substrings according to Conway's Splitting Theorem.
    Assumes the string is not empty. 

    ## Example Session:
    ```python
    string = '1211132213'
    chunks = split_Conway(string)
    print(chunks)
    ```
    ### Output:

    ```sh
    ['12', '1113', '22', '13']
    ```
    """
    chunks = []
    start = 0
    for i in range(1, len(string)):
        if _is_split_pair_Conway(string[start:i], string[i:]):
            chunks.append(string[start:i])
            start = i
    chunks.append(string[start:])
    return chunks

def _is_split_pair_Conway(L, R):
    """Implementation of Conway's Splitting Theorem"""
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

_CONWAY_ELEMENTS = {'3': {'name': 'U', 'number': 92}, '13': {'name': 'Pa', 'number': 91}, '1113': {'name': 'Th', 'number': 90}, '3113': {'name': 'Ac', 'number': 89}, '132113': {'name': 'Ra', 'number': 88}, '1113122113': {'name': 'Fr', 'number': 87}, '311311222113': {'name': 'Rn', 'number': 86}, '1322113': {'name': 'At', 'number': 85}, '1113222113': {'name': 'Po', 'number': 84}, '3113322113': {'name': 'Bi', 'number': 83}, '123222113': {'name': 'Pb', 'number': 82}, '111213322113': {'name': 'Tl', 'number': 81}, '31121123222113': {'name': 'Hg', 'number': 80}, '132112211213322113': {'name': 'Au', 'number': 79}, '111312212221121123222113': {'name': 'Pt', 'number': 78}, '3113112211322112211213322113': {'name': 'Ir', 'number': 77}, '1321132122211322212221121123222113': {'name': 'Os', 'number': 76}, '111312211312113221133211322112211213322113': {'name': 'Re', 'number': 75}, '312211322212221121123222113': {'name': 'W', 'number': 74}, '13112221133211322112211213322113': {'name': 'Ta', 'number': 73}, '11132': {'name': 'Hf', 'number': 72}, '311312': {'name': 'Lu', 'number': 71}, '1321131112': {'name': 'Yb', 'number': 70}, '11131221133112': {'name': 'Tm', 'number': 69}, '311311222': {'name': 'Er', 'number': 68}, '1321132': {'name': 'Ho', 'number': 67}, '111312211312': {'name': 'Dy', 'number': 66}, '3113112221131112': {'name': 'Tb', 'number': 65}, '13221133112': {'name': 'Gd', 'number': 64}, '1113222': {'name': 'Eu', 'number': 63}, '311332': {'name': 'Sm', 'number': 62}, '132': {'name': 'Pm', 'number': 61}, '111312': {'name': 'Nd', 'number': 60}, '31131112': {'name': 'Pr', 'number': 59}, '1321133112': {'name': 'Ce', 'number': 58}, '11131': {'name': 'La', 'number': 57}, '311311': {'name': 'Ba', 'number': 56}, '13211321': {'name': 'Cs', 'number': 55}, '11131221131211': {'name': 'Xe', 'number': 54}, '311311222113111221': {'name': 'I', 'number': 53}, '1322113312211': {'name': 'Te', 'number': 52}, '3112221': {'name': 'Sb', 'number': 51}, '13211': {'name': 'Sn', 'number': 50}, '11131221': {'name': 'In', 'number': 49}, '3113112211': {'name': 'Cd', 'number': 48}, '132113212221': {'name': 'Ag', 'number': 47}, '111312211312113211': {'name': 'Pd', 'number': 46}, '311311222113111221131221': {'name': 'Rh', 'number': 45}, '132211331222113112211': {'name': 'Ru', 'number': 44}, '311322113212221': {'name': 'Tc', 'number': 43}, '13211322211312113211': {'name': 'Mo', 'number': 42}, '1113122113322113111221131221': {'name': 'Nb', 'number': 41}, '12322211331222113112211': {'name': 'Zr', 'number': 40}, '1112133': {'name': 'Y', 'number': 39}, '3112112': {'name': 'Sr', 'number': 38}, '1321122112': {'name': 'Rb', 'number': 37}, '11131221222112': {'name': 'Kr', 'number': 36}, '3113112211322112': {'name': 'Br', 'number': 35}, '13211321222113222112': {'name': 'Se', 'number': 34}, '11131221131211322113322112': {'name': 'As', 'number': 33}, '31131122211311122113222': {'name': 'Ge', 'number': 32}, '13221133122211332': {'name': 'Ga', 'number': 31}, '312': {'name': 'Zn', 'number': 30}, '131112': {'name': 'Cu', 'number': 29}, '11133112': {'name': 'Ni', 'number': 28}, '32112': {'name': 'Co', 'number': 27}, '13122112': {'name': 'Fe', 'number': 26}, '111311222112': {'name': 'Mn', 'number': 25}, '31132': {'name': 'Cr', 'number': 24}, '13211312': {'name': 'V', 'number': 23}, '11131221131112': {'name': 'Ti', 'number': 22}, '3113112221133112': {'name': 'Sc', 'number': 21}, '12': {'name': 'Ca', 'number': 20}, '1112': {'name': 'K', 'number': 19}, '3112': {'name': 'Ar', 'number': 18}, '132112': {'name': 'Cl', 'number': 17}, '1113122112': {'name': 'S', 'number': 16}, '311311222112': {'name': 'P', 'number': 15}, '1322112': {'name': 'Si', 'number': 14}, '1113222112': {'name': 'Al', 'number': 13}, '3113322112': {'name': 'Mg', 'number': 12}, '123222112': {'name': 'Na', 'number': 11}, '111213322112': {'name': 'Ne', 'number': 10}, '31121123222112': {'name': 'F', 'number': 9}, '132112211213322112': {'name': 'O', 'number': 8}, '111312212221121123222112': {'name': 'N', 'number': 7}, '3113112211322112211213322112': {'name': 'C', 'number': 6}, '1321132122211322212221121123222112': {'name': 'B', 'number': 5}, '111312211312113221133211322112211213322112': {'name': 'Be', 'number': 4}, '312211322212221121123222112': {'name': 'Li', 'number': 3}, '13112221133211322112211213322112': {'name': 'He', 'number': 2}, '22': {'name': 'H', 'number': 1}}

def _conway_name(element):
    string = element.get_string()
    if string in _CONWAY_ELEMENTS:
        return _CONWAY_ELEMENTS[string]['name']
    Pu = '31221132221222112112322211n'
    Np = '1311222113321132211221121332211n'
    if len(string) == len(Pu) and string[:-1] == Pu[:-1]:
        return 'Pu' + string[-1]
    if len(string) == len(Np) and string[:-1] == Np[:-1]:
        return 'Np' + string[-1]
    return element.get_name()

def _conway_number(element):
    string = element.get_string()
    if string in _CONWAY_ELEMENTS:
        return _CONWAY_ELEMENTS[string]['number']
    else: # Handling transuranic elements
        return 92 * len(string) + ord(string[-1])

################# LOOK AND SAY #################################

class LookAndSay():
    """
    A class responsible for the fundamental say-what-you-see operation
    that generates a look and say sequence. The parameter ``say`` in the
    constructor is a function that determines the decay of chunk of the form
    \\(a^b\\). The say function can have one or two parameters:

    * If the say function accepts one parameter, the LookAndSay object will correspond to the decay \\(a^b\\to say(b)a\\).
    * If the say function accepts two parameters, the LookAndSay object will correspond to the decay \\(a^b\\to say(b, a)\\).

    When no parameter is passed to the constructor, the LookAndSay
    object will correspond to standard base ten look and say sequences.

    
    ## Example Session: Default Constructor. 
    The following example uses the default (standard) look and say sequences.
    Note that the ratio of lengths are approaching Conway's constant.
    ```python 
    ls = LookAndSay()  
    ls.generate_sequence('55555', 50)
    sequence = ls.get_sequence()
    first_terms = sequence[:10]
    print('Sequence:', first_terms)
    print('Ratios of lengths:', ls.get_length_ratios())
    print('Just the last ratio:', ls.get_last_length_ratio())
    ```
    ### Output:

    ```sh
    Sequence: ['55555', '55', '25', '1215', '11121115', '31123115', '132112132115', '11131221121113122115', '311311222112311311222115', '1321132132211213211321322115']
    Ratios of lengths: [0.4, 1.0, 2.0, 2.0, 1.0, 1.5, 1.6666666666666667, 1.2, 1.1666666666666667, 1.5714285714285714, 1.1818181818181819, 1.1538461538461537, 1.4666666666666666, 1.2727272727272727, 1.25, 1.4, 1.3265306122448979, 1.2461538461538462, 1.3333333333333333, 1.3518518518518519, 1.226027397260274, 1.312849162011173, 1.3361702127659574, 1.2611464968152866, 1.3257575757575757, 1.318095238095238, 1.2919075144508672, 1.3053691275167785, 1.3161953727506426, 1.2936197916666667, 1.2989431303472572, 1.3142192948469587, 1.2951061320754718, 1.2997951286137037, 1.312784588441331, 1.2996264674493063, 1.3030178608088687, 1.3061288797857256, 1.3046441495778045, 1.300263510702233, 1.304700277323473, 1.3052921299324176, 1.299567840664732, 1.3057126333376172, 1.304461231821649, 1.3014789104353732, 1.3050192770385831, 1.304147670163319, 1.3026438489740129, 1.3036460274187538]
    Just the last ratio: 1.3036460274187538
    ```

    ## Example Sessions: One parameter say functions

    Here is an implementation of a Roman look and say:
    ```python
    def roman_say(num):
        assert num < 10, "This Roman can only count to 9."
        roman = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
        return roman[num]

    roman_ls = LookAndSay(roman_say)

    roman_ls.generate_sequence('I', 10)
    print(roman_ls.get_sequence())

    roman_ls.generate_sequence('V', 10)
    print(roman_ls.get_sequence())
    ```
    ### Output:

    ```sh
    ['I', 'II', 'III', 'IIII', 'IVI', 'IIIVII', 'IIIIIVIII', 'VIIVIIII', 'IVIIIIVIVI', 'IIIVIVIIVIIIVII', 'IIIIIVIIIVIIIIVIIIIIVIII']
    ['V', 'IV', 'IIIV', 'IIIIIV', 'VIIV', 'IVIIIIV', 'IIIVIVIIV', 'IIIIIVIIIVIIIIV', 'VIIVIIIIIVIVIIV', 'IVIIIIVVIIVIIIVIIIIV', 'IIIVIVIIIVIIIIVIIIIIVIVIIV']
    ```
    Here is a standard binary look and say:
    ```python
    def binary_say(num):
        return "{0:b}".format(num)

    binary_ls = LookAndSay(binary_say)

    binary_ls.generate_sequence('0', 9)
    print(binary_ls.get_sequence())

    binary_ls.generate_sequence('1', 9)
    print(binary_ls.get_sequence())
    ```
    ### Output:

    ```sh
    ['0', '10', '1110', '11110', '100110', '1110010110', '111100111010110', '100110011110111010110', '1110010110010011011110111010110', '1111001110101100111001011010011011110111010110']
    ['1', '11', '101', '111011', '11110101', '100110111011', '111001011011110101', '111100111010110100110111011', '100110011110111010110111001011011110101', '1110010110010011011110111010110111100111010110100110111011']
    ```
    ## Example Sessions: Two parameter say functions

    Here is a *look-and-say-again* from the paper *Stuttering Conway Sequences Are Still Conway Sequences* by Brier et al.
    ```python
    def say_again(char_count, char):
        return 2 * str(char_count) + 2 * char

    look_and_say_again = LookAndSay(say_again)

    look_and_say_again.generate_sequence('1', 10)
    print(look_and_say_again.get_sequence())

    look_and_say_again.generate_sequence('2', 10)
    print(look_and_say_again.get_sequence())
    ```
    ### Output:

    ```sh
    ['1', '1111', '4411', '22442211', '2222224422222211', '6622224466222211', '226644222244226644222211', '2222226622444422224422222266224444222211', '662222662222444444222244662222662222444444222211', '22664422226644226644442222442266442222664422664444222211', '2222226622444422226622442222226644444422224422222266224444222266224422222266444444222211']
    ['2', '1122', '22112222', '222222114422', '6622221122442222', '226644222211222222444422', '22222266224444222211662244442222', '6622226622224444442222112266222244444422', '226644222266442266444422221122222266442266442222', '222222662244442222662244222222664444442222116622226622442222226622444422', '66222266222244444422226622222244662222666644442222112266442222662222224466222266222244442222']
    ```
    Here is Morrill's *Look Knave*.
    ```python
    def knave_say(bit_count, bit):
        flip = {'0':'1', '1':'0'}
        return "{0:b}".format(bit_count) + flip[bit]

    look_knave = LookAndSay(knave_say)

    look_knave.generate_sequence('0', 12)
    print(look_knave.get_sequence())

    look_knave.generate_sequence('1', 12)
    print(look_knave.get_sequence())
    ```
    ### Output:

    ```sh
    ['0', '11', '100', '10101', '1011101110', '10111101111011', '1011100011100011100', '1011110111110111110101', '1011100011101011101011101110', '10111101111101110111101110111101111011', '10111000111010111101110001111011100011100011100', '1011110111110111011100011110111100011110111110111110101', '1011100011101011110111101111000111000111100011101011101011101110']
    ['1', '10', '1011', '1011100', '1011110101', '1011100011101110', '10111101111101111011', '1011100011101011100011100', '1011110111110111011110111110101', '101110001110101111011100011101011101110', '10111101111101110111000111101111101110111101111011', '10111000111010111101111011110001110101111011100011100011100', '10111101111101110111000111000111000111110111011100011110111110111110101']
    ```
    """
    def __init__(self, say = None):
        super(LookAndSay, self).__init__()
        self._is_Conway = False
        if say == None:
            say = (lambda n : str(n))
            self._is_Conway = True
        self.say = say
        self.sequence = []

    def _chunk_op(self, char_count, char):
        """
        Conversion of the say function to a two parameter function 
        if the say function takes only one parameter; 
        just a copy of the say function otherwise.
        """
        try:
            return self.say(char_count, char)
        except:
            return self.say(char_count) + char

    def get_sequence(self):
        """Returns the look and say sequence as a list of strings"""
        return self.sequence

    def say_what_you_see(self, string):
        """
        The fundamental look and say operation that generates each 
        term of a look and say sequence from its predecessor. For example, 
        using the standard (default) LookAndSay object, 
        ``say_what_you_see('1112222333')`` returns ``'314233'``.
        """
        if not string: return None # handles empty string, which is falsy
        letter = string[0]
        result = ''
        count = 0
        for ch in string:
            if ch == letter: 
                count += 1
            else:
                result += self._chunk_op(count, letter)
                count = 1
                letter = ch 
        result += self._chunk_op(count, letter)
        return result
     
    def generate_sequence(self, seed, num_iterations):
        """
        Generates the look and say sequence. The parameter ``seed`` is 
        the initial term in the sequence, and ``num_iterations`` is the 
        number of terms generated.
        """
        if not seed: return None # handles empty seed, which is falsy
        result = [seed]
        for _ in range(num_iterations):
            result.append(self.say_what_you_see(result[-1]))
        self.sequence = result

    def get_length_ratios(self):
        """
        Returns a list of the ratios of lengths of 
        successive terms in the look and say sequence.
        """
        num_iterations = len(self.sequence)
        assert num_iterations > 1, 'Look and say sequence does not have enough terms to compute the ratio of lengths.'
        return [len(self.sequence[i+1]) / len(self.sequence[i]) for i in range(num_iterations - 1)]

    def get_last_length_ratio(self):
        """
        Returns the ratio of the lengths of the last 
        two terms of the look and say sequence
        """
        return self.get_length_ratios()[-1]


########### CHEMISTRY #####################

class Chemistry():
    """
    A class responsible for generating all the persistent elements 
    appearing in look and say sequences, along with 
    the chemical properties of those elements.

    Parameters in the constructor are a LookAndSay object ``las`` and
    a splitting function ``split``. The user is responsible
    for verifying that the provided splitting function is valid for the given
    LookAndSay object. The default splitting function corresponds to 
    Conway's original Splitting Theorem.

    """
    def __init__(self, las, split = split_Conway, elements = None):
        super(Chemistry, self).__init__()
        self.las = las
        self.split = split
        if elements == None:
            elements = []
        self.elements = elements

    def get_elements(self):
        """Returns the elements as a list."""
        return self.elements

    def clear_elements(self):
        """Resets the list of elements back to the empty list"""
        self.elements = []

    def _split_to_elements(self, string): 
        return [Element(chunk, self.las) for chunk in self.split(string)]

    def _generate_all_elements(self, strings):
        for string in strings:
            for elt in self._split_to_elements(string):
                if elt not in self.elements:
                    # add elt to the chemistry:
                    self.elements.append(elt)
                    # recursively set the decay for elt:
                    decay_elts = self._split_to_elements(self.las.say_what_you_see(elt.get_string()))
                    self._generate_all_elements(map(lambda e : e.get_string(), decay_elts))
                    elt._set_decay(decay_elts)
        # clean up decay for all elements:
        for elt in self.elements:
            dec = []
            for d in elt.get_decay():
                dec += [e for e in self.elements if e == d]
            elt._set_decay(dec)

    def _remove_extinct_elements(self): 
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
        """
        Collects all the persistent elements from all the look and
        say sequences generated by the given seeds. The parameter ``seeds``
        should be a nonempty list of strings. By default, this method will 
        clear any elements in the chemistry that exist before this method is called
        prior to collecting from the given seeds. Use ``reset = False`` 
        to keep the old elements. 
        """
        assert type(seeds) == type(['0']), "The parameter seeds in generate_elements should be a list of strings."
        if reset:
            self.clear_elements()
        strings = [self.las.say_what_you_see(seed) for seed in seeds] #only look at 2-day-old strings
        self._generate_all_elements(strings)
        self._remove_extinct_elements()
        self.order_elements('string')
        self._name_elements()

    def _name_elements(self):
        if self.las._is_Conway:
            for e in self.get_elements():
                e.set_name(_conway_name(e))
            self.elements = sorted(self.get_elements(), key = _conway_number)
        else:
            for i, e in enumerate(self.get_elements()):
                e.set_name('E' + str(i + 1))

    def get_decay_matrix(self):
        """
        Returns the decay matrix as a nested list of integers 
        (i.e. a list of the rows).
        The order of the columns and rows correspond to the order
        in the list of elements.
        """
        mat = []
        e = self.elements
        for i in range(len(e)):
            row = []
            for j in range(len(e)):
                row.append(e[j].get_decay().count(e[i]))
            mat.append(row)
        return mat

    def get_max_eigenvalue(self):
        """
        Returns the maximal real eigenvalue of the decay matrix.
        This method assumes the existence of a real eigenvalue which
        is larger than (the absolute value) of every other eigenvalue.
        This assumption is usually guaranteed by the Perron-Frobenius Theorem.
        """
        eigenstuff = numpy.linalg.eig(numpy.array(self.get_decay_matrix()))
        eigenvalues = eigenstuff[0]
        return max(eigenvalues).real

    def get_char_poly(self, factor = True):
        """
        Returns the characteristic polynomial of the decay matrix using sympy.
        By default the returned polynomial will be factored. 
        Use ``factor = False`` to get the expanded (i.e. unfactored) polynomial. 
        """
        chi = sympy.Matrix(self.get_decay_matrix()).charpoly()
        if factor:
            return sympy.factor(chi.as_expr())
        else:
            return chi.as_expr()

    def _get_abundances(self, dec_places = 8):
        """
        Returns a list of relative abundances of each element.
        Note the abundances are given as percentages, 
        so they will differ from Conway's abundances by a factor of \\(10^4\\).
        The order of the list corresponds to the order of the list of elements.
        """
        eigenstuff = numpy.linalg.eig(numpy.array(self.get_decay_matrix()))
        eigenvalues = eigenstuff[0]
        eigenvectors = eigenstuff[1]
        index = numpy.where(eigenvalues == max(eigenvalues))
        limiting_eigenvector_nparray = eigenvectors[:,index].real
        # The next two lines are converting the numpy array to a list
        limiting_eigenvector = limiting_eigenvector_nparray.tolist()
        limiting_eigenvector = [elt[0][0] for elt in limiting_eigenvector]
        abundance = [round(100 * num / sum(limiting_eigenvector), dec_places) for num in limiting_eigenvector]
        return abundance

    def periodic_table(self, dec_places = 8):
        """
        Creates a periodic table including each element's name, string, relative abundance, and decay.
        Returns the periodic table as a nested dictionary.
        """
        return {e.get_name() : {'string' : e.get_string(), 
                                'abundance' : self._get_abundances(dec_places)[i],
                                'decay' : e.get_decay()}
                                for i, e in enumerate(self.get_elements())}

    def print_periodic_table(self, dec_places = 8):
        """
        Prints the periodic table. Note the abundances are given as percentages, 
        so they will differ from Conway's abundances by a factor of \\(10^4\\).
        The parameter ``dec_places`` refers to the accuracy of the abundances.
        """
        pt = self.periodic_table(dec_places)
        elt_width = 2 + max(len('element'), max([len(e.get_name()) for e in self.get_elements()]))
        str_width = 2 + max(len('string'), max([len(e.get_string()) for e in self.get_elements()]))
        ab_width  = 2 + max(len('abundance'), max([len(str(prop['abundance'])) for elt, prop in pt.items()]))
        print("{:<{elt_width}} {:<{str_width}} {:<{ab_width}} {}".format('element', 'string', 'abundance', 'decay', elt_width=elt_width, str_width=str_width, ab_width=ab_width))
        for elt, prop in pt.items():
            print("{:<{elt_width}} {:<{str_width}} {:<{ab_width}} {}".format(elt, prop['string'], prop['abundance'], str(prop['decay']), elt_width=elt_width, str_width=str_width, ab_width=ab_width))

    def order_elements(self, order_on, key = None, reverse = False, rename = True):
        """
        Reorders the list of elements depending on the parameter ``order_on`` as follows:

        * ``order_on='abundance'``: Orders elements from highest abundance to lowest.
        * ``order_on='string'``: Orders elements according to the lexicographic order of their strings.
        * ``order_on='string length'``: Orders elements according to the lengths of their strings from shortest to longest.
        * ``order_on='name'``: Orders elements alphabetically according to their names.
        * ``order_on='key'``: Orders elements according to the function specified by the parameter ``key``.

        Note: By default this method will automatically rename the elements according to their new order.
        This will not happen if the elements are named via Conway or if the parameter ``rename = False`` is passed.
        """
        assert order_on in ['abundance', 'name', 'string', 'string length', 'key'], "Invalid parameter passed to order_elements. Valid parameter are 'abundance', 'name', 'string', 'string length', and 'key'."
        pt = self.periodic_table()
        sorted_key = {
            'abundance': lambda e : pt[e.get_name()]['abundance'],
            'name': lambda e : pt[e.get_name()]['name'],
            'string': lambda e : e.get_string(),
            'string length': lambda e : len(e.get_string()),
            'key': key
        }
        self.elements = sorted(self.get_elements(), key = sorted_key[order_on])
        if order_on == 'abundance':
            self.elements.reverse()
        if reverse:
            self.elements.reverse()
        if not self.las._is_Conway and rename:
            self._name_elements()

class BinaryChemistry(Chemistry):
    """
    A chemistry for binary look and say sequences that split as 1.0 
    (i.e. whenever a 1 is left of a 0). This chemistry is valid whenever
    the say-what-you-see operation maps 
    \\(a^b\\) to \\([b]a\\) where \\([b]\\) is a binary
    string that always starts with a 1. For example, this chemistry is 
    valid for standard base two binary look and say sequences. 

    ## Example Session: Standard Binary
    ```python
    def binary_say(num):
        return "{0:b}".format(num)

    binary_ls = LookAndSay(binary_say)
    binary_chem = BinaryChemistry(binary_ls)
    binary_chem.generate_elements(['1'])
    binary_chem.order_elements('abundance')
    binary_chem.print_periodic_table()
    print(binary_chem.get_char_poly())
    print(binary_chem.get_max_eigenvalue())
    ```

    ### Output:

    ```sh
    element   string   abundance     decay
    E1        110      21.6756572    [E2, E1]
    E2        10       21.6756572    [E3]
    E3        1110     14.78990357   [E4]
    E4        11110    10.09156242   [E6, E1]
    E5        1100     10.09156242   [E2, E5]
    E6        100      10.09156242   [E7]
    E7        11100    6.88575362    [E8]
    E8        111100   4.69834115    [E6, E5]
    E9        11       0.0           [E2, E10]
    E10       1        0.0           [E9]
    lambda**4*(lambda - 1)**2*(lambda + 1)*(lambda**3 - lambda**2 - 1)
    1.4655712318767664
    ```
    """
    def __init__(self, las, elements = None):
        sf = SplittingFactory()
        sf.split_after('0')
        binary_split = sf.get_split()
        super().__init__(las, binary_split, elements)

########### ELEMENT #######################

class Element():
    """
    An element consists of a string (usually a chunk of digits) and 
    a name. For example, in Conway's chemistry there is an element
    named H (short for Hydrogen) consisting of the string '22'. 
    Each element decays into a list of other elements. 
    """
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

    def _set_decay(self, elements):
        self.decay = elements

    def get_decay(self):
        """Returns the decay of the element as a list of elements."""
        return self.decay

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_string(self):
        return self.string

########### SPLITTING FACTORY #####################

class SplittingFactory():
    """
    A class to help create a split function. The splitting factory
    can produce a split function via any combination of the following:

    * Specifying specific strings L and R such that LR splits as L.R.
    * Specifying specific characters or strings to always split before or after.
    * Specifying some conditions on L and R that imply LR splits as L.R.
    """
    def __init__(self):
        self._splitting_pairs = []
        self._chunks_before_split = []
        self._chunks_after_split = []
        self._split_conditions = []

    def get_split(self):
        """Return the split function"""
        return lambda string : self._split(string)

    def _split(self, string):
        chunks = []
        start = 0
        for i in range(1, len(string)):
            if self._is_split(string[start:i], string[i:]):
                chunks.append(string[start:i])
                start = i
        chunks.append(string[start:])
        return chunks

    def _is_split(self, L, R):
        if L == '' or R == '':
            return True
        if L[-1] == R[0]:
            return False
        for l in self._chunks_before_split:
            if len(l) <= len(L) and l == L[-len(l):]:
                return True
        for r in self._chunks_after_split:
            if len(r) <= len(R) and r == R[:len(r)]:
                return True
        for l, r in self._splitting_pairs:
            if len(l) <= len(L) and len(r) <= len(R) and l == L[-len(l):] and r == R[:len(r)]:
                return True
        for condition in self._split_conditions:
            if condition(L, R):
                return True
        return False

    def declare_splitting_pairs(self, *args):
        """
        Specify pairs of chunks in the form (L, R) 
        such that LR always splits as L.R
        """
        for arg in args:
            self._splitting_pairs.append(arg)

    def split_after(self, *args):
        """Specify chunks L such that LR splits for every possible R"""
        for arg in args:
            self._chunks_before_split.append(arg)

    def split_before(self, *args):
        """Specify chunks R such that LR splits for every possible L"""
        for arg in args:
            self._chunks_after_split.append(arg)

    def add_splitting_condition(self, *args):
        """
        Specify functions ``is_split`` such that 
        ``is_split(L,R)`` returns True for some splittable pairs 
        (L,R). 
        """
        for arg in args:
            self._split_conditions.append(arg)

# sf = SplittingFactory()
# sf.split_after('0', 'X')
# print(sf._chunks_before_split)
# split = sf.get_split()
# print(split('1234024350034X3450X34500X2345XX003425'))

# ls = LookAndSay()
# chem = Chemistry(ls)
# chem.generate_elements(['1', '4', '5', 'X'])
# chem.print_periodic_table()

def binary_say(num):
        return "{0:b}".format(num)

binary_ls = LookAndSay(binary_say)
binary_chem = BinaryChemistry(binary_ls)
binary_chem.generate_elements(['1'])
binary_chem.order_elements('abundance')
binary_chem.print_periodic_table()
print(binary_chem.get_char_poly())
print(binary_chem.get_max_eigenvalue())     
