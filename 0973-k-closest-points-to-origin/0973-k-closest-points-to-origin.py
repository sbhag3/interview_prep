class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance(point):
            return point[0] ** 2 + point[1] ** 2

        def splitter(remaining, distances, midpoint):
            closer, farther = [], []
            for idx in remaining:
                if distances[idx] <= mid:
                    closer.append(idx)
                else:
                    farther.append(idx)
            return [closer, farther]

        distances = [distance(point) for point in points]
        remaining = [i for i in range(len(points))]

        left, right = 0, max(distances)
        closest = []

        while k:
            mid = (left + right) // 2
            closer, farther = splitter(remaining, distances, mid)
            if len(closer) > k:
                remaining = closer
                right = mid
            else:
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                left = mid + 1
            
        return [points[i] for i in closest]