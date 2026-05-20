class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {} # userId: {tweet, timestamp}
        self.followers = {} #followerId: followeeId
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        heapq.heappush(self.tweets[userId], [-self.time, tweetId])


        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        newMaxHeap = []
        users = self.followers.get(userId, set())
        if userId not in users:
            users.add(userId) 
        print(users)
        usersList = list(users)
        
        for user in usersList:
            for t, v in self.tweets.get(user, []):
                heapq.heappush(newMaxHeap, [t, v])
        # print(newMaxHeap)
        while newMaxHeap and len(res) != 10:
            res.append(heapq.heappop(newMaxHeap)[1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            return
        self.followers[followerId].remove(followeeId)
        
