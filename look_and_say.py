"""
.. include:: ./docs/SUMMARY.md

.. include:: ./docs/EXAMPLESESSIONS.md

.. include:: ./docs/MAINDOCS.md

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
    For example, split_Conway('1211132213') returns ['12', '1113', '22', '13'].
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
            return True # pragma: no cover
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
    if string == '':
        return 0
    elif string in _CONWAY_ELEMENTS:
        return _CONWAY_ELEMENTS[string]['number']
    else: # Handling transuranic elements
        return 92 * int(string[:9]) + ord(string[-1])

################# LOOK AND SAY #################################

class LookAndSay():
    """
    A class responsible for the fundamental say-what-you-see operation
    that generates a look and say sequence. The parameter ``say`` in the
    constructor is a function that determines the decay of a chunk of the form
    $d^n$. The say function can have one or two parameters:

    * If the say function accepts one parameter, the LookAndSay object will correspond to the decay $d^n\\to say(n)d$.
    * If the say function accepts two parameters, the LookAndSay object will correspond to the decay $d^n\\to say(n, d)$.

    When no parameter is passed to the constructor, the LookAndSay
    object will correspond to standard decimal look and say sequences.
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

    def say_what_you_see(self, string):
        """
        The fundamental look and say operation that generates each 
        term of a look and say sequence from its predecessor. For example, 
        using the standard (default) LookAndSay object, 
        ``say_what_you_see('1112222333')`` returns ``'314233'``.
        """
        if not string: return '' # handles empty string, which is falsy
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
     
    def generate_sequence(self, seed, terms):
        """
        Generates the look and say sequence. The parameter ``seed`` is 
        the initial term in the sequence, and ``terms`` is the 
        number of terms generated.
        """
        if not seed: return None # handles empty seed, which is falsy
        result = [seed]
        for _ in range(terms-1):
            result.append(self.say_what_you_see(result[-1]))
        self.sequence = result

    def get_sequence(self):
        """Returns the look and say sequence as a list of strings"""
        return self.sequence

    def get_length_ratios(self):
        """
        Returns a list of the ratios of lengths of 
        successive terms in the look and say sequence.
        """
        terms = len(self.sequence)
        assert terms > 1, 'Look and say sequence does not have enough terms to compute the ratio of lengths.'
        return [len(self.sequence[i+1]) / len(self.sequence[i]) for i in range(terms - 1)]

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
        self._eigenvector = None

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
                break # pragma: no cover

    def generate_elements(self, *seeds):
        """
        Collects all the persistent elements from all the look and
        say sequences generated by the given seeds. The string(s) entered as the 
        parameter(s) will be used as the seed(s) for generating the elements. 
        This method will clear any elements in the chemistry that exist 
        before this method is called (i.e. prior to collecting from the new seeds). 
        """

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

    def get_elements(self):
        """Returns the elements as a list."""
        return self.elements

    def get_element(self, name):
        """Returns the element with the given name. Returns None there is no element with the given name."""
        for e in self.elements:
            if e.get_name() == name:
                return e

    def clear_elements(self):
        """Resets the list of elements back to the empty list."""
        self.elements = []
        self._eigenvector = None

    def get_periodic_table(self, dec_places = 7, abundance_sum = 100):
        """
        Creates a periodic table including each element's name, string, relative abundance, and decay.
        Returns the periodic table as a nested dictionary.

        """

        return {e.get_name() : {'string' : e.get_string(), 
                                'abundance' : self._get_abundances(dec_places, abundance_sum)[i],
                                'decay' : e.get_decay()}
                                for i, e in enumerate(self.get_elements())}

    def print_periodic_table(self, dec_places = 7, abundance_sum = 100):
        """
        Prints the periodic table. Note the abundances are given as percentages, 
        so they will differ from Conway's abundances by a factor of $10^4$.
        The parameter ``dec_places`` refers to the accuracy of the abundances.
        """
        pt = self.get_periodic_table(dec_places, abundance_sum)
        elt_width = 2 + max(len('element'), max([len(e.get_name()) for e in self.get_elements()]))
        str_width = 2 + max(len('string'), max([len(e.get_string()) for e in self.get_elements()]))
        ab_width  = 2 + max(len('abundance'), max([len(str(prop['abundance'])) for elt, prop in pt.items()]))
        print("{:<{elt_width}} {:<{str_width}} {:<{ab_width}} {}".format('element', 'string', 'abundance', 'decay', elt_width=elt_width, str_width=str_width, ab_width=ab_width))
        for elt, prop in pt.items():
            print("{:<{elt_width}} {:<{str_width}} {:<{ab_width}} {}".format(elt, prop['string'], prop['abundance'], str(prop['decay']), elt_width=elt_width, str_width=str_width, ab_width=ab_width))

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

    def get_dom_eigenvalue(self):
        """
        Returns the maximal real eigenvalue of the decay matrix.
        In the standard case, this will give Conway's constant. 
        In general, this will give the growth rate of the look and say sequence. 
        This method assumes the existence of a real eigenvalue which
        is larger than (the absolute value) of every other eigenvalue.
        This assumption is usually guaranteed by the Perron-Frobenius Theorem.
        """
        assert len(self.elements) > 0, "The get_dom_eigenvalue method requires a nonempty list of elements.\n\tTo fix: Use the generate_elements method prior to calling get_dom_eigenvalue."
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
        so they will differ from Conway's abundances by a factor of $10^4$.
        The abundances can be renormalized by setting the parameter ``abundance_sum``.
        The order of the list corresponds to the order of the list of elements.
        """
        # Computing the eigenvector is time intensive for large chemistries, so 
        # we keep it as an attribute of the object after computing it once.
        if self._eigenvector is None:
            eigenstuff = numpy.linalg.eig(numpy.array(self.get_decay_matrix()))
            eigenvalues = eigenstuff[0]
            eigenvectors = eigenstuff[1]
            index = numpy.where(eigenvalues == max(eigenvalues))
            limiting_eigenvector_nparray = eigenvectors[:,index].real
            # The next two lines are converting the numpy array to a list
            limiting_eigenvector = limiting_eigenvector_nparray.tolist()
            limiting_eigenvector = [elt[0][0] for elt in limiting_eigenvector]
            # Now store the eigenvector as a dictionary to avoid issues with reordering elements
            self._eigenvector = {e:limiting_eigenvector[i] for i, e in enumerate(self.get_elements())}
        eigenvector_lst = [self._eigenvector[e] for e in self.get_elements()]
        abundance = [abs(round(abundance_sum * num / sum(eigenvector_lst), dec_places)) for num in eigenvector_lst]
        return abundance

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
    $d^n$ to $[n]d$ where $[n]$ is a binary representation of n
    that always starts with a 1. For example, this chemistry is 
    valid for standard base two binary look and say sequences. 
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
        return hash((self.string, self.las))

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
    """
    def __init__(self):
        self._splitting_pairs = []
        self._chunks_before_split = []
        self._chunks_after_split = []

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
            return True # pragma: no cover
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
        return False

    def declare_splitting_pairs(self, *pairs):
        """
        Specify pairs of chunks in the form (L, R) 
        such that LR always splits as L.R.
        """
        for pair in pairs:
            self._splitting_pairs.append(pair)

    def declare_split_after(self, *chunks):
        """
        Specify chunks L such that LR splits for every possible R (assuming the last character of L and the first character of R are distinct).
        """
        for chunk in chunks:
            self._chunks_before_split.append(chunk)

    def declare_split_before(self, *chunks):
        """
        Specify chunks R such that LR splits for every possible L (assuming the last character of L and the first character of R are distinct).
        """
        for chunk in chunks:
            self._chunks_after_split.append(chunk)

