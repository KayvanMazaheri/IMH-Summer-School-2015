def inverse(a,n):
  t = 0
  new_t = 1
  r = n
  new_r = a
  while new_r!=0:
    quotient=r//new_r
    temp=new_t
    new_t= t-(quotient*new_t)
    t=temp
    temp=new_r
    new_r= r-(quotient*new_r)
    r=temp
  if r>1:
    print ("a is not invertible!")
    t=-n
  if t<0:
    t=t+n
  return t

