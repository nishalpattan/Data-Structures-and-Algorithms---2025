# Last updated: 8/3/2025, 9:02:16 PM
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if topRight.x >= bottomLeft.x and topRight.y >= bottomLeft.y:
            if sea.hasShips(topRight, bottomLeft):
                if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                    return 1
                midX = (topRight.x + bottomLeft.x) // 2
                midY = (topRight.y + bottomLeft.y ) // 2
                return self.countShips(sea,Point(midX, midY),bottomLeft) + self.countShips(sea, topRight,Point(midX + 1, midY + 1)) + self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1)) + self.countShips(sea,Point(topRight.x , midY), Point(midX + 1, bottomLeft.y))
                
            
            else:
                return 0
            
        
        else:
            return 0