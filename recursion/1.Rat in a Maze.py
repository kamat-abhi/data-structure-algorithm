class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        # code here
        result = []
        choice = [['U', -1, 0], ['D', 1, 0], ['L', 0, -1], ['R', 0, 1]]
        n = len(maze[0])
        if maze[0][0] == 1:
            self.solve(0, 0, n, [], choice, maze, result)
            result.sort()
        return result
    
    def solve(self, x, y, n, path, choice, maze, result):
        if x == n-1 and y == n-1:
            result.append("".join(path))
            return
        for val in choice:
            newX = x + val[1]
            newY = y + val[2]
            if newX>=0 and newY>=0 and newX<n and newY< n and maze[newX][newY] == 1:
                maze[x][y] = 0
                path.append(val[0])
                self.solve(newX, newY, n, path, choice, maze, result)
                maze[x][y] =1
                path.pop()