	#Author-Abhishek Roy
	#Computer science and department
	#Texas A & M 
import tweepy

def Authenticate_twitter():    
	#Authenticating step
	consumer_key = <consumer-key>
	consumer_secret = <consumer-secret>
	access_key = <access-key>
	access_secret = <access-secret>
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	return tweepy.API(auth)
	
def main():
       while 1==1:
		api=Authenticate_twitter()
		it=0
		print "ENTER QUERY and 0 to EXIT"
		Query=raw_input()
		
		if Query=='0':
		     break
		
		for tweet in api.search(q=Query,count=50,result_type="recent",lang="en"):
			    if it < 50 :		
				   print tweet.text		
			     
			    else:
				   break
			    
			    it=it+1
		

main()
