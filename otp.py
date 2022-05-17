import random
import smtplib

s = smtplib.SMTP("smtp.gmail.com" , 587)
s.starttls()
s.login("sendotp84@gmail.com" , "dolab#11111")
otp = random.randint(1000, 9999)
otp = str(otp)
s.sendmail("sendotp84@gmail.com", "anshidnm@gmail.com",otp)
print("OTP sent succesfully..")
s.quit()

inp = int(input("enter your otp :"))
if inp == int(otp):
    print("Authenticated")
else:
    print("Denied")