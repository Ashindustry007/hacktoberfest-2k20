#Python program with O(n*n)
def LeftRotate90(m):
  n = len(m[0])
  res = [[0]*n]*n
  for i in range(n):
    for j in range(n):
      res[n-1-j][i] = m[i][j]
  return res
  
  #This function takes a square matrix as 2D list as arguement and returns an Anti ClockWise 90 degree rotated matrix.
