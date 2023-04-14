import datetime as dt
from datetime import date
from plan import Plan
from plan import *
from user import User



nizar = User("nizar", basic_plan, dt.datetime(2019, 1, 6))
wisnu = User("wisnu", standard_plan, date.today())

print(nizar)