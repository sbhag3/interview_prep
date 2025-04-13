class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        parent = [i for i in range(len(accounts))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        owner_map = {}

        for i, account in enumerate(accounts):
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email in owner_map:
                    union(i, owner_map[email])
                owner_map[email] = i

        ans = defaultdict(list)
        for email, owner in owner_map.items():
            ans[find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
        