"""Sample Input

STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]

Sample Output

Yes
No

Explanation

In the first test case, pick in this order: left -4, right -4 , left -3 , right - 3, left -2 , right -1 .
In the second test case, no order gives an appropriate arrangement of vertical cubes. will always come after either or
."""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque


def check(d):
    while d:
        big = d.popleft() if d[0] > d[-1] else d.pop()
        if not d:
            return "Yes"
        if d[-1] > big or d[0] > big:
            return "No"


for i in range(int(input())):
    int(input())
    d = deque(map(int, input().split()))
    print(check(d))