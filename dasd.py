from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
import time 
from selenium.webdriver import TouchActions
from bs4 import BeautifulSoup as bs
import random
print("enter username") 
username = '' 

print("enter password") 
password = ''

print("enter the url") 
url = '/'

def path(): 
	global chrome 
	# starts a new chrome session 
	chrome = webdriver.Firefox()
def url_name(url): 
	# the web page opens up 
	chrome.get(url) 
	
	# webdriver will wait for 4 sec before throwing a 
	# NoSuchElement exception so that the element 
	# is detected and not skipped. 
	time.sleep(4) 
def login(username, your_password):
    log_but = chrome.find_element_by_class_name("L3NKy") 
    time.sleep(2) 
    log_but.click()	 
    time.sleep(4) 
    # finds the username box 
    usern = chrome.find_element_by_name("username")	 
    # sends the entered username 
    usern.send_keys(username) 

    # finds the password box 
    passw = chrome.find_element_by_name("password")	 

    # sends the entered password 
    passw.send_keys(your_password)	
    passw.send_keys(Keys.RETURN)
    time.sleep(3)
    # finds the login button 
    #log_cl = chrome.find_element_by_class_name("IwRSH")	 
    #log_cl.click() 
    time.sleep(4) 
    notk = chrome.find_element_by_class_name("yWX7d")
    notk.click()
    time.sleep(3)
    #import insta
def send_message():
    message = chrome.find_element_by_class_name('_862NM ')
    message.click()
    time.sleep(2)
    chrome.find_element_by_class_name('HoLwm ').click()
    time.sleep(1)
    l = ['Divu','Hitler','Kaisi hai oya','hello','beta','chandigharh vapis aagi','oya','Sunn','Divneet']
    for x in range(50):
        mbox = chrome.find_element_by_tag_name('textarea')
        mbox.send_keys(random.choice(l))
        mbox.send_keys(Keys.RETURN)
        time.sleep(1.2)
        if (x%10):
            print(x)
def first_picture(): 
    pic = chrome.find_element_by_class_name("kIKUG").click()
     # clicks on the first picture
def like_pic():
    time.sleep(2)
    like = chrome.find_element_by_class_name('fr66n')
    soup = bs(like.get_attribute('innerHTML'),'html.parser')
    if(soup.find('svg')['aria-label'] == 'Like'):
        like.click()
    chrome.implicitly_wait(3) 
    like = chrome.find_element_by_class_name('sH9wk')
    like.click()
    time.sleep(2)
    like_a = chrome.find_element_by_class_name('Ypffh')
    like_a.send_keys('Sir')
    time.sleep(1.5)
    like_a.send_keys(Keys.RETURN)
    time.sleep(1.5)
def next_picture(): 
	time.sleep(2) 

	# finds the button which gives the next picture 
	nex = chrome.find_element_by_class_name("coreSpriteRightPaginationArrow") 
	time.sleep(1) 
	return nex 
def continue_liking(): 
	while(True): 
		next_el = next_picture() 

		# if next button is there then 
		if next_el != False: 

			# click the next button 
			next_el.click() 
			time.sleep(2) 

			# like the picture 
			like_pic()	 
			time.sleep(2)			 
		else: 
			print("not found") 
			break
path() 
time.sleep(1) 

url_name(url) 

login(username, password) 
send_message()
#first_picture() 
#like_pic() 

#continue_liking() 

