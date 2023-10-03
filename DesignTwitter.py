'''
Design a simplified version of Twitter where users can post tweets, 
follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) 
    -Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) 
    -Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId)
-  The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) 
-   The user with ID followerId started unfollowing the user with ID followeeId.
'''
from collections import defaultdict
from typing import List
import heapq
class Twitter:
    def __init__(self):
        #Build Two table to throug Hash Map to hold uID -> tweetId and followID->FolloweeId sets
        self.tweetMap = defaultdict(list)
        self.followMap =defaultdict(set)
        self.count = 0
    def postTweet(self,userId:int,tweetId:int):
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -=1

    def follow(self,followerId:int, followeeId:int):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId:int, followeeId:int):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

    def getNewsFeed(self,userId:int) ->List[int]:
        #this would become like merge k-sorted listed 
        ans = []
        minHeap = [] #Store maximum 10 most recenlty made tweets by user and its followee..
        allUserIdList = list(self.followMap[userId]) + [userId]
        #first add most recent tweets from user and its follow into maxheap
        for uId in allUserIdList:
            index = len(self.tweetMap[uId]) - 1
            if index >=0:
                cnt, tweetId = self.tweetMap[uId][index] 
                heapq.heappush(minHeap,[cnt,tweetId,uId,index-1])
        
        while minHeap and len(ans) < 10:
           cnt,tweetId,uId,index = heapq.heappop(minHeap) 
           ans.append(tweetId)
           if index >=0:
               cnt, tweetId = self.tweetMap[uId][index] 
               heapq.heappush(minHeap,[cnt,tweetId,uId,index-1])
        
        return ans


twitter = Twitter()
twitter.postTweet(1, 5) #// User 1 posts a new tweet (id = 5).
print("Get news feed",twitter.getNewsFeed(1))  #// User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2)   #// User 1 follows user 2.
twitter.postTweet(2, 6) #// User 2 posts a new tweet (id = 6).
print("Get news feed" ,twitter.getNewsFeed(1))  #// User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2)  #// User 1 unfollows user 2.
print("Get news feed",twitter.getNewsFeed(1))  #// User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
            
               



    
