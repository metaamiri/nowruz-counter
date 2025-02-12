from datetime import timedelta
from khayyam import JalaliDate, JalaliDatetime

next_year = JalaliDatetime.now().year + 1
nowruz = JalaliDatetime ( next_year, 1, 1, 12, 31, 30)
now = JalaliDatetime.now()
diff = nowruz - (now)
days = diff.days
hours = int(diff.seconds / (60*60))
minutes = int((diff.seconds - hours*60*60 ) / 60)
seconds = int(diff.seconds - (minutes*60 + hours*60*60))

print(f"days : {days}, hours : {hours}, minutes :{minutes}, seconds : {seconds}")