########### COSMOLOGY #####################

class Cosmology():
    '''
    A class for proving Conway's Cosmological Theorem.
    Currently this will only prove The Cosmological Theorem 
    for the standard decimal look and say sequences where every term
    consists of strings of some of the digits 1, 2, and 3.  
    '''
    def __init__(self, digits = '123'):
        self.las = LookAndSay()
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
                new_atoms = self.split(self.las.say_what_you_see(atom))
                next_atoms += [a for a in new_atoms if a not in self.common_strings]
            atoms = next_atoms
            days += 1
        return days

    def decay_tree(self, string):
        '''
        Starting with the passed string, the say_what_you_see operation is applied
        repeatedly until the result splits as a compound of common elements. 
        Returns a nested dictionary corresponding to the resulting *decay tree*: 
        The root of the tree is the passed string, the children of a node are the 
        atoms obtained by applying the say_what_you_see operation to the node and 
        splitting the result, the leaves are the nodes corresponding to common elements.
        '''
        if string in self.common_strings:
            return string
        return {string: [self.decay_tree(atom) for atom in self.split(self.las.say_what_you_see(string))]}


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
        any string, but may return True even if kid is not contained in any day-old descendant.
        '''
        # Apply the parents function day-times and see what we get:
        ancestors = [kid]
        for _ in range(day):
            next_ancestors = []
            for a in ancestors:
                next_ancestors += self._parents(a)
            ancestors = next_ancestors

        return len(ancestors) != 0
