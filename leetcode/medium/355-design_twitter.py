"""
    Leetcode #355
"""


from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.order = 0  # for orderding tweets in timeline

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((self.order, tweetId))
        self.order -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        """
        tw = sorted(tw for i in self.following[userId] | {userId} for tw in self.tweets[i])[:10]
        return [news for i, news in tw]


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.following[followerId].discard(followeeId)



if __name__ == "__main__":


    # Your Twitter object will be instantiated and called as such:
    obj = Twitter()
    obj.postTweet(123, 345)

    param_2 = obj.getNewsFeed(123)

    obj.follow(101, 123)
    obj.unfollow(101, 123)

    obj.postTweet(101, 786)
    obj.follow(123, 101)

    print(obj.getNewsFeed(123))     # [786, 345]

