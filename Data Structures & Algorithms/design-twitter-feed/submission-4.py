class Twitter:
    def __init__(self):
        self.followers = defaultdict(list)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = list(self.posts[userId])
        # if self.followers.get(userId) == []:
        #     return [post[1] for post in posts]
        following = self.followers.get(userId, [])
        for user in self.posts:
            if user in following:
                posts.extend(self.posts[user])
        heapq.heapify(posts)
        return [tweetId for _, tweetId in heapq.nlargest(10, posts)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)
            

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers.get(followerId).remove(followeeId)
