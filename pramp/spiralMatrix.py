def spiral_copy(inputMatrix):
  row_cnt = len(inputMatrix)
  if row_cnt < 1:
    return []
  output = []
  col_cnt = len(inputMatrix[0])
  low_row_idx = 0
  high_row_idx = row_cnt
  low_col_idx = 0
  high_col_idx = col_cnt
  while (low_row_idx < high_row_idx and low_col_idx < high_col_idx):
    for i in range(low_col_idx,high_col_idx):
      output.append(inputMatrix[low_row_idx][i])
    low_row_idx +=1
    for j in range(low_row_idx, high_row_idx):
      output.append(inputMatrix[j][high_col_idx-1])
    high_col_idx -= 1
    for i in range(high_col_idx-1, low_col_idx-1, -1):
      output.append(inputMatrix[high_row_idx-1][i])
    high_row_idx -= 1
    for j in range(high_row_idx-1, low_row_idx-1, -1):
      output.append(inputMatrix[j][low_col_idx])
    low_col_idx += 1
  return output

#assert spiral_copy([[1]]) == [1]
#assert spiral_copy([[1],[2]]) == [1,2]
#print spiral_copy([[1,2]])
print spiral_copy([[1,2],[3,4]])
#assert spiral_copy([[1,2],[3,4]]) == [1,2,4,3]