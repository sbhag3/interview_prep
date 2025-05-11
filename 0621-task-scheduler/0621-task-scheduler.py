class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1
        task_max = max(count.values())
        max_cnt = sum(1 for v in count.values() if v == task_max)
        return max(len(tasks), (task_max - 1) * (n + 1) + max_cnt)
        