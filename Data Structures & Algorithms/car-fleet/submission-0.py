class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        we are given the position and speed of the ith car, they are both n length
        we are also given a destination (target) that the cars are supposed to hit in miles
        we need to return the amount of car fleets (arrays of cars with the same position and 
        speed)

        potential solution: we should create a tuple of position and speed so that we can 
        sort by position (arrays get sorted by first value in the tuple).

        """
        stack = []
        pos_speed = [(p,s) for p,s in zip(position, speed)]

        # for i in range(len(speed)):
        #     pos_speed.append((position[i], speed[i]))
        
        pos_speed.sort(reverse=True)

        for p,s in pos_speed:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()

        return len(stack)
            

        