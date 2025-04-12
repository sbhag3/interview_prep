class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()
        q = sorted((val, i) for i, val in enumerate(queries))

        ans = [-1] * len(queries)

        curr = 0
        pq = []

        for query, idx in q:
            while curr < len(intervals) and query >= intervals[curr][0]:
                diff = intervals[curr][1] - intervals[curr][0] + 1
                print((diff, intervals[curr]))
                heappush(pq, (diff, intervals[curr]))
                curr += 1

            while pq and (pq[0][1][1] < query):
                heappop(pq)

            print(pq[0][0] if pq else -1)
            ans[idx] = pq[0][0] if pq else -1

        return ans
        