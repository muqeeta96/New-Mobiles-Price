import requests
import bs4
import csv

def createBeautifulSoupObject(url):
    html_page=requests.get(url)
    return bs4.BeautifulSoup(html_page.text,"html5lib")

def writeCSV(record):
    with open("New Mobiles and Prices.csv","a",newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(record)

def findMobileNames(BeautifulSoupObject):
    mobileNames=[]
    for i in BeautifulSoupObject.findAll("a"):
        try:
            if  str(i.contents[1])== "<br/>":
                mobileNames.append(str(i.contents[0]).strip() + " " + str(i.contents[2]))
        except IndexError:
            pass
    return mobileNames

def findMobilePrices(BeautifulSoupObject):
    mobilePrices=[]
    for i in BeautifulSoupObject.findAll("span",class_="PriceFont"):
        if str(i.string)!="None":
            mobilePrices.append(str(i.string).strip())
    return mobilePrices

def choiceMobileCompany():
    choice=0
    choicelist=[1,2,3,4,5,6,7,8,9,10]
    while choice not in choicelist:
        print("Press 1: Samsung Mobile Prices")
        print("Press 2: Huawei Mobile Prices")
        print("Press 3: Xiaomi Mobile Prices")
        print("Press 4: Apple Iphone Prices")
        print("Press 5: OnePlus Mobile Prices")
        print("Press 6: Nokia Mobile Prices")
        print("Press 7: Oppo Mobile Prices")
        print("Press 8: Vivo Mobile Prices")
        print("Press 9: Honor Mobile Prices")
        print("Press 10: Realme Mobile Prices")
        choice=int((input("Enter Choice: ")))
        if choice==1:
            soup=createBeautifulSoupObject("https://www.whatmobile.com.pk/Latest_Samsung_Mobiles_Prices")
            return soup,findMobileNames(soup)
        elif choice==2:
            soup=createBeautifulSoupObject("https://www.whatmobile.com.pk/Latest_Huawei_Mobiles_Prices")
            return soup,findMobileNames(soup)
        elif choice==3:
            soup=createBeautifulSoupObject("https://www.whatmobile.com.pk/Latest_Xiaomi_Mobiles_Prices")
            return soup,findMobileNames(soup)
        elif choice==4:
            soup=createBeautifulSoupObject("https://www.whatmobile.com.pk/Latest_Apple_Mobiles_Prices")
            return soup,findMobileNames(soup)
        elif choice==5:
            soup=createBeautifulSoupObject("https://www.whatmobile.com.pk/Latest_OnePlus_Mobiles_Prices")
            return soup,findMobileNames(soup)
        elif choice==6:
            soup=createBeautifulSoupObject("https://www.whatmobile.com.pk/Latest_Nokia_Mobiles_Prices")
            return soup,findMobileNames(soup)
        elif choice==7:
            soup=createBeautifulSoupObject("https://www.whatmobile.com.pk/Latest_Oppo_Mobiles_Prices")
            return soup,findMobileNames(soup)
        elif choice==8:
            soup=createBeautifulSoupObject("https://www.whatmobile.com.pk/Latest_Vivo_Mobiles_Prices")
            return soup,findMobileNames(soup)
        elif choice==9:
            soup=createBeautifulSoupObject("https://www.whatmobile.com.pk/Latest_Honor_Mobiles_Prices")
            return soup,findMobileNames(soup)
        elif choice==10:
            soup=createBeautifulSoupObject("https://www.whatmobile.com.pk/Latest_Realme_Mobiles_Prices")
            return soup,findMobileNames(soup)
        else:
            print("\nInvalid Input\n")


soup,mobileNames=choiceMobileCompany()
mobilePrices=findMobilePrices(soup) 
header=["Mobile Name","Price"]
writeCSV(header)
for i,j in zip(mobileNames,mobilePrices):
    record=[i,j]
    writeCSV(record)