"""
.. include:: ./docs/SUMMARY.md

.. include:: ./docs/EXAMPLESESSIONS.md

.. include:: ./docs/PROJECTS.md

.. include:: ./docs/ACKNOWLEDGMENTS.md
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
    >>> from look_and_say import split_Conway
    >>> string = '1211132213'
    >>> chunks = split_Conway(string)
    >>> print(chunks)
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
        return 92 * int(string[:9]) + ord(string[-1])

################# LOOK AND SAY #################################

class LookAndSay():
    """
    A class responsible for the fundamental say-what-you-see operation
    that generates a look and say sequence. The parameter ``say`` in the
    constructor is a function that determines the decay of a chunk of the form
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

    Here is a *look-and-say-again* from the paper [*Stuttering Conway Sequences Are Still Conway Sequences* by Brier et al](https://arxiv.org/abs/2006.06837).
    The say function for this example corresponds to the decay \\(a^b\\to bbaa\\).
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
    Here is [Morrill's *Look Knave*](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/abs/look-knave/BFC51822DED97095C96ABD2255AEDC2A):
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

    ## Example Session: Conway's Constant and his 92 Common Elements

    ```python
    ls = LookAndSay()
    chem = Chemistry(ls)
    chem.generate_elements('1')
    chem.print_periodic_table() 

    print(chem.get_char_poly())
    print(chem.get_max_eigenvalue())   
    ```
    ### Output:

    ```sh
    element   string                                       abundance   decay
    H         22                                           9.1790383   [H]
    He        13112221133211322112211213322112             0.3237297   [Hf, Pa, H, Ca, Li]
    Li        312211322212221121123222112                  0.4220067   [He]
    Be        111312211312113221133211322112211213322112   0.2263886   [Ge, Ca, Li]
    B         1321132122211322212221121123222112           0.295115    [Be]
    C         3113112211322112211213322112                 0.3847053   [B]
    N         111312212221121123222112                     0.501493    [C]
    O         132112211213322112                           0.6537349   [N]
    F         31121123222112                               0.852194    [O]
    Ne        111213322112                                 1.1109007   [F]
    Na        123222112                                    1.4481449   [Ne]
    Mg        3113322112                                   1.8850441   [Pm, Na]
    Al        1113222112                                   2.4573007   [Mg]
    Si        1322112                                      3.2032813   [Al]
    P         311311222112                                 1.4895887   [Ho, Si]
    S         1113122112                                   1.9417939   [P]
    Cl        132112                                       2.5312784   [S]
    Ar        3112                                         3.299717    [Cl]
    K         1112                                         4.3014361   [Ar]
    Ca        12                                           5.6072543   [K]
    Sc        3113112221133112                             0.9302097   [Ho, Pa, H, Ca, Co]
    Ti        11131221131112                               1.2126003   [Sc]
    V         13211312                                     1.5807182   [Ti]
    Cr        31132                                        2.0605883   [V]
    Mn        111311222112                                 2.686136    [Cr, Si]
    Fe        13122112                                     3.5015859   [Mn]
    Co        32112                                        4.5645877   [Fe]
    Ni        11133112                                     1.3871124   [Zn, Co]
    Cu        131112                                       1.8082082   [Ni]
    Zn        312                                          2.3571391   [Cu]
    Ga        13221133122211332                            0.1447891   [Eu, Ca, Ac, H, Ca, Zn]
    Ge        31131122211311122113222                      0.1887437   [Ho, Ga]
    As        11131221131211322113322112                   0.0027246   [Ge, Na]
    Se        13211321222113222112                         0.0035518   [As]
    Br        3113112211322112                             0.00463     [Se]
    Kr        11131221222112                               0.0060355   [Br]
    Rb        1321122112                                   0.0078678   [Kr]
    Sr        3112112                                      0.0102563   [Rb]
    Y         1112133                                      0.0133699   [Sr, U]
    Zr        12322211331222113112211                      0.0174286   [Y, H, Ca, Tc]
    Nb        1113122113322113111221131221                 0.0227196   [Er, Zr]
    Mo        13211322211312113211                         0.0296167   [Nb]
    Tc        311322113212221                              0.0386077   [Mo]
    Ru        132211331222113112211                        0.0328995   [Eu, Ca, Tc]
    Rh        311311222113111221131221                     0.042887    [Ho, Ru]
    Pd        111312211312113211                           0.0559065   [Rh]
    Ag        132113212221                                 0.0728785   [Pd]
    Cd        3113112211                                   0.0950027   [Ag]
    In        11131221                                     0.1238434   [Cd]
    Sn        13211                                        0.1614395   [In]
    Sb        3112221                                      0.2104488   [Pm, Sn]
    Te        1322113312211                                0.2743363   [Eu, Ca, Sb]
    I         311311222113111221                           0.3576186   [Ho, Te]
    Xe        11131221131211                               0.4661834   [I]
    Cs        13211321                                     0.6077061   [Xe]
    Ba        311311                                       0.7921919   [Cs]
    La        11131                                        1.0326833   [Ba]
    Ce        1321133112                                   1.3461825   [La, H, Ca, Co]
    Pr        31131112                                     1.7548529   [Ce]
    Nd        111312                                       2.2875864   [Pr]
    Pm        132                                          2.9820456   [Nd]
    Sm        311332                                       1.5408115   [Pm, Ca, Zn]
    Eu        1113222                                      2.0085669   [Sm]
    Gd        13221133112                                  2.1662973   [Eu, Ca, Co]
    Tb        3113112221131112                             2.8239359   [Ho, Gd]
    Dy        111312211312                                 3.6812186   [Tb]
    Ho        1321132                                      4.7987529   [Dy]
    Er        311311222                                    0.1098596   [Ho, Pm]
    Tm        11131221133112                               0.1204908   [Er, Ca, Co]
    Yb        1321131112                                   0.1570691   [Tm]
    Lu        311312                                       0.2047517   [Yb]
    Hf        11132                                        0.2669097   [Lu]
    Ta        13112221133211322112211213322113             0.0242077   [Hf, Pa, H, Ca, W]
    W         312211322212221121123222113                  0.0315567   [Ta]
    Re        111312211312113221133211322112211213322113   0.0169288   [Ge, Ca, W]
    Os        1321132122211322212221121123222113           0.022068    [Re]
    Ir        3113112211322112211213322113                 0.0287673   [Os]
    Pt        111312212221121123222113                     0.0375005   [Ir]
    Au        132112211213322113                           0.0488847   [Pt]
    Hg        31121123222113                               0.063725    [Au]
    Tl        111213322113                                 0.0830705   [Hg]
    Pb        123222113                                    0.1082888   [Tl]
    Bi        3113322113                                   0.1411629   [Pm, Pb]
    Po        1113222113                                   0.1840167   [Bi]
    At        1322113                                      0.23988     [Po]
    Rn        311311222113                                 0.3127021   [Ho, At]
    Fr        1113122113                                   0.4076313   [Rn]
    Ra        132113                                       0.5313789   [Fr]
    Ac        3113                                         0.6926935   [Ra]
    Th        1113                                         0.7581905   [Ac]
    Pa        13                                           0.9883599   [Th]
    U         3                                            0.0102563   [Pa]
    lambda**18*(lambda - 1)**2*(lambda + 1)*(lambda**71 - lambda**69 - 2*lambda**68 - lambda**67 + 2*lambda**66 + 2*lambda**65 + lambda**64 - lambda**63 - lambda**62 - lambda**61 - lambda**60 - lambda**59 + 2*lambda**58 + 5*lambda**57 + 3*lambda**56 - 2*lambda**55 - 10*lambda**54 - 3*lambda**53 - 2*lambda**52 + 6*lambda**51 + 6*lambda**50 + lambda**49 + 9*lambda**48 - 3*lambda**47 - 7*lambda**46 - 8*lambda**45 - 8*lambda**44 + 10*lambda**43 + 6*lambda**42 + 8*lambda**41 - 5*lambda**40 - 12*lambda**39 + 7*lambda**38 - 7*lambda**37 + 7*lambda**36 + lambda**35 - 3*lambda**34 + 10*lambda**33 + lambda**32 - 6*lambda**31 - 2*lambda**30 - 10*lambda**29 - 3*lambda**28 + 2*lambda**27 + 9*lambda**26 - 3*lambda**25 + 14*lambda**24 - 8*lambda**23 - 7*lambda**21 + 9*lambda**20 + 3*lambda**19 - 4*lambda**18 - 10*lambda**17 - 7*lambda**16 + 12*lambda**15 + 7*lambda**14 + 2*lambda**13 - 12*lambda**12 - 4*lambda**11 - 2*lambda**10 + 5*lambda**9 + lambda**7 - 7*lambda**6 + 7*lambda**5 - 4*lambda**4 + 12*lambda**3 - 6*lambda**2 + 3*lambda - 6)
    1.3035772690342997
    ```

    ## Example Session: Conway's Chemistry with Transuranic Elements
    In the following example, the seeds used to generate elements 
    guarantee that a few transuranic elements will appear. Also, we print the 
    periodic table using Conway's convention that abundances are given in 
    atoms per million.

    ```python
    ls = LookAndSay()
    chem = Chemistry(ls)
    chem.generate_elements('11111', '78')
    chem.print_periodic_table(abundance_sum = 10**6) 
    ```

    ### Output:
    ```sh
    element   string                                       abundance       decay
    H         22                                           91790.383216    [H]
    He        13112221133211322112211213322112             3237.2968587    [Hf, Pa, H, Ca, Li]
    Li        312211322212221121123222112                  4220.0665982    [He]
    Be        111312211312113221133211322112211213322112   2263.8860324    [Ge, Ca, Li]
    B         1321132122211322212221121123222112           2951.1503716    [Be]
    C         3113112211322112211213322112                 3847.0525419    [B]
    N         111312212221121123222112                     5014.9302464    [C]
    O         132112211213322112                           6537.349075     [N]
    F         31121123222112                               8521.9396539    [O]
    Ne        111213322112                                 11109.0068209   [F]
    Na        123222112                                    14481.4487733   [Ne]
    Mg        3113322112                                   18850.4412275   [Pm, Na]
    Al        1113222112                                   24573.0066954   [Mg]
    Si        1322112                                      32032.81296     [Al]
    P         311311222112                                 14895.8866582   [Ho, Si]
    S         1113122112                                   19417.9392497   [P]
    Cl        132112                                       25312.7842174   [S]
    Ar        3112                                         32997.1701218   [Cl]
    K         1112                                         43014.3609132   [Ar]
    Ca        12                                           56072.5431285   [K]
    Sc        3113112221133112                             9302.0974443    [Ho, Pa, H, Ca, Co]
    Ti        11131221131112                               12126.0027828   [Sc]
    V         13211312                                     15807.1815919   [Ti]
    Cr        31132                                        20605.8826107   [V]
    Mn        111311222112                                 26861.3601797   [Cr, Si]
    Fe        13122112                                     35015.8585455   [Mn]
    Co        32112                                        45645.8772557   [Fe]
    Ni        11133112                                     13871.1241997   [Zn, Co]
    Cu        131112                                       18082.0822027   [Ni]
    Zn        312                                          23571.3913363   [Cu]
    Ga        13221133122211332                            1447.8905642    [Eu, Ca, Ac, H, Ca, Zn]
    Ge        31131122211311122113222                      1887.4372276    [Ho, Ga]
    As        11131221131211322113322112                   27.2462161      [Ge, Na]
    Se        13211321222113222112                         35.5175479      [As]
    Br        3113112211322112                             46.2998682      [Se]
    Kr        11131221222112                               60.3554557      [Br]
    Rb        1321122112                                   78.6780001      [Kr]
    Sr        3112112                                      102.5628525     [Rb]
    Y         1112133                                      133.6986032     [Sr, U]
    Zr        12322211331222113112211                      174.28646       [Y, H, Ca, Tc]
    Nb        1113122113322113111221131221                 227.1958675     [Er, Zr]
    Mo        13211322211312113211                         296.1673685     [Nb]
    Tc        311322113212221                              386.0770494     [Mo]
    Ru        132211331222113112211                        328.9948058     [Eu, Ca, Tc]
    Rh        311311222113111221131221                     428.8701504     [Ho, Ru]
    Pd        111312211312113211                           559.0653795     [Rh]
    Ag        132113212221                                 728.7849206     [Pd]
    Cd        3113112211                                   950.0274565     [Ag]
    In        11131221                                     1238.4341972    [Cd]
    Sn        13211                                        1614.3946687    [In]
    Sb        3112221                                      2104.4881933    [Pm, Sn]
    Te        1322113312211                                2743.3629717    [Eu, Ca, Sb]
    I         311311222113111221                           3576.1856107    [Ho, Te]
    Xe        11131221131211                               4661.8342719    [I]
    Cs        13211321                                     6077.0611889    [Xe]
    Ba        311311                                       7921.9188284    [Cs]
    La        11131                                        10326.8333118   [Ba]
    Ce        1321133112                                   13461.8251664   [La, H, Ca, Co]
    Pr        31131112                                     17548.5292866   [Ce]
    Nd        111312                                       22875.863883    [Pr]
    Pm        132                                          29820.4561674   [Nd]
    Sm        311332                                       15408.1151815   [Pm, Ca, Zn]
    Eu        1113222                                      20085.6687093   [Sm]
    Gd        13221133112                                  21662.9728211   [Eu, Ca, Co]
    Tb        3113112221131112                             28239.3589492   [Ho, Gd]
    Dy        111312211312                                 36812.1864183   [Tb]
    Ho        1321132                                      47987.5294384   [Dy]
    Er        311311222                                    1098.5955997    [Ho, Pm]
    Tm        11131221133112                               1204.9083841    [Er, Ca, Co]
    Yb        1321131112                                   1570.6911808    [Tm]
    Lu        311312                                       2047.51732      [Yb]
    Hf        11132                                        2669.0970363    [Lu]
    Ta        13112221133211322112211213322113             242.0773667     [Hf, Pa, H, Ca, W]
    W         312211322212221121123222113                  315.5665525     [Ta]
    Re        111312211312113221133211322112211213322113   169.2880181     [Ge, Ca, W]
    Os        1321132122211322212221121123222113           220.6800123     [Re]
    Ir        3113112211322112211213322113                 287.6734477     [Os]
    Pt        111312212221121123222113                     375.0045674     [Ir]
    Au        132112211213322113                           488.8474298     [Pt]
    Hg        31121123222113                               637.2503975     [Au]
    Tl        111213322113                                 830.7051329     [Hg]
    Pb        123222113                                    1082.8883286    [Tl]
    Bi        3113322113                                   1411.62861      [Pm, Pb]
    Po        1113222113                                   1840.1669683    [Bi]
    At        1322113                                      2398.7998311    [Po]
    Rn        311311222113                                 3127.0209328    [Ho, At]
    Fr        1113122113                                   4076.3134078    [Rn]
    Ra        132113                                       5313.7894999    [Fr]
    Ac        3113                                         6926.9352045    [Ra]
    Th        1113                                         7581.9047124    [Ac]
    Pa        13                                           9883.5986391    [Th]
    U         3                                            102.5628525     [Pa]
    Np5       13112221133211322112211213322115             0.0             [Hf, Pa, H, Ca, Pu5]
    Np7       13112221133211322112211213322117             0.0             [Hf, Pa, H, Ca, Pu7]
    Np8       13112221133211322112211213322118             0.0             [Hf, Pa, H, Ca, Pu8]
    Pu5       312211322212221121123222115                  0.0             [Np5]
    Pu7       312211322212221121123222117                  0.0             [Np7]
    Pu8       312211322212221121123222118                  0.0             [Np8]
    ```

    ## Example Session: Standard Ternary

    ```python
    # Define the say function:
    def ternary(num):
        if num < 3:
            return str(num)
        return ternary(num // 3) + str(num % 3)


    # Use the Split Function Factory to create a split function:
    sff = SplitFuncFactory()
    sff.declare_split_after('0')
    sff.declare_splitting_pairs(('2', '1110'), ('2', '10'))
    split = sff.get_split()

    # Instantiate the LookAndSay and Chemistry objects:
    ternary_ls = LookAndSay(ternary)
    ternary_chem = Chemistry(ternary_ls, split)

    # Generate elements and order them according to relative abundances:
    ternary_chem.generate_elements('0', '1', '2')
    ternary_chem.order_elements('abundance')

    # Print chemical properties:
    ternary_chem.print_periodic_table()
    print(ternary_chem.get_char_poly())
    print(ternary_chem.get_max_eigenvalue())
    ```

    ### Output:
    ```sh
    element   string     abundance    decay
    E1        10         18.5037375   [E4]
    E2        22110      13.9680582   [E5]
    E3        2110       13.9680582   [E6]
    E4        1110       13.9680582   [E1, E7]
    E5        222110     10.5441752   [E1, E2]
    E6        122110     10.5441752   [E8]
    E7        110        10.5441752   [E3]
    E8        11222110   7.9595623    [E3, E2]
    E9        222112     0.0          [E1, E10]
    E10       22112      0.0          [E9]
    E11       212221     0.0          [E16, E4, E13]
    E12       2112       0.0          [E14]
    E13       211        0.0          [E15]
    E14       122112     0.0          [E17]
    E15       1221       0.0          [E18]
    E16       12         0.0          [E20]
    E17       11222112   0.0          [E3, E10]
    E18       112211     0.0          [E11]
    E19       112        0.0          [E12]
    E20       1112       0.0          [E1, E19]
    lambda**6*(lambda - 1)**2*(lambda + 1)**2*(lambda**2 + 1)*(lambda**3 - lambda - 1)*(lambda**5 - lambda**3 + 1)
    1.3247179572447458
    ```

    
    ## Example Session: Balanced Ternary
    In this example we find the chemical properties of a [balanced ternary](https://en.wikipedia.org/wiki/Balanced_ternary)
    look and say sequence. 

    ```python
    # Define a (partial) say function to convert integers to balanced ternary:
    def bal_tern(num):
        assert num < 11, "bal_tern will only convert integers from 1 to 10."
        repn = {1:'1', 2:'1T', 3:'10', 4:'11', 5:'1TT', 6:'1T0', 7:'1T1', 8:'10T', 9:'100', 10:'101'}
        return repn[num]

    # Use the split function factory to generate an appropriate split function: 
    sff = SplitFuncFactory()
    sff.declare_split_after('0', 'T')
    split = sff.get_split()

    # Instantiate the look and say and chemistry objects:
    bal_tern_ls = LookAndSay(bal_tern)
    bal_tern_chem = Chemistry(bal_tern_ls, split)

    # Generate persistent elements from the seed '0', and order them according to their relative abundance:
    bal_tern_chem.generate_elements('0')
    bal_tern_chem.order_elements('abundance')

    # Print the chemical properties
    bal_tern_chem.print_periodic_table()
    print(bal_tern_chem.get_char_poly())
    print(bal_tern_chem.get_max_eigenvalue()) # golden!
    ```

    ### Output:
    ```sh
    element   string   abundance    decay
    E1        1T       23.6067977   [E3]
    E2        11T      23.6067977   [E1, E2]
    E3        111T     14.5898034   [E5, E2]
    E4        110      14.5898034   [E1, E4]
    E5        10       14.5898034   [E6]
    E6        1110     9.0169944    [E5, E4]
    lambda**3*(lambda - 1)*(lambda**2 - lambda - 1)
    1.6180339887498953
    ```

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
        """Resets the list of elements back to the empty list."""
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

    def _remove_intermittent_elements(self): 
        while True:
            common_elements = []
            for elt in self.elements:
                for d in elt.get_decay():
                    if d not in common_elements:
                        common_elements.append(d)
            if len(common_elements) < len(self.elements):
                self.elements = list(common_elements)
            else: 
                break

    def generate_elements(self, *seeds, reset = True):
        """
        Collects all the persistent elements from all the look and
        say sequences generated by the given seeds. The string(s) entered as the 
        parameter(s) will be used as the seed(s) for generating the elements. 
        By default, this method will clear any elements in the chemistry that exist 
        before this method is called (i.e. prior to collecting from the new seeds). 
        Use ``reset = False``  to keep the old elements. 
        """
        if reset:
            self.clear_elements()
        strings = [self.las.say_what_you_see(seed) for seed in seeds] #only look at 2-day-old strings
        self._generate_all_elements(strings)
        self._remove_intermittent_elements()
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
        In the standard case, this will give Conway's constant. 
        In general, this will give the growth rate of the look and say sequence. 
        This method assumes the existence of a real eigenvalue which
        is larger than (the absolute value) of every other eigenvalue.
        This assumption is usually guaranteed by the Perron-Frobenius Theorem.
        """
        assert len(self.elements) > 0, "The get_max_eigenvalue method requires a nonempty list of elements.\n\tTo fix: Use the generate_elements method prior to calling get_max_eigenvalue."
        eigenstuff = numpy.linalg.eig(numpy.array(self.get_decay_matrix()))
        eigenvalues = eigenstuff[0]
        return max(eigenvalues).real

    def get_char_poly(self, factor = True, latex = False):
        """
        Returns the characteristic polynomial of the decay matrix using sympy.
        By default the returned polynomial will be factored. 
        Use ``factor = False`` to get the expanded (i.e. unfactored) polynomial. 
        Use ``latex = True`` to return the polynomial formatted in latex.
        """
        chi = sympy.Matrix(self.get_decay_matrix()).charpoly()
        if factor:
            chi = sympy.factor(chi.as_expr())
        else:
            chi = chi.as_expr()
        if latex:
            return sympy.latex(chi)
        else:
            return chi

    def _get_abundances(self, dec_places = 7, abundance_sum = 100):
        """
        Returns a list of relative abundances of each element.
        By default the abundances are given as percentages, 
        so they will differ from Conway's abundances by a factor of \\(10^4\\).
        The abundances can be renormalized by setting the parameter ``abundance_sum``.
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
        abundance = [abs(round(abundance_sum * num / sum(limiting_eigenvector), dec_places)) for num in limiting_eigenvector]
        return abundance

    def get_periodic_table(self, dec_places = 7, abundance_sum = 100):
        """
        Creates a periodic table including each element's name, string, relative abundance, and decay.
        Returns the periodic table as a nested dictionary.

        ## Example Session:
        ```python
        ls = LookAndSay()
        chem = Chemistry(ls)
        chem.generate_elements('4')
        print(chem.get_periodic_table())
        ```

        ### Output:
        ```sh
        {'H': {'string': '22', 'abundance': 9.1790383, 'decay': [H]}, 'He': {'string': '13112221133211322112211213322112', 'abundance': 0.3237297, 'decay': [Hf, Pa, H, Ca, Li]}, 'Li': {'string': '312211322212221121123222112', 'abundance': 0.4220067, 'decay': [He]}, 'Be': {'string': '111312211312113221133211322112211213322112', 'abundance': 0.2263886, 'decay': [Ge, Ca, Li]}, 'B': {'string': '1321132122211322212221121123222112', 'abundance': 0.295115, 'decay': [Be]}, 'C': {'string': '3113112211322112211213322112', 'abundance': 0.3847053, 'decay': [B]}, 'N': {'string': '111312212221121123222112', 'abundance': 0.501493, 'decay': [C]}, 'O': {'string': '132112211213322112', 'abundance': 0.6537349, 'decay': [N]}, 'F': {'string': '31121123222112', 'abundance': 0.852194, 'decay': [O]}, 'Ne': {'string': '111213322112', 'abundance': 1.1109007, 'decay': [F]}, 'Na': {'string': '123222112', 'abundance': 1.4481449, 'decay': [Ne]}, 'Mg': {'string': '3113322112', 'abundance': 1.8850441, 'decay': [Pm, Na]}, 'Al': {'string': '1113222112', 'abundance': 2.4573007, 'decay': [Mg]}, 'Si': {'string': '1322112', 'abundance': 3.2032813, 'decay': [Al]}, 'P': {'string': '311311222112', 'abundance': 1.4895887, 'decay': [Ho, Si]}, 'S': {'string': '1113122112', 'abundance': 1.9417939, 'decay': [P]}, 'Cl': {'string': '132112', 'abundance': 2.5312784, 'decay': [S]}, 'Ar': {'string': '3112', 'abundance': 3.299717, 'decay': [Cl]}, 'K': {'string': '1112', 'abundance': 4.3014361, 'decay': [Ar]}, 'Ca': {'string': '12', 'abundance': 5.6072543, 'decay': [K]}, 'Sc': {'string': '3113112221133112', 'abundance': 0.9302097, 'decay': [Ho, Pa, H, Ca, Co]}, 'Ti': {'string': '11131221131112', 'abundance': 1.2126003, 'decay': [Sc]}, 'V': {'string': '13211312', 'abundance': 1.5807182, 'decay': [Ti]}, 'Cr': {'string': '31132', 'abundance': 2.0605883, 'decay': [V]}, 'Mn': {'string': '111311222112', 'abundance': 2.686136, 'decay': [Cr, Si]}, 'Fe': {'string': '13122112', 'abundance': 3.5015859, 'decay': [Mn]}, 'Co': {'string': '32112', 'abundance': 4.5645877, 'decay': [Fe]}, 'Ni': {'string': '11133112', 'abundance': 1.3871124, 'decay': [Zn, Co]}, 'Cu': {'string': '131112', 'abundance': 1.8082082, 'decay': [Ni]}, 'Zn': {'string': '312', 'abundance': 2.3571391, 'decay': [Cu]}, 'Ga': {'string': '13221133122211332', 'abundance': 0.1447891, 'decay': [Eu, Ca, Ac, H, Ca, Zn]}, 'Ge': {'string': '31131122211311122113222', 'abundance': 0.1887437, 'decay': [Ho, Ga]}, 'As': {'string': '11131221131211322113322112', 'abundance': 0.0027246, 'decay': [Ge, Na]}, 'Se': {'string': '13211321222113222112', 'abundance': 0.0035518, 'decay': [As]}, 'Br': {'string': '3113112211322112', 'abundance': 0.00463, 'decay': [Se]}, 'Kr': {'string': '11131221222112', 'abundance': 0.0060355, 'decay': [Br]}, 'Rb': {'string': '1321122112', 'abundance': 0.0078678, 'decay': [Kr]}, 'Sr': {'string': '3112112', 'abundance': 0.0102563, 'decay': [Rb]}, 'Y': {'string': '1112133', 'abundance': 0.0133699, 'decay': [Sr, U]}, 'Zr': {'string': '12322211331222113112211', 'abundance': 0.0174286, 'decay': [Y, H, Ca, Tc]}, 'Nb': {'string': '1113122113322113111221131221', 'abundance': 0.0227196, 'decay': [Er, Zr]}, 'Mo': {'string': '13211322211312113211', 'abundance': 0.0296167, 'decay': [Nb]}, 'Tc': {'string': '311322113212221', 'abundance': 0.0386077, 'decay': [Mo]}, 'Ru': {'string': '132211331222113112211', 'abundance': 0.0328995, 'decay': [Eu, Ca, Tc]}, 'Rh': {'string': '311311222113111221131221', 'abundance': 0.042887, 'decay': [Ho, Ru]}, 'Pd': {'string': '111312211312113211', 'abundance': 0.0559065, 'decay': [Rh]}, 'Ag': {'string': '132113212221', 'abundance': 0.0728785, 'decay': [Pd]}, 'Cd': {'string': '3113112211', 'abundance': 0.0950027, 'decay': [Ag]}, 'In': {'string': '11131221', 'abundance': 0.1238434, 'decay': [Cd]}, 'Sn': {'string': '13211', 'abundance': 0.1614395, 'decay': [In]}, 'Sb': {'string': '3112221', 'abundance': 0.2104488, 'decay': [Pm, Sn]}, 'Te': {'string': '1322113312211', 'abundance': 0.2743363, 'decay': [Eu, Ca, Sb]}, 'I': {'string': '311311222113111221', 'abundance': 0.3576186, 'decay': [Ho, Te]}, 'Xe': {'string': '11131221131211', 'abundance': 0.4661834, 'decay': [I]}, 'Cs': {'string': '13211321', 'abundance': 0.6077061, 'decay': [Xe]}, 'Ba': {'string': '311311', 'abundance': 0.7921919, 'decay': [Cs]}, 'La': {'string': '11131', 'abundance': 1.0326833, 'decay': [Ba]}, 'Ce': {'string': '1321133112', 'abundance': 1.3461825, 'decay': [La, H, Ca, Co]}, 'Pr': {'string': '31131112', 'abundance': 1.7548529, 'decay': [Ce]}, 'Nd': {'string': '111312', 'abundance': 2.2875864, 'decay': [Pr]}, 'Pm': {'string': '132', 'abundance': 2.9820456, 'decay': [Nd]}, 'Sm': {'string': '311332', 'abundance': 1.5408115, 'decay': [Pm, Ca, Zn]}, 'Eu': {'string': '1113222', 'abundance': 2.0085669, 'decay': [Sm]}, 'Gd': {'string': '13221133112', 'abundance': 2.1662973, 'decay': [Eu, Ca, Co]}, 'Tb': {'string': '3113112221131112', 'abundance': 2.8239359, 'decay': [Ho, Gd]}, 'Dy': {'string': '111312211312', 'abundance': 3.6812186, 'decay': [Tb]}, 'Ho': {'string': '1321132', 'abundance': 4.7987529, 'decay': [Dy]}, 'Er': {'string': '311311222', 'abundance': 0.1098596, 'decay': [Ho, Pm]}, 'Tm': {'string': '11131221133112', 'abundance': 0.1204908, 'decay': [Er, Ca, Co]}, 'Yb': {'string': '1321131112', 'abundance': 0.1570691, 'decay': [Tm]}, 'Lu': {'string': '311312', 'abundance': 0.2047517, 'decay': [Yb]}, 'Hf': {'string': '11132', 'abundance': 0.2669097, 'decay': [Lu]}, 'Ta': {'string': '13112221133211322112211213322113', 'abundance': 0.0242077, 'decay': [Hf, Pa, H, Ca, W]}, 'W': {'string': '312211322212221121123222113', 'abundance': 0.0315567, 'decay': [Ta]}, 'Re': {'string': '111312211312113221133211322112211213322113', 'abundance': 0.0169288, 'decay': [Ge, Ca, W]}, 'Os': {'string': '1321132122211322212221121123222113', 'abundance': 0.022068, 'decay': [Re]}, 'Ir': {'string': '3113112211322112211213322113', 'abundance': 0.0287673, 'decay': [Os]}, 'Pt': {'string': '111312212221121123222113', 'abundance': 0.0375005, 'decay': [Ir]}, 'Au': {'string': '132112211213322113', 'abundance': 0.0488847, 'decay': [Pt]}, 'Hg': {'string': '31121123222113', 'abundance': 0.063725, 'decay': [Au]}, 'Tl': {'string': '111213322113', 'abundance': 0.0830705, 'decay': [Hg]}, 'Pb': {'string': '123222113', 'abundance': 0.1082888, 'decay': [Tl]}, 'Bi': {'string': '3113322113', 'abundance': 0.1411629, 'decay': [Pm, Pb]}, 'Po': {'string': '1113222113', 'abundance': 0.1840167, 'decay': [Bi]}, 'At': {'string': '1322113', 'abundance': 0.23988, 'decay': [Po]}, 'Rn': {'string': '311311222113', 'abundance': 0.3127021, 'decay': [Ho, At]}, 'Fr': {'string': '1113122113', 'abundance': 0.4076313, 'decay': [Rn]}, 'Ra': {'string': '132113', 'abundance': 0.5313789, 'decay': [Fr]}, 'Ac': {'string': '3113', 'abundance': 0.6926935, 'decay': [Ra]}, 'Th': {'string': '1113', 'abundance': 0.7581905, 'decay': [Ac]}, 'Pa': {'string': '13', 'abundance': 0.9883599, 'decay': [Th]}, 'U': {'string': '3', 'abundance': 0.0102563, 'decay': [Pa]}, 'Pu4': {'string': '312211322212221121123222114', 'abundance': 0.0, 'decay': [Np4]}, 'Np4': {'string': '13112221133211322112211213322114', 'abundance': 0.0, 'decay': [Hf, Pa, H, Ca, Pu4]}}
        ```

        """
        return {e.get_name() : {'string' : e.get_string(), 
                                'abundance' : self._get_abundances(dec_places, abundance_sum)[i],
                                'decay' : e.get_decay()}
                                for i, e in enumerate(self.get_elements())}

    def print_periodic_table(self, dec_places = 7, abundance_sum = 100):
        """
        Prints the periodic table. Note the abundances are given as percentages, 
        so they will differ from Conway's abundances by a factor of \\(10^4\\).
        The parameter ``dec_places`` refers to the accuracy of the abundances.
        """
        pt = self.get_periodic_table(dec_places, abundance_sum)
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

        You can reverse the ordering above by passing the extra parameter ``reverse = True``.
        
        By default this method will automatically rename the elements according to their new order.
        This will not happen if the elements are named via Conway or if the parameter ``rename = False`` is passed.
        """
        assert order_on in ['abundance', 'name', 'string', 'string length', 'key'], "Invalid parameter passed to order_elements. Valid parameter are 'abundance', 'name', 'string', 'string length', and 'key'."
        pt = self.get_periodic_table()
        sorted_key = {
            'abundance': lambda e : pt[e.get_name()]['abundance'],
            'name': lambda e : e.get_name(),
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
    >>> def binary_say(num):
    ...     return "{0:b}".format(num)
    ... 
    >>> binary_ls = LookAndSay(binary_say)
    >>> binary_chem = BinaryChemistry(binary_ls)
    >>> binary_chem.generate_elements('1')
    >>> binary_chem.order_elements('abundance')
    >>> binary_chem.print_periodic_table()
    element   string   abundance    decay
    E1        110      21.6756572   [E2, E1]
    E2        10       21.6756572   [E3]
    E3        1110     14.7899036   [E4]
    E4        11110    10.0915624   [E6, E1]
    E5        1100     10.0915624   [E2, E5]
    E6        100      10.0915624   [E7]
    E7        11100    6.8857536    [E8]
    E8        111100   4.6983411    [E6, E5]
    E9        11       0.0          [E2, E10]
    E10       1        0.0          [E9]
    >>>
    >>> print(binary_chem.get_max_eigenvalue())
    1.4655712318767664

    ```

    ## Example Session: Twindragon Binary
    The following chemistry corresponds to the binary number system using 
    the complex base \\(-1+i.\\) This binary number system is known as *twindragon binary*.

    ```python
    >>> def twindragon_say(num):
    ...     assert num < 8, "This twindragon can only count to 7."
    ...     twindragon = {1:'1', 2:'1100', 3:'1101', 4:'111010000', 5:'111010001', 6:'111011100', 7:'111011101'}
    ...     return twindragon[num]
    ... 
    >>> twindragon_ls = LookAndSay(twindragon_say)
    >>> twindragon_chem = BinaryChemistry(twindragon_ls)
    >>> twindragon_chem.generate_elements('1')
    >>> twindragon_chem.print_periodic_table()
    element   string   abundance    decay
    E1        1        0.0          [E6]
    E2        10       6.746022     [E9]
    E3        1000     1.5358344    [E11, E2]
    E4        10000    2.8580442    [E12, E5]
    E5        100000   1.3339664    [E12, E3, E2]
    E6        11       0.0          [E8, E1]
    E7        110      28.3551578   [E8, E7]
    E8        1100     24.8181731   [E8, E10]
    E9        1110     14.6891551   [E7, E9]
    E10       111000   11.5836587   [E7, E11, E2]
    E11       11110    6.1234052    [E9, E4, E7]
    E12       111110   1.9565832    [E9, E3, E9]

    ```
    """
    def __init__(self, las, elements = None):
        sff = SplitFuncFactory()
        sff.declare_split_before('1')
        binary_split = sff.get_split()
        super().__init__(las, binary_split, elements)

########### ELEMENT #######################

class Element():
    """
    An element consists of a string (usually a chunk of digits) and 
    a name. For example, in Conway's chemistry there is an element
    named H (short for Hydrogen) consisting of the string '22'. 
    Each element decays into a list of other elements. 
    The only methods for this class are getters and a setter.
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
        return self.decay

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_string(self):
        return self.string

########### SPLIT FUNCTION FACTORY #####################

class SplitFuncFactory():
    """
    A class to help create a split function. The split function factory
    can produce a split function via any combination of the following:

    * Specifying specific chunks L and R such that LR splits as L.R.
    * Specifying specific characters or chunks to always split before or after.

    ## Example Session: Split after 0
    Many look and say sequences split after any run of 0's. 
    The following illustrates how the split function factory can 
    be used to create such a split function:
    ```python
    sff = SplitFuncFactory()
    sff.declare_split_after('0')
    split = sff.get_split()
    string = '1101230022200012301325023'
    print(split(string))
    ```

    ### Output:
    ```sh
    ['110', '12300', '222000', '1230', '13250', '23']
    ```


    ## Example Session: A combination of multiple methods.
    ```python
    sff = SplitFuncFactory()
    sff.declare_split_before('111')
    sff.declare_split_after('2', '30')
    sff.declare_splitting_pairs(('11', '333'))
    split = sff.get_split()
    string = '1234411154211333234530411113333344'
    print(split(string))
    ```

    ### Output:
    ```sh
    ['12', '344', '111542', '11', '3332', '34530', '4', '1111', '3333344']
    ```
    """
    def __init__(self):
        self._splitting_pairs = []
        self._chunks_before_split = []
        self._chunks_after_split = []
        self._split_conditions = []

    def get_split(self):
        """Returns the split function."""
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

    def declare_splitting_pairs(self, *pairs):
        """
        Specify pairs of chunks in the form (L, R) 
        such that LR always splits as L.R.

        ## Example Session:
        ```python
        sff = SplitFuncFactory()
        sff.declare_splitting_pairs(('311', '223'), ('0', '1'))
        split = sff.get_split()
        string = '12311223323112011200011110234234'
        print(split(string))
        ```

        ### Output:
        ```sh
        ['12311', '2233231120', '112000', '11110234234']
        ```
        """
        for pair in pairs:
            self._splitting_pairs.append(pair)

    def declare_split_after(self, *chunks):
        """
        Specify chunks L such that LR splits for every possible R (assuming the last character of L and the first character of R are distinct).
        
        ## Example Session:
        ```python
        sff = SplitFuncFactory()
        sff.declare_split_after('1', '20')
        split = sff.get_split()
        string = '12311223323112011200011110234234'
        print(split(string))
        ```

        ### Output:
        ```sh
        ['1', '2311', '22332311', '20', '11', '20001111', '0234234']
        ```
        """
        for chunk in chunks:
            self._chunks_before_split.append(chunk)

    def declare_split_before(self, *chunks):
        """Specify chunks R such that LR splits for every possible L (assuming the last character of L and the first character of R are distinct).

        ## Example Session:
        ```python
        sff = SplitFuncFactory()
        sff.declare_split_before('0', '31')
        split = sff.get_split()
        string = '12311223323112011200011110234234'
        print(split(string))
        ```

        ### Output:
        ```sh
        ['12', '31122332', '3112', '0112', '0001111', '0234234']
        ```
        """
        for chunk in chunks:
            self._chunks_after_split.append(chunk)

########### COSMOLOGY #####################

class Cosmology():
    '''
    A class for proving Conway's Cosmological Theorem.
    Currently this will only prove The Cosmological Theorem 
    for the standard base ten look and say sequences where every term
    consists of strings of some of the digits 1 through 9. The default
    digits considered are the crucial ones: 1, 2, and 3.  
    '''
    def __init__(self, digits = '123'):
        self.look_and_say = LookAndSay()
        self.split = split_Conway
        self.digits = digits
        self._compendium_sets = []
        self.common_strings = {elt for elt in _CONWAY_ELEMENTS}
        # add transuranic elements to the list of common strings:
        for digit in self.digits:
            if digit not in '123':
                self.common_strings.add('31221132221222112112322211' + digit)
                self.common_strings.add('1311222113321132211221121332211' + digit)

    def days_exotic(self, string):
        '''
        Returns the number of days until the string splits into a compound of common elements. 
        '''
        atoms = [atom for atom in self.split(string) if atom not in self.common_strings]
        days = 0
        while atoms != []:
            next_atoms = []
            for atom in atoms:
                new_atoms = self.split(self.look_and_say.say_what_you_see(atom))
                next_atoms += [a for a in new_atoms if a not in self.common_strings]
            atoms = next_atoms
            days += 1
        return days

    def proof(self, day = 9):
        '''
        Uses a backtracking algorithm to prove Conway's Cosmological Theorem. If we pass the parameter
        ``day = N`` the algorithm searches for all strings that might appear as chunks of an N-day
        old element. The search starts with strings of length 1 (i.e. the digits) and then 
        searches for strings of length 2, then length 3, etc. For each string found in the search, 
        the algorithm repeatedly applies the say-what-you-see operation until the result is a 
        compound of common elements. The algorithm terminates when for some positive integer L, 
        there are no strings of length L that can appear as chunks of an N-day old element, and 
        all strings of length less than L which might appear as a chunk of an N-day old element 
        are shown to eventually decay into a compound of common elements.

        Running the program prints a few details about the search. In particular, an upper bound
        for the age of an exotic (i.e. not common) element is displayed.  

        The default parameter is ``day = 9``, which results in a proof of the Cosmological Theorem
        that gives an upper bound of 27 for the age of an exotic element. 

        The proof is essentially the same as that of Zeilberger. 
        The implementation is similar to that of Litherland.
        '''
        chunks = self.digits # start with length 1 chunks
        max_days_exotic = 0

        print(f'To prove the Cosmological Theorem we search for all strings\nwhich could appear as chunks of {day} day old elements.\nSearching...')
        length = 0
        while True:
            length += 1
            compendium = []
            #Gather all chunks that have a grandparent to the compendium
            for chunk in chunks:
                if self._has_grandparent(chunk, day):
                    compendium.append(chunk)

            if compendium == []:
                print(f'There are no strings of length {length} that can appear as chunks\nof {day} day old elements. All strings of length less than {length}\nthat could appear after {day} days decay into compounds of common\nelements after an additional {max_days_exotic-day} days. This gives an upper\nbound of {max_days_exotic} days for the age of an exotic element.\nQ.E.D.')
                return max_days_exotic

            self._compendium_sets.append(set(compendium))

            #Compute an upper bound on the maximum longevity of an exotic element:
            for chunk in compendium:
                lifespan = day + self.days_exotic(chunk)
                if lifespan > max_days_exotic:
                    max_days_exotic = lifespan

            chunks = []
            #For each found above, add all possible digits to the left and check if splits
            for digit in self.digits:
                chunks += [digit+chunk for chunk in compendium if len(self.split(digit+chunk)) == 1]

    def _parents(self, kid):
        '''
        We call a string a *parent* of the kid if applying the say-what-you-see operation
        results in a string which contains the kid as a substring. This function returns
        a list of all the minimal parents of kid (here minimal means that every parent of
        the kid will contain one of the elements of the list as a substring).
        '''
        parents = []
        if self._is_day_one_even(kid):
            parents += self._even_parents(kid)
        if self._is_day_one_odd(kid):
            parents += self._odd_parents(kid)
        return parents

    def _is_day_one_odd(self, string):
        if len(string) == 1:
            return False
        if len(string) % 2 == 0:
            i = 0
        else:
            i = 1
        while i < len(string) - 2:
            if string[i] == string[i+2]:
                return False
            i += 2
        return True

    def _is_day_one_even(self, string):
        if len(string) == 1:
            return True
        if len(string) % 2 == 0:
            i = 1
        else:
            i = 0
        while i < len(string) - 2:
            if string[i] == string[i+2]:
                return False
            i += 2
        return True

    def _even_parents(self, string):
        new_string = ''
        if len(string) % 2 == 0:
            start = 0
        else:
            start = 1
            new_string += string[0]
        while start < len(string) - 1:
            new_string += int(string[start]) * string[start+1]
            start += 2
        return [new_string]

    def _odd_parents(self, string):
        new_string = ''
        if len(string) % 2 == 0:
            start = 1
            new_string += string[0]
        else:
            start = 0
        while start < len(string) - 2:
            new_string += int(string[start]) * string[start+1]
            start += 2
        return [new_string + int(string[-1]) * digit for digit in self.digits if digit != string[-2]]


    def _has_grandparent(self, kid, day):
        '''
        Returns True if the string kid *might* be contained in the result of applying
        the say-what-you-see operation day-times to some string. Note that this method
        will only return False when kid cannot be part of a day-old descendant of 
        any string,
        but may return True even if kid is not contained in any day-old descendant.
        '''
        # To speed things up, we first check the compendium sets:
        # if the kid has a parent who is already in a compendium, we know it's parent
        # has (possibly) a day-old ancestor, so certainly the kid also (possibly) has one.
        for parent in self._parents(kid):
            if len(parent) < len(self._compendium_sets) and parent in self._compendium_sets[len(parent)]:
                return True

        # Now apply the parents function day-times and see what we get:
        ancestors = [kid]
        for _ in range(day):
            next_ancestors = []
            for a in ancestors:
                next_ancestors += self._parents(a)
            ancestors = next_ancestors

        return len(ancestors) != 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()

