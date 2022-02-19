import requests
import json

#To get the digits of the randomness field from cloudflare:
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
randomness= data["randomness"]

#To get the last 20 characters:
randomness=randomness[-20:]

digits=list(randomness.split(" "))

char_occurrence=[0]*16

#Hexadecimal dictionary
hex_dict={'a': 10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

for i in range(20):
    #If the character is a number
    if(digits[i].isalpha()==False):
        char_occurrence[digits[i]]+=1
    #Else if the character is a letter
    else:
        char_occurrence[hex_dict.get(digits[i])]+=1



          
        
    












      








