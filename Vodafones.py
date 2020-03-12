import requests,time
print("\033[1;35mwelcome to idroid xtreme scripte")
print(" \033[1;34mYOUSSEF ELKHODARY is congratulations for you to use here scripte")
print("\033[1;35m _   _____   _____    _____   _   _____       __    __  _____   _____    _____       ___  ___   ____")
print("| | |  _  \ |  _  \  /  _  \ | | |  _  \      \ \  / / |_   _| |  _  \  | ____|     /   |/   | | ____|")
print("| | | | | | | |_| |  | | | | | | | | | |       \ \/ /    | |   | |_| |  | |__      / /|   /| | | |__")
print("| | | | | | |  _  /  | | | | | | | | | |        }  {     | |   |  _  /  |  __|    / / |__/ | | |  __|")
print("| | | |_| | | | \ \  | |_| | | | | |_| |       / /\ \    | |   | | \ \  | |___   / /       | | | |")
print("|_| |_____/ |_|  \_\ \_____/ |_| |_____/      /_/  \_\   |_|   |_|  \_\ |_____| /_/        |_| |_____|")
print (          "\033[1;31mby Youssef Elkhodary")







time.sleep(2)

print ("\033[1;34menter your number and pass")


class main():
    def __init__(self,number, password):
        self.number=number
        self.password=password
  
   

        headers ={'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Realme C2 Colore OS/V6.2)',
                  'Host': 'mobile.Vodafone.com.eg',
                  'Accept-Encoding': 'gzip'}
        
        url = 'https://https://mobile.Vodafone.com.eg/SignIn.svc/SignInUser'
        data = '{"appVersion":"2020.2.2","channel":{"ChannelName":"AnaVodafone","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (number,password)
        response = requests.post(url, headers=headers, data=data)
        global userID            
        userID = response.json()['SignInUserResult']['UserData']['UserID']
        if userID:
            print(" Welcome to our world"+"\n")




    def token(self,number,password):
       
        url2 = 'https://mobile.Vodafone.com.eg/BucketsService.svc/SubscribeToBuckets'

        headers2 ={'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Realme C2 Colore OS/V6.2)',
                  'Host': 'mobile.Vodafone.com.eg',
                  'Accept-Encoding': 'gzip'}
        
        data2 = '{"begindate":"","bucketID":"1211 ","channel":{"ChannelName":"AnaVodafone","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dial":"%s","lang":"ar","renewDuration":"","renewEndDate":"","userID":"%s","isEasyLogin":false,"password":"%s"}' % (number,userID,password)

        r=requests.post(url2,data=data2,headers=headers2)
      






    def delta(self,number , password):
            
        url3 = 'https://mobile.Vodafone.com.eg/BucketsService.svc/UnSubscribeToBuckets'
               
        headers3 ={'Content-type': 'application/json',
                   'Accept': 'application/json',
                    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Realme C2 Colore OS/V6.2)',
                    'Host': 'http://mobile.Vodafone.com.eg',
                    'Accept-Encoding': 'gzip'}

        data3='{"bucketID":"1211","channel":{"ChannelName":"AnaVodafone","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dial":"%s","lang":"ar","isEasyLogin":false,"password":"%s"}'% (number,password)

                
        req=requests.post(url3,data=data3,headers=headers3)
       
    ##
    
    def india(self,number , password):
            
        url4 = 'https://mobile.Vodafone.com.eg/BucketsService.svc/UnSubscribeToBuckets'
               
        headers4 ={'Content-type': 'application/json',
                   'Accept': 'application/json',
                    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Realme C2 Colore OS/V6.2)',
                    'Host': 'http://mobile.Vodafone.com.eg',
                    'Accept-Encoding': 'gzip'}

        data4='{"bucketID":"89001","channel":{"ChannelName":"AnaVodafone","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dial":"%s","lang":"ar","isEasyLogin":false,"password":"%s"}'% (number,password)

                
        req=requests.post(url4,data=data4,headers=headers4)
        





number=input("enter you are vodafone phone number ... :")
password= input("enter you are account password ... :")



fox=main(number,password)
print("\033[1;30mto send  the bandle in you are account enter(A)\n   \033[1;32mto delete your bandle enter (D)\n \033[1;33mDelete your bandel and renew enter (R)"+"\n" +"\033[1;31mto extented the bandle enter (M)")

delta= input(("Enter your choice here==>> "))


if delta =="A":
    x=fox.token(number,password)  #token
    print("now you have the bandle")
elif  delta =="D":
    x=fox.delta(number,password)

    print("you are bandle has been deleted ")

elif  delta =="R":
    x=fox.india(number,password)
    print("done the bandle was deleted and renew again")

else:
    x=fox.delta(number,password)
    time.sleep(6)
    
    x=fox.token(number,password)
    print("done the bandle was extented ")
#IDROID_XTREME_ONLY_ONE