from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
import time 
from selenium.webdriver import TouchActions
from bs4 import BeautifulSoup as bs
import random
import urllib
import requests
import os
import re
import getpass
print("enter username") 
username = input()

print("enter password") 
password = getpass.getpass() 

url = 'https://instagram.com/'+input('Enter username of user')
def download_profile():
    time.sleep(1.5)
    img = chrome.find_element_by_class_name('_6q-tv')
    link = img.get_attribute('src')
    response = requests.get(link)
    with open("image.jpg", 'wb') as f:
        f.write(response.content)
def save_image(class_name,img_name):
    time.sleep(0.5)
    pic = chrome.find_element_by_class_name(class_name)
    html = pic.get_attribute('innerHTML')
    soup = bs(html,'html.parser')
    link = soup.find('img')['src']
    response = requests.get(link)
    with open(img_name, 'wb') as f:
        f.write(response.content)
    time.sleep(0.5)
def download_allphotos():
    first_picture()
    user_name = url.split('/')[-1]
    if(os.path.isdir(user_name)):
        save_image('_97aPb',user_name+'/'+'image1')
    else:
        os.mkdir(user_name)
        save_image('_97aPb',user_name+'/'+'image1')
    c = 2    
    while(True):
        next_el = next_picture()
        if next_el != False:
            next_el.click()
            time.sleep(1)
            save_image('_97aPb',user_name+'/'+'image'+str(c))
            time.sleep(1.1)
        else:
            break
        c += 1
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
def get_followers():
    time.sleep(1)
    elems = chrome.find_elements_by_class_name("-nal3 ")
    print(elems)
    elems[1].click()
    time.sleep(1)
    followers = chrome.find_elements_by_class_name("FPmhX")
    time.sleep(1)
    elem_scroll = chrome.find_element_by_class_name('isgrP') 
    lenOfPage = chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;",elem_scroll)
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
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
def getUserFollowers():
    chrome.find_element_by_xpath('//a[contains(@href, "%s")]' % page).click()
    scr2 = chrome.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    time.sleep(2)
    text1 = scr2.text
    print(text1)
    j = re.findall(r'[0-9]+', text1)
    print(j[0])
    for i in range(1, 100):
        scr1 = chrome.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[2]/ul/div/li[%s]' % i)
        chrome.execute_script("arguments[0].scrollIntoView();", scr1)
        # time.sleep(1)
        text = scr1.text.split()
        dirname = os.path.dirname(os.path.abspath(__file__))
        csvfilename = os.path.join(
            dirname, page + "  " + url.split("/")[-2] + ".txt")
        f = open(csvfilename, 'a', encoding='utf-8')
        f.write(str(i)+" - Username = " +
                str(text[0]) + "\t  Name =  " + ' '.join(text[1:-1]) + "\t" + "( " + text[-1] + " )" + "\n")
        f.close()
        # list = text.encode('utf-8').split()
        print('{}: Username - {}  Name - {}'.format(
            i, text[0], ' '.join(text[1:-1])))
page="followers"
path() 
time.sleep(1) 

url_name(url) 

login(username, password) 
#getUserFollowers()
#download_profile()
download_allphotos()

chrome.close()
#get_followers()
#send_message()
#first_picture() 
#like_pic() 

#continue_liking() 

