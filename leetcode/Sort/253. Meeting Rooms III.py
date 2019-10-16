"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the max number of conference one room can host.

Solution:
Greedy
First sort the event according to (end_time, duration) in ascending order.
Then sweep the events with initial end = -Inf and ans = 0

if the arrival time is greater or equal to end, increment ans, update end as the end time for current event.
otherwise ignore the current event

如果让一个会议室容纳的会议最多，让结束的早的会议尽量在前，早结束了下一场就能开始。
"""


# Greedy
# Time: O(NlogN)
# Space: O(N)
def universityCareerFair(arrival, duration):
    aux = sorted(
        list(zip(arrival, duration)),
        key=lambda p: (sum(p), p[1])
    )
    ans, end = 0, -float('inf')
    for arr, dur in aux:
        if arr >= end:
            ans, end = ans + 1, arr + dur
    return ans