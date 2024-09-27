mat = [[1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9]]

m = len(mat)  
n = len(mat[0]) 

result = []
row = 0
col = 0
direction = 1  
for i in range(m * n):
    result.append(mat[row][col])
    if direction == 1:
        if col == n - 1:  
            row += 1
            direction = -1
        elif row == 0:  
            col += 1
            direction = -1
        else: 
            row -= 1
            col += 1
    else:
        if row == m - 1:
            direction = 1
        elif col == 0: 
            row += 1
            direction = 1
        else:  
            row += 1
            col -= 1

print(result)
