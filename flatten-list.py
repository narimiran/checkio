def flat_list(b):
 c=[]
 for a in b:
  c+=flat_list(a) if isinstance(a,list) else [a]
 return c