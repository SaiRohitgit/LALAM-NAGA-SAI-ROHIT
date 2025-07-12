def generate_series(a):
  series=[]
  for i in range(a):
    series.append(2*i+1)
  return series
#Example
a=5
result=generate_series(a)
print(result)
