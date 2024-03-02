import smtplib
import datetime as dt
import random


now = dt.datetime.now()
day_of_the_week = now.weekday()


MY_EMAIL = "starstruckcentral01@gmail.com"
PASSWORD = "dqkdjxwkygjyvint"



if day_of_the_week == 5:
    with open("quotes.txt") as file:
        quote = random.choice(file.readlines())
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="mckingmichael003@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )




