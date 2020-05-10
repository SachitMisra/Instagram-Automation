from selenium import webdriver
from time import sleep
import requests
import json
import random
import os 
from os import environ
from flask import Flask


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
#driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

def jokes():

    import requests

    url = "https://joke3.p.rapidapi.com/v1/joke"

    payload = "{ \"content\": \"A joke here\", \"nsfw\": \"false\"}"
    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "18a2b74abfmsh33d6bc7affb0c0dp156da5jsn8a17725ee385",
        'content-type': "application/json",
        'accept': "application/json"
        }

    response = requests.request("GET", url, data=payload, headers=headers)
    json_response= response.json()

    return(json_response["content"])

def top_indian_news():
    url="https://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=daf20c40821a4172a6ed2f8e377d4f1a"
    response= requests.get(url)
    json_response= response.json()
    return json_response['articles'] [0] ['title'] +" : "+ json_response['articles'] [0] ['description'] +"\n"+ json_response['articles'] [1] ['title'] +" : "+ json_response['articles'] [1] ['description'] +"\n"+ json_response['articles'] [2] ['title'] +" : "+ json_response['articles'] [2] ['description']

def international_news():
    url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=daf20c40821a4172a6ed2f8e377d4f1a"
    response= requests.get(url)
    json_response= response.json()
    return json_response['articles'] [0] ['title'] +" : "+ json_response['articles'] [0] ['description'] +"\n"+ json_response['articles'] [1] ['title'] +" : "+ json_response['articles'] [1] ['description'] +"\n"+ json_response['articles'] [2] ['title'] +" : "+ json_response['articles'] [2] ['description']
 
def total_cases():
    try:
        url = "https://api.covid19api.com/summary"
        response = requests.get(url)
        json_response= response.json()
        s=json_response['Global']
        NC= s['NewConfirmed']
        TC= s['TotalConfirmed']
        ND= s['NewDeaths']
        NR= s['NewRecovered']
        
        q= "New Confirmed - " +str(NC) + "\nTotal Confirmed - " + str(TC) + "\nNew Deaths - "+ str(ND)+"\n New Recovered - "+ str(NR)
        return q
    except:
        return "Server down, please try again in a few hours"
    
def country_cases(last_message):
    try:
        url = "https://api.covid19api.com/summary"
        response = requests.get(url)
        json_response= response.json()
        c=0
        for i in range (0, len(json_response['Countries'])):
            
            list_of_countries=  json_response['Countries'] [i] ['Country']
            
        
            if(last_message==list_of_countries):
                print(list_of_countries)
                s= str(list_of_countries)
                c= c+1
                return("The Total Confirmed cases in " +  s +" " + str(json_response['Countries'] [i] ['TotalConfirmed']) + "\nTotal Deaths in " +  s +" " + str(json_response['Countries'] [i] ['TotalDeaths']))
                #return "country name detected"
            
        if(c==0):
            return "No country found"
    except:
        return "Server down, please try again in a few hours"
                   
def like(self):
    
    self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div/div").click()
    sleep(1)
    anyphotosthere = self.driver.find_elements_by_class_name("_9AhH0")
    if(len(anyphotosthere)>0):
        # Find the first photo and then click it
        self.driver.find_element_by_class_name("_9AhH0").click()     
        sleep(1)
        #liking the picture
        self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
        sleep(1) 
        onlyone = self.driver.find_elements_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a")
        if(len(onlyone)!=0):
            self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a").click()

        sleep(1) 
        try:
            for photos in range(0,10):
                self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
                sleep(1)
                self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow").click()  
                sleep(1)
            self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button").click()
            self.driver.get("https://www.instagram.com/direct/inbox/")
        except:
            self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button").click()
            self.driver.get("https://www.instagram.com/direct/inbox/")
        else:
            self.driver.get("https://www.instagram.com/direct/inbox/")

class InstaBot:
 
    def __init__(self, username, password):
        self.driver= webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        #username
        self.driver.find_element_by_class_name('pexuQ').send_keys(username)
        #Pass
        self.driver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input').send_keys(password)
        #Login button click
        self.driver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button > div').click()
        sleep(5)
        while(True):
            print("Started")
            #Not now
            notnowhai = self.driver.find_elements_by_xpath('//button[text()="Not Now"]')
            if(len(notnowhai)>0):
                self.driver.find_element_by_xpath('//button[text()="Not Now"]').click()
            sleep(1)
            #heart button
            # self.driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(4) > a > svg').click()
            # sleep(1)
            #Whos follow request
            # x = self.driver.find_elements_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(4) > div > div > div.uo5MA._2ciX.tWgj8.XWrBI > div._01UL2 > div > div > div > div > div.PUHRj.eKc9b.H_sJK > div.YFq-A')
            # print("New follow requests : ")
            # print(len(x))
            # if (len(x)>0):
            #     self.driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(4) > div > div > div.uo5MA._2ciX.tWgj8.XWrBI > div._01UL2 > div > div > div > div > div.PUHRj.eKc9b.H_sJK > div.YFq-A').click()
            # sleep(1)

            # x is a list that contains the text "Confirm
            # ActionChains performs a series of actions
            # anyreq = self.driver.find_elements_by_xpath("//button[contains(text(),'Confirm')]")
            # print("How many people have sent requests : ")
            # print(len(anyreq))
            #c=0
            # if len(anyreq)>0:
            #     for x in self.driver.find_elements_by_xpath("//button[contains(text(),'Confirm')]"):
            #         webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
            
            #self.driver.get("https://www.instagram.com/icantkeepusernames/")
            #sleep(2)
            #self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]").click()
            #sleep(1)
            #scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
            #last_ht,ht =0,1
            #while last_ht!=ht:
            #    last_ht = ht
            #    sleep(1)
            #    ht = self.driver.execute_script("""
            #    arguments[0].scrollTo(0, arguments[0].scrollHeight);
            #    return arguments[0].scrollHeight;
            #    """, scroll_box)
            #    sleep(1)
            #    followers = self.driver.find_elements_by_class_name("y3zKF")
            #    for y in self.driver.find_elements_by_class_name("y3zKF"):
            #        webdriver.ActionChains(self.driver).move_to_element(y).click(y).perform()
                           
            self.driver.get("https://www.instagram.com/direct/inbox/")
            #if any msg requests (like 1 or 2)
            sleep(2)
            msgrequest = self.driver.find_elements_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/button")
            sleep(2)
            if(len(msgrequest)>0):
                #click the request button
                self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/button").click()
                sleep(1)
                #click on the first request
                self.driver.find_element_by_class_name("OEMU4").click()
                #accept it
                self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/button/div/div").click()
            sleep(1)
            try:
                y= self.driver.find_elements_by_class_name("_41V_T")
                while len(y)!=0:
                    y= self.driver.find_elements_by_class_name("_41V_T")
                    if(len(y)==0):
                        break
                    else:
                        y[0].click()
                        msg = self.driver.find_elements_by_tag_name('span')
                        print("Last message in chats "+ msg[len(msg)-1].get_attribute('innerHTML'))
                        lastmsg = msg[len(msg)-1].get_attribute('innerHTML')
                        if(lastmsg == "Usa" or lastmsg == "USA" or lastmsg == "usa" or lastmsg == "America" or lastmsg == "Murica"):
                            info = country_cases("United States of America")
                        else:
                            info = country_cases(lastmsg)
                        if(lastmsg == "Like"):
                            like(self)
                            #self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Service temporarily down please try again in a while.")
                            #self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        elif(lastmsg== "Total Cases" ):
                            total_cases()
                        elif (lastmsg=="Hi" or lastmsg=="Hey" or lastmsg == "hi" or lastmsg=="hey"):
                            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Hi, I am the Chinese bot not to be confused with a bat. Type \"List\" to know what I learnt in China ;)")
                            self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        elif(lastmsg=="List" or lastmsg == "list" or lastmsg == "What"):
                            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Type \"Total\" for total cases, \"Country Name\" for a specific country, \"News\" for domestic news, \"International\" for International News, \"Like\" for getting your pictures liked, \"Tell me a joke\" to hear a quick joke, \"Memes\" for memes")
                            self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        elif (lastmsg=="Credits" or lastmsg == "Credit"):
                            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Made by @anushkawwww and @s0a0c0h0i0t")
                            self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        elif (lastmsg=="Memes" or lastmsg == "Meme" or lastmsg == "meme" or lastmsg == "Send memes"or lastmsg == "Send meme" or lastmsg == "Lol"or lastmsg == "Haha"or lastmsg == "XD"or lastmsg == "Lmao"or lastmsg == "Ok"):
                            accname = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div/div").get_attribute('innerHTML')
                            self.driver.get("https://www.instagram.com/chinese_bot_not_bat/")
                            sleep(2)
                            #finds the post
                            randompost = self.driver.find_elements_by_class_name("eLAPa")
                            randompost[random.randint(0, 5)].click()
                            sleep(2)
                            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/button").click()
                            sleep(2)
                            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div[1]").click()
                            sleep(2)
                            self.driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[1]/div/div[2]/input").send_keys(accname)
                            sleep(2)
                            #click first option checkbox
                            self.driver.find_element_by_class_name("dCJp8").click()
                            sleep(2)
                            #click send button
                            self.driver.find_element_by_xpath("/html/body/div[6]/div/div[1]/div/div[2]/div/button").click()
                            sleep(1)
                            #click close
                            self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()
                            #open dm again
                            self.driver.get("https://www.instagram.com/direct/inbox/")
                            #self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("This service is temporarily down. You can visit our page for memes instead")
                            #self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        elif(lastmsg == "Total cases"or lastmsg == "Total"):
                            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(total_cases())
                            self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        elif(lastmsg=="Good bot"):
                            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("This isn't reddit relax")
                            self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        elif(lastmsg=="Jokes" or lastmsg=="Joke" or lastmsg=="Tell me a joke" or lastmsg=="Another" or lastmsg=="I'm bored"):
                            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(jokes())
                            self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        elif(lastmsg=="News"):
                            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(top_indian_news())
                            self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        elif(lastmsg=="International" or lastmsg == "International news"):
                            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(international_news())
                            self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        elif(info =="No country found"):
                            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Not a valid command, type Hi to get further assistance")
                            self.driver.find_element_by_xpath('//button[text()="Send"]').click()
                        else:
                            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(info)
                            self.driver.find_element_by_xpath('//button[text()="Send"]').click()  
                            sleep(1) 
            except:
                self.driver.get("https://instagram.com")
                sleep(1)
            print("Ended")
            sleep(1)
            self.driver.get("https://instagram.com")
            newdm = self.driver.find_elements_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div")
            while(len(newdm)==0):
                sleep(5)
                newdm = self.driver.find_elements_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div")
                print("Nothing new, waiting")

        sleep(10)

InstaBot("", "")
