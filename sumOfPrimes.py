"""
A program to calculate all ways to sum primes such that they add up to a given number
"""

from functools import lru_cache
from time import process_time
from primeList import primesUpToN

@lru_cache(maxsize=None)
def sumOfPrimes(n, primesUpToN=primesUpToN):
  list_ = primesUpToN(n)
  result = ()
  for i in list_:
    if n-i in list_:
      if (n-i, i) in result:
        continue
      result = result + ((i, n-i),)
  return result

@lru_cache(maxsize=None)
def recursiveSumOfPrimes(n, sumOfPrimes=sumOfPrimes, sorted=sorted, len=len, set=set, tuple=tuple): #passing builtins as default arguments for optimization of speed with memoization
  if len(sumOfPrimes(n)) == 0:
    return ()
  start = sumOfPrimes(n)
  result = set()
  for pair in start:
    result.add((*pair,))
    for sub1 in ((pair[0],),) + recursiveSumOfPrimes(pair[0]):
      for sub2 in ((pair[1],),) + recursiveSumOfPrimes(pair[1]):
        result.add(tuple(sorted((*sub1, *sub2))))

  return tuple(result)

def mainloop():
  print("\n\n")
  while True:
    n = int(input("Enter a number: "))
    starttime = process_time()*1000
    result = recursiveSumOfPrimes(n)
    elapsed = 1000*process_time()-starttime
    print(f'There are {len(result)} sums of primes adding up to {n}.')
    if input('Would you like to list them? (y/n/yes/no) > ')[0].lower() == 'y':
      print(result)
    print()
    print(f'That took {elapsed} milliseconds to calculate the entire list.')

if __name__ == '__main__':
  mainloop()
