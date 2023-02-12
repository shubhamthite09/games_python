import smtplib
import _datetime
a =_datetime.date.today()
print(a)
email = "fortestingnewmail@gmail.com"
password = "evaihxshspgixbds"

with smtplib.SMTP("smtp.gmail.com") as connection:
   connection.starttls()
   connection.login(user=email, password=password)
   connection.sendmail(from_addr=email, to_addrs="fortestingnewmail1@yahoo.com", msg="subject:new testing mail\n\n this is body of my mail")

