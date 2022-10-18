import unittest
from while_lista import jämna_tal

assert(jämna_tal(10) == [0, 2, 4, 6, 8])
assert(jämna_tal(4) == [0, 2])
assert(jämna_tal(21) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])


