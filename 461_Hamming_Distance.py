class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = [x1 - x2 for (x1, x2) in zip(self.bitPositions(x), self.bitPositions(y))]
        return sum(map(abs, a))
    
    def bitPositions(self, z: int):
        positions = [0]*31
        for i in range(31):
            if z > 2**(30-i):
                z -= 2**(30-i)
                positions[i] = 1
            elif z == 2**(30-i):
                positions[i] = 1
                break
        return positions
