'''
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. 
Other areas are safe to sail in. There are other explorers trying to find the treasure. 
So you must figure out a shortest route to the treasure island.
Assume the map area is a two dimensional grid, represented by a matrix of characters. 
You must start from the top-left corner of the map and can move one block up, down, left or right at a time. 
The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. 
Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks.
You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. 
Output the minimum number of steps to get to the treasure.
Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
'''
def numIslands(grid):
    result = dfs(grid,0,0,-1,float("inf"))
    print(result[1])
    
def dfs(grid,i,j,curr_steps,min_steps):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 'D' or grid[i][j] == '#':
        return None,min_steps
    if grid[i][j] == 'X':
        curr_steps+=1
        min_steps = min(curr_steps, min_steps)
        return None,min_steps
    else:
        temp = grid[i][j]
        grid[i][j] = '#'
        curr_steps += 1
        left = dfs(grid,i,j-1,curr_steps,min_steps)
        right = dfs(grid,i,j+1,curr_steps,min_steps)
        up = dfs(grid,i-1,j,curr_steps,min_steps)
        down = dfs(grid,i+1,j,curr_steps,min_steps)

        grid[i][j] = temp
        return curr_steps,min(left[1],right[1],up[1],down[1])

print(numIslands([['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]))