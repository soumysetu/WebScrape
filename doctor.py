import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/cb5ac97987f269ac550469af94ee98ea27"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
full_name = soup.find("div", class_="docInfo",recursive=True).h3.get_text()
specification = soup.find("div", class_="ProviderMainCard__Tag-lt2r6j-1 dmNAGQ speciality-tag",recursive=True).get_text()
gender = soup.find("div", class_="ProviderMainCard__Tag-lt2r6j-1 dmNAGQ",recursive=True).get_text()
city = soup.find("div", class_="ResidencySelection__Wrapper-sc-1neb61h-0 hGKZHE",recursive=True).span.get_text()
phone = soup.find("div", class_="LocationCard__Wrapper-sc-15q16f7-0 jAbTOx card location-card",recursive=True).span.get_text()
address = soup.find("div", class_="BasicInfo__Wrapper-gas5ca-0 hMRnVk basicInfoWrapper",recursive=True).get_text()
# print("full name - ",full_name)
# print("specification - ",specification)
# print("gender - ",gender)
# print("phone - ",phone)
# print("city - ",city)
# print("address - ",address)

data = {
  "full name": [full_name],
  "specifications": [specification],
  "gender": [gender],
  "phone": [phone],
  "city": [city],
  "address": [address],
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)


list1=[]
list1.append("Name : ")
list1.append(full_name)
list1.append("specification : ")
list1.append(specification)
list1.append("gender : ")
list1.append(gender)
list1.append("phone : ")
list1.append(phone)
list1.append("city : ")
list1.append(city)
list1.append("address : ")
list1.append(address)
with open('C:/Users/Lenovo/Desktop/websc/name.txt', 'w') as f:
    for line in list1:
        f.write(line)
        f.write('\n')






