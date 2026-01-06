# 355. Design Twitter

https://leetcode.com/problems/design-twitter/

## Classify
**Heap (Priority Queue)**, **Hash Map**, **Design**

這題的本質是 "Merge k Sorted Lists"。每個使用者的推文列表可以視為一個依時間排序的序列，而 `getNewsFeed` 就是要從這些有序列表中取出合併後的前 10 大元素。

## Line of thought

### 資料結構
我們需要維護兩個主要關係：
1.  **使用者關係 (Follow Graph)**：能夠快速查找某個 User 關注了誰。
    *   `HashMap: userId -> Set(followeeIds)`
2.  **推文儲存 (Tweet Storage)**：能夠存取某個 User 發過的推文。為了排序，我們需要一個全域的時間戳記 (Timestamp)。
    *   `HashMap: userId -> List[(time, tweetId)]`
    *   `Global Variable: time`

### 核心操作：Get News Feed
當 User A 要看 News Feed 時，我們要聚合他關注的人（例如 B, C）以及自己的推文。
這就像是有多個已經排好序的隊伍（B 的推文列表、C 的推文列表...），我們要從這些隊伍的頭部挑出最新的推文。

1.  **初始化**：
    *   找出所有關注對象（包括自己）。
    *   把每個人 **最新的那一篇** 推文放入 Max Heap 中。
    *   Heap 依照 `time` 排序（Python 的 heapq 是 Min Heap，所以存 `-time`）。

2.  **提取與推進 (Pop & Push)**：
    *   從 Heap 拿出當前最新的推文，放入結果。
    *   如果這篇推文來自 User B 的第 `k` 篇，那麼就把 User B 的第 `k-1` 篇（下一篇較舊的）放回 Heap。
    *   就像是指標在多個陣列上向後移動。

3.  **終止**：
    *   直到收集滿 10 篇，或 Heap 空了為止。

### 具體追蹤 (Concrete Trace)
假設 User 1 關注 User 2。
*   User 1 tweets: `[time=1, id=101], [time=3, id=103]`
*   User 2 tweets: `[time=2, id=201], [time=4, id=204]`

`getNewsFeed(1)` 流程：

1.  **Init Heap**:
    *   User 1 最新是 `(time=3, id=103)`
    *   User 2 最新是 `(time=4, id=204)`
    *   Heap: `[(-4, 204, u2, idx=1), (-3, 103, u1, idx=1)]`

2.  **Loop 1**:
    *   Pop Max `(-4, 204)` -> Result: `[204]`
    *   Push Next of User 2 -> `(time=2, id=201)`
    *   Heap: `[(-3, 103, u1, idx=1), (-2, 201, u2, idx=0)]`

3.  **Loop 2**:
    *   Pop Max `(-3, 103)` -> Result: `[204, 103]`
    *   Push Next of User 1 -> `(time=1, id=101)`
    *   Heap: `[(-2, 201, u2, idx=0), (-1, 101, u1, idx=0)]`

...依此類推，直到收集 10 篇。

## Solution

### Heap Optimization
*   **Time Complexity**: $O(F + k \log F)$, where $F$ is number of followees, $k$ is 10 (number of tweets to retrieve).
*   **Space Complexity**: $O(F)$ for the heap.

```python
class Twitter:

    def __init__(self):
        self.f_map = defaultdict(set)
        self.t_map = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t_map[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get followee
        followees = self.f_map[userId] | {userId}
        res = []
        heap = []

        # Push the last tweet of each followee into the heap
        for uid in followees:
            tweets = self.t_map[uid]
            if tweets:
                last_idx = len(tweets) - 1
                time, tweetId = tweets[last_idx]
                heapq.heappush(heap, (-time, tweetId, uid, last_idx))
            
        while heap and len(res) < 10:
            _, tweetId, uid, idx = heapq.heappop(heap)
            res.append(tweetId)

            # Push the previous tweet of the same user into the heap
            if idx - 1 >= 0:
                time, next_tweetId = self.t_map[uid][idx-1]
                heapq.heappush(heap, (-time, next_tweetId, uid, idx-1))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.f_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.f_map[followerId]:
            self.f_map[followerId].remove(followeeId)
```

### Naive Sort approach
*   **Time Complexity**: $O(N \cdot F \log (N \cdot F))$
*   **Space Complexity**: $O(N \cdot F)$

```python
class Twitter:

    def __init__(self):
        self.f_map = defaultdict(set)
        self.t_map = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t_map[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = []
        # 1. 把每個人 (包含自己) 的前 10 篇拿出來
        followees = self.f_map[userId] | {userId}
        for uid in followees:
            # 這裡利用 List slicing，只拿最後 10 個
            candidates.extend(self.t_map[uid][-10:]) 
        
        # 2. 全部混在一起排序 (根據時間倒序)
        candidates.sort(key=lambda x: x[0], reverse=True)
        
        # 3. 取出前 10 個 ID
        return [tweetId for time, tweetId in candidates[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.f_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.f_map[followerId]:
            self.f_map[followerId].remove(followeeId)
```