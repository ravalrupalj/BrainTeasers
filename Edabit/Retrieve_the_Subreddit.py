#Retrieve the Subreddit
#Create a function to extract the name of the subreddit from its URL.
import re
def sub_reddit(string):
    r=re.findall(r"/(\w+)/$",string)
    return ''.join(r)
print(sub_reddit("https://www.reddit.com/r/funny/") )
#➞ "funny"
print(sub_reddit("https://www.reddit.com/r/relationships/") )
#➞ "relationships"
print(sub_reddit("https://www.reddit.com/r/mildlyinteresting/") )
#➞ "mildlyinteresting"

