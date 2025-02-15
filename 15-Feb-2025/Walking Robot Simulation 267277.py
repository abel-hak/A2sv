# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

from typing import List, Set, Tuple

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (dx, dy)
        x, y, direction_idx = 0, 0, 0  # Initial position and facing North
        max_distance = 0

        # Convert obstacles list to a set for quick lookup
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:  # Turn left
                direction_idx = (direction_idx - 1) % 4
            elif command == -1:  # Turn right
                direction_idx = (direction_idx + 1) % 4
            else:  # Move forward k units
                dx, dy = directions[direction_idx]
                for _ in range(command):
                    if (x + dx, y + dy) in obstacle_set:  # Stop if obstacle ahead
                        break
                    x += dx
                    y += dy
                    max_distance = max(max_distance, x ** 2 + y ** 2)

        return max_distance
