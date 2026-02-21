def risk(mid,low,high,duration):
  if high:
    return "high risk")
  if mid>7:
    return "medium"
  if duration >=7 and low:
    return "Consult a doctor"
  return low

#test
x = risk(low = 3, high>=8)
print(x)
