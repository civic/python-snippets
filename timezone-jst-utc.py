from datetime import datetime
from dateutil import tz
import dateutil
from dateutil.tz.tz import tzfile
import pytz

JST = tz.gettz("Asia/Tokyo")
UTC = tz.gettz("UTC")

A = datetime(2021, 4, 1, 11, 22, 33, tzinfo=UTC)
print(A)

B = datetime(2021, 4, 1, 11, 22, 33)
print(B)

C = datetime(2021, 4, 1, 20, 22, 33, tzinfo=JST)
print(C)

D = datetime(2021, 4, 1, 20, 22, 33)
print(D)

print(A.astimezone(JST) == C)
print(C.astimezone(UTC) == A)
print(B.replace(tzinfo=UTC).astimezone(JST).replace(tzinfo=None))


A2 = pytz.timezone("UTC").localize(datetime(2021, 4, 1, 11, 22, 33))
print(A2)
C2 = pytz.timezone("Asia/Tokyo").localize(datetime(2021, 4, 1, 20, 22, 33))
print(C2)