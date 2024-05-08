a = "15-aug-1947 14:25:00"
hours,minutes,seconds = a.split(" ")[1].split(":")
date,month,year = a.split(" ")[0].split("-")
print(f"hours is {hours}\nminutes is {minutes}\nseconds is {seconds}")
print(f"Date is {date}\nMonth is {month}\nyear is {year}")














