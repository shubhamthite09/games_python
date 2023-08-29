
import datetime
import pandas
import random
import smtplib

today = (datetime.datetime.now().month, datetime.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

email = "fortestingnewmail@gmail.com"
password = "evaihxshspgixbds"

if (today) in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_filr:
        contants = letter_filr.read()
        contants = contants.replace("[NAME]", birthday_person["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n {contants}")





