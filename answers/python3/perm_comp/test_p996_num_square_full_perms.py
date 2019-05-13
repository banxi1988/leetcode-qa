# coding: utf-8

__author__ = '代码会说话'

import math
import itertools
from collections import Counter
def calc_squares():
  END = math.pow(10,9) * 2 + 1
  squares = set()
  root = 1
  square = 1
  while square < END:
    root += 1
    square = root * root
    squares.add(square)
  return squares

def distinct_permutations(iterable):
    """Yield successive distinct permutations of the elements in *iterable*.

        >>> sorted(distinct_permutations([1, 0, 1]))
        [(0, 1, 1), (1, 0, 1), (1, 1, 0)]

    Equivalent to ``set(permutations(iterable))``, except duplicates are not
    generated and thrown away. For larger input sequences this is much more
    efficient.

    Duplicate permutations arise when there are duplicated elements in the
    input iterable. The number of items returned is
    `n! / (x_1! * x_2! * ... * x_n!)`, where `n` is the total number of
    items input, and each `x_i` is the count of a distinct item in the input
    sequence.

    """

    def perm_unique_helper(item_counts, perm, i):
      """Internal helper function

      :arg item_counts: Stores the unique items in ``iterable`` and how many
          times they are repeated
      :arg perm: The permutation that is being built for output
      :arg i: The index of the permutation being modified

      The output permutations are built up recursively; the distinct items
      are placed until their repetitions are exhausted.
      """
      if i < 0:
        yield tuple(perm)
      else:
        for item in item_counts:
          if item_counts[item] <= 0:
            continue
          perm[i] = item
          item_counts[item] -= 1
          for x in perm_unique_helper(item_counts, perm, i - 1):
            yield x
          item_counts[item] += 1

    item_counts = Counter(iterable)
    length = sum(item_counts.values())

    return perm_unique_helper(item_counts, [None] * length, length - 1)

class Solution:
  def numSquarefulPerms(self, A: 'List[int]') -> 'int':
    alen = len(A)
    if alen < 2:
      return 0
    squares = calc_squares()
    count = 0
    for perm in distinct_permutations(A):
      all = True
      for i in range(0, alen-1):
        sum = perm[i] + perm[i+1]
        if sum not in squares:
          all = False
          break
      if all:
        count += 1
    return  count


def test():
  s = Solution()
  assert s.numSquarefulPerms([1,17,8]) == 2
  assert s.numSquarefulPerms([2,2,2]) == 1
  assert s.numSquarefulPerms([1,1,1,1,1,1,1,1,1,1,1,1]) == 0
  assert s.numSquarefulPerms([99,62,10,47,53,9,83,33,15,24]) == 19
