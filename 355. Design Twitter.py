class Twitter(object):
    def __init__(self):
        self.posts = []
        self.follows = {}

    def postTweet(self, userId, tweetId):
        self.posts.append([userId, tweetId])

    def getNewsFeed(self, userId):
        res = []
        for x in range(len(self.posts) - 1, -1, -1):
            post = self.posts[x]
            if post[0] == userId or post[0] in self.follows[userId]:
                res.append(post)
            if len(res) == 10:
                return res
        return res

    def follow(self, followerId, followeeId):
        if followerId not in self.follows.keys():
            self.follows[followerId] = [followeeId]
        else:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        followers = self.follows[followerId]
        for x in range(len(followers)):
            if followers[x] == followeeId:
                del self.follows[followerId][x]
if __name__ == "__mian__":
    t = Twitter()
    t.follow(5, 8)
    t.unfollow(6, 9)
    t.postTweet(1, 5)
    print t.getNewsFeed(1)
    t.follow(1, 2)
    t.postTweet(2, 6)
    print t.getNewsFeed(1)
    t.unfollow(1, 2)
    print t.getNewsFeed(1)
    print 'ffffff'