def cavityMap(grid):
    i=1
    n=len(grid)
    n-=1
    flag=False
    while i<n:
        s=grid[i][0]
        j=1
        while j<n:
            if grid[i+1][j]!="X" and grid[i-1][j]!="X" and grid[i][j+1]!="X" and grid[i][j-1]!="X" and int(grid[i][j-1])<int(grid[i][j]) and int(grid[i][j+1])<int(grid[i][j]) and int(grid[i+1][j])<int(grid[i][j]) and int(grid[i-1][j])<int(grid[i][j]):
                s+="X"+grid[i][j+1]
                j+=1
            else:
                s+=grid[i][j]
            j+=1
        if j==n:
            s+=grid[i][-1]
        grid[i]=s
        i+=1
    '''for i in grid:
        print(i)'''
    return grid
        
                
            
        
