import pytz
from datetime import datetime, timedelta

JST = pytz.timezone("Asia/Tokyo")
UTC = pytz.UTC

now = datetime.now(tz=JST)
print(now)

d1 = datetime(2021, 4, 10, 11)
print(d1)


print(datetime(2021, 9, 10, 11, tzinfo=JST))
print(JST.localize(datetime(1896, 1, 1, 0)))
