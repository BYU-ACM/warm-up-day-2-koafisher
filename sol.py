def Binary_Search(arr, to_find):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: arr (a list ordered from least to greatest)
             to_find (the item to find in arr)
     returns: index (int), x, s.t. arr[x] == to_find
              None(none-type) if for all x, arr[x] != to_find
  """
  r = len(arr)-1
  l = 0
  while l <= r:
    m = (l+r)/2
    if arr[m] == to_find:
        return m
    elif arr[m] > to_find:
        r = m-1
    else:
        l = m+1
  return None


def Bisection(func, left_side, right_side, tol=1e-5):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: func (a function)
             left_side (a value for the function to take on, it should have opposite sign from `right_side`)
             right_side (a value for the function to take on, it should have opposite sign from `left_side`)
             tol (a value for which the function should return once a value at least that distance from zero is found)
     returns: root (float), x, s.t. abs(func(x))<tol
              None(none-type) if func(left_side), func(right_side) < 0 or func(left_side), func(right_side) > 0
  """
  N = 1
  Nmax = 100
  while N <= Nmax:
    c = (left_side+right_side)/2.
    if func(c) == 0 or (right_side-left_side)/2. < tol:
        return c
    N += 1
    if (func(c)*func(left_side) > 0):
        left_side = c
    else:
        right_side = c
  return None

