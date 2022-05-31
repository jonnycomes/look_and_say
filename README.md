# look_and_say
A python module for exploring look and say sequences in the spirit of John H Conway.

## Documentation and resources

- Full documentation for the module [here](https://jonnycomes.github.io/look_and_say/docs/look_and_say.html).

- The theory of standard look and say sequences is explained in Conway's delightful article [The Weird and Wonderful Chemistry of Audioactive Decay](https://link.springer.com/chapter/10.1007/978-1-4612-4808-8_53). 

- For an introduction to nonstandard look and say sequences, see the [notes here](https://jonnycomes.github.io/look_and_say/papers/intro_nonstandard_look_and_say/look_and_say_intro.pdf).

## Example Sessions

### Standard decimal look and say sequences

```python
>>> from look_and_say import *
>>> 
>>> # The default LookAndSay object uses the standard decimal number system:
... decimal = LookAndSay()
>>> 
>>> # Perform the fundamental look and say operation:
... decimal.say_what_you_see('1222111')
'113231'
>>> 
>>> # Generate a look and say sequence
... decimal.generate_sequence(seed='1', num_iterations=5)
>>> decimal.get_sequence()
['1', '11', '21', '1211', '111221', '312211']
>>> 
>>> # Use Conway's splitting theorem to search for all the elements 
... # in the look and say sequence generated from the seed '1'. 
... # This will generate Conway's 92 common elements: 
... chem = Chemistry(decimal)
>>> chem.generate_elements('1')
>>> chem.get_elements()
[H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ga, Ge, As, Se, Br, Kr, Rb, Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd, In, Sn, Sb, Te, I, Xe, Cs, Ba, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Po, At, Rn, Fr, Ra, Ac, Th, Pa, U]
>>> 
>>> # The periodic table is a dictionary holding the chemical properties of each element.
... pt = chem.get_periodic_table(abundance_sum=10**6)
>>> print('Hydrogen:', pt['H'])
Hydrogen: {'string': '22', 'abundance': 91790.383216, 'decay': [H]}
>>> print('Thulium:', pt['Tm'])
Thulium: {'string': '11131221133112', 'abundance': 1204.9083841, 'decay': [Er, Ca, Co]}
>>> 
>>> # Conway's constant can be found as the maximal real eigenvalue of the 
... # characteristic polynomial of the decay matrix:
... chem.get_max_eigenvalue()
1.3035772690342984
>>> chem.get_char_poly()
lambda**18*(lambda - 1)**2*(lambda + 1)*(lambda**71 - lambda**69 - 2*lambda**68 - lambda**67 + 2*lambda**66 + 2*lambda**65 + lambda**64 - lambda**63 - lambda**62 - lambda**61 - lambda**60 - lambda**59 + 2*lambda**58 + 5*lambda**57 + 3*lambda**56 - 2*lambda**55 - 10*lambda**54 - 3*lambda**53 - 2*lambda**52 + 6*lambda**51 + 6*lambda**50 + lambda**49 + 9*lambda**48 - 3*lambda**47 - 7*lambda**46 - 8*lambda**45 - 8*lambda**44 + 10*lambda**43 + 6*lambda**42 + 8*lambda**41 - 5*lambda**40 - 12*lambda**39 + 7*lambda**38 - 7*lambda**37 + 7*lambda**36 + lambda**35 - 3*lambda**34 + 10*lambda**33 + lambda**32 - 6*lambda**31 - 2*lambda**30 - 10*lambda**29 - 3*lambda**28 + 2*lambda**27 + 9*lambda**26 - 3*lambda**25 + 14*lambda**24 - 8*lambda**23 - 7*lambda**21 + 9*lambda**20 + 3*lambda**19 - 4*lambda**18 - 10*lambda**17 - 7*lambda**16 + 12*lambda**15 + 7*lambda**14 + 2*lambda**13 - 12*lambda**12 - 4*lambda**11 - 2*lambda**10 + 5*lambda**9 + lambda**7 - 7*lambda**6 + 7*lambda**5 - 4*lambda**4 + 12*lambda**3 - 6*lambda**2 + 3*lambda - 6)
```

### Standard ternary look and say sequences

The following session illustrates how to use the module to explore look and say sequences using the standard ternary number system (i.e. using base 3 with digits 0, 1, and 2). 

Note that the construction of the corresponding LookAndSay object requires a **say function** which, in this case, is a function that converts an integer to it's standard ternary representation. Also, the construction of the Chemistry object requires both the LookAndSay object as well as a **splitting function** which determines when the terms of the look and say sequences split. In this case, one can show that the terms will always split after a run of 0's as well as between a 2 (on the left) and either a 10 or a 1110 (on the right). We use a SplitFuncFactory object to create the splitting function. 

```python
>>> from look_and_say import *
>>> 
>>> # Define a "say function"
... def ternary(num):
...     '''Returns the ternary representation of a nonnegative integer'''
...     if num < 3:
...         return str(num)
...     return ternary(num // 3) + str(num % 3)
... 
>>> 
>>> # Use the Split Function Factory to create a split function:
... sff = SplitFuncFactory()
>>> sff.declare_split_after('0')
>>> sff.declare_splitting_pairs(('2', '1110'), ('2', '10'))
>>> split = sff.get_split()
>>> 
>>> # Instantiate the LookAndSay and Chemistry objects:
... ternary_ls = LookAndSay(ternary)
>>> ternary_chem = Chemistry(ternary_ls, split)
>>> 
>>> # Generate elements and order them according to relative abundances:
... ternary_chem.generate_elements('0', '1', '2')
>>> ternary_chem.order_elements('abundance')
>>> 
>>> # Print chemical properties:
... ternary_chem.print_periodic_table()
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
>>> print(ternary_chem.get_char_poly(latex=True))
\lambda^{6} \left(\lambda - 1\right)^{2} \left(\lambda + 1\right)^{2} \left(\lambda^{2} + 1\right) \left(\lambda^{3} - \lambda - 1\right) \left(\lambda^{5} - \lambda^{3} + 1\right)
>>> print(ternary_chem.get_max_eigenvalue())
1.3247179572447458
```

## Projects that used the look_and_say module

- A D3 force graph showing [the decay of Conway's elements](https://observablehq.com/@jonnycomes/the-decay-of-conways-look-and-say-elements).

- A D3 collapsable tree showing the [descendants of Methuselum](https://observablehq.com/@jonnycomes/descendants-of-methuselum).

## Acknowledgments

- The initial implementation of the proof() method in the Cosmology class was written with Ethan Bassingthwaite and Monika de los Rios in the Spring of 2022 at The College of Idaho. We followed the strategy of Zeilberger's proof with implementation similar to that of Litherland. 
