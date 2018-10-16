import datetime
now = datetime.datetime.now()
now_srt = datetime.datetime.strftime(now,'%Y-%m-%d %H:%M:%S %f')
#datetime.datetime.strptime()
print(now_srt)
