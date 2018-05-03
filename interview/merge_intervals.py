# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
def build_interval(arrays):
    return [Interval(arr[0],arr[1]) for arr in arrays]

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __repr__(self):
        return "start : %s end: %s" %(self.start, self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        k = []
        if len(intervals) < 2:
            return intervals
        temp = intervals[0]
        for j in intervals[1:]:
            if temp.end < j.start:
                k.append(temp)
                temp = j
            elif temp.end < j.end:
                temp.end = j.end  # overwriting the end

        k.append(temp)
        return k



# intervals = build_interval([[1,3],[2,6],[8,10],[15,18]]);
# k =  Solution()
# expected_output = build_interval([[1,6],[8,10],[15,18]])
# actual_output = k.merge(intervals)
# assert expected_output == actual_output;

intervals = build_interval([[1,4],[0,4]]);
k = Solution()
actual_output = k.merge(intervals)
print actual_output
