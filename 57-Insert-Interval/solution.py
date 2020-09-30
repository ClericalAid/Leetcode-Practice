class Solution:
    """
    Inserting a new interval into a list of non-overlapping intervals

    [1,3] , [6,9] => insert([2,5])
    output:
    [2,5] , [6,9]

    Is this solved in two steps?
        1)  Insert the interval into the array
        2)  Run through the array and merge overlapping intervals
            We can merge intervals by flagging adjacent intervals to be merged and do it at
            once
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        self.insert_interval(intervals, newInterval)
        return self.merge_intervals(intervals)

    """
    merge_intervals

    Basic steps:
    Rebuild the interval array from the beginning
    Start from 0 and continue to the end
        Push each interval onto our new array
        Merge intervals as they come along
        Interval array has to be sorted by their beginning for this to work
    
    Loop through the array:
    """
    def merge_intervals(self, intervals):
        newIntervalArray = []
        newIntervalArray.append(intervals[0])
        for interval in intervals:
            if newIntervalArray[-1][1] >= interval[0]:
                newIntervalArray[-1][1] = max(newIntervalArray[-1][1], interval[1])
            else:
                newIntervalArray.append(interval)
        return newIntervalArray

    """
    1)
    Loop through the array:
        If we find an interval before which we should insert our interval
            Do the insertion
    2)
    We reached the end of the array without performing an insertion
    Put the array at the end
    """
    def insert_interval(self, intervals, newInterval):
        # 1)
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                return
        # 2)
        intervals.append(newInterval)
        return
