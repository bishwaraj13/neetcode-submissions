class Solution:
    def jobScheduling(
        self,
        startTime: List[int],
        endTime: List[int],
        profit: List[int]
    ) -> int:

        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            # No more jobs left
            if i == len(intervals):
                return 0

            # Return the already computed result
            if i in cache:
                return cache[i]

            # Option 1: skip the current job
            dont_include = dfs(i + 1)

            # Option 2: include the current job
            include = intervals[i][2]

            # Find the first job that does not overlap
            # with the current job
            j = i + 1

            while (
                j < len(intervals)
                and intervals[j][0] < intervals[i][1]
            ):
                j += 1

            # Add the maximum profit starting from
            # the next non-overlapping job
            include += dfs(j)

            # Store the better of the two choices
            cache[i] = max(include, dont_include)

            return cache[i]

        return dfs(0)