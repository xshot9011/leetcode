# https://leetcode.com/problems/meeting-rooms/

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        START_INDEX = 0
        END_INDEX = 1
        intervals.sort(key=lambda x: x[START_INDEX])
        
        for index in range(len(intervals)-1):
            print(f'intervalPair: {intervals[index]}')
            print(f'checkPair: {intervals[index+1]}')
            if intervals[index][END_INDEX] > intervals[index+1][START_INDEX]:
                return False
        return True
