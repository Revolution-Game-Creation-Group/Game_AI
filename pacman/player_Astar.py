#!/usr/bin/python
# A* search algorithm for pacman, by Matthew Schieber

#!/usr/bin/python
import heapq
def dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid):

    # setup
    search_stack = []
    heapq.heappush(search_stack, (abs(r - food_r) + abs(c - food_c), (pacman_r, pacman_c)))
    dfs = []
    found = False
    paths = {}
    paths[pacman_r, pacman_c] = [(pacman_r, pacman_c)]
    
    # search
    while(not found):
        
        location = heapq.heappop(search_stack)[1]
        path = paths[location]       
        
        if(not (location in dfs)):
            dfs.append(location)
            lr = location[0]
            lc = location[1]
            if(grid[lr][lc] == '.'):
                found = True
                continue

            h = abs(r - food_r) + abs(c - food_c)
                
            # up
            if(lr - 1 >= 0):
                dest = (lr - 1, lc)
                val = grid[dest[0]][dest[1]]
                if(val != '%' and (not (dest in search_stack))):
                    paths[dest] = path + [dest]
                    heapq.heappush(search_stack, (h, dest))
        
            # left
            if(lc - 1 >= 0):
                dest = (lr, lc - 1)        
                val = grid[dest[0]][dest[1]]
                if(val != '%' and (not (dest in search_stack))):
                    paths[dest] = path + [dest]
                    heapq.heappush(search_stack, (h, dest))
            
            # right
            if(lc + 1 < c):
                dest = (lr, lc + 1)        
                val = grid[dest[0]][dest[1]]
                if(val != '%' and (not (dest in search_stack))):
                    paths[dest] = path + [dest]
                    heapq.heappush(search_stack, (h, dest))

            # down
            if(lr + 1 < r):
                dest = (lr + 1, lc)        
                val = grid[dest[0]][dest[1]]
                if(val != '%' and (not (dest in search_stack))):
                    paths[dest] = path + [dest]
                    heapq.heappush(search_stack, (h, dest))

        
    destination = (food_r, food_c)
    print (len(paths[destination]) - 1)
    for i in paths[destination]:
        print ("%d %d" % (i[0], i[1]))
    return


pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)
