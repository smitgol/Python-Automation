# Python-Automation
  This file is Facebook automation project file that uses selenium to do following Tasks:-
        
   1. Login to Facebook
   2. Add the About you in account detail (Note that the about you detail can only added once Hence if About you status is aleardy added in personal detail the Scripts might not work)
	 
3. Visit the friends page and comment on latest post
4. Search the friend nearby area and send request to friend request
	 
Steps to Follow to run this scripts:-
	
Check for the selenium library if not installed then run
						
	pip install selenium
	
Then download Chrome webdriver from below link :- 
	
	https://chromedriver.chromium.org/downloads
	
Get the location of driver :-

Now run the scripts By typing
	
	python autobot.py
	
First file will ask for webdriver path :-

	Enter Webdriver path
	
Then Ask for Facebook Id and Password

	Enter Id and Password
	
Now it will ask for Status to add in About you in personal detail section 

	Enter text to be added in About you section

Now it will ask for comment to be posted in friends Post

	Enter Comment
