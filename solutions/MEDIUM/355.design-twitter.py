# Problem ID: 355
# Title: Design Twitter
# Runtime: 11 ms

class User:
    def __init__(self, userId):
        self.userId = userId
        self.tweets = {}
        self.followers = set()
        self.follows = set()

class Twitter:
    def __init__(self):
        self.users = {}
        self.time = 0

    def create(self,userId):
        if userId not in self.users:
            self.users[userId] = User(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.create(userId)
        user = self.users[userId]
        user.tweets[tweetId] = self.time
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        self.create(userId)
        tweets = []
        for tweet,time in self.users[userId].tweets.items():
            tweets.append((tweet,time))
        for followee in self.users[userId].follows:
            user = self.users[followee]
            for tweet,time in user.tweets.items():
                tweets.append((tweet,time))

        tweets.sort(key = lambda x:x[1],reverse = True)
        ret = []
        for i in range(min(10,len(tweets))):
            ret.append(tweets[i][0])
        return ret


    def follow(self, followerId: int, followeeId: int) -> None:
        self.create(followerId)
        self.create(followeeId)
        self.users[followerId].follows.add(followeeId)
        self.users[followeeId].followers.add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.create(followerId)
        self.create(followeeId)
        if followerId in self.users[followeeId].followers:
            self.users[followerId].follows.remove(followeeId)
            self.users[followeeId].followers.remove(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)