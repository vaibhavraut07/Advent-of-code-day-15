def spin(grid):
    for y in range(len(grid)): 
        for x in range(len(grid[0])): 
            if grid[y][x] == '0': 
                ny = y grid[ny][x] = '.' 
                while ny >= 0 and grid[ny][x] 
                ny-=1 
                grid[ny+1][x] = '0'

def score(grid):
ans = 0  
for y in range(len(grid)):
    for x in range(len(grid[0])): 
        if grid[y][x] == '0':
            ans += len(grid)-y
return ans
def main(input):
grid = [list(1) for 1 in input.splitlines()] 
print(*grid, sep='\n') 
spin(grid) 
print()
print(*grid, sep='\n')
return None