# Import necessary modules
from datetime import date
from datetime import datetime
from time import perf_counter
from collections import namedtuple
from collections import Counter
import random
from faker import Faker
from decimal import Decimal
from numpy import mean

# function to return age when date of birth is given in the format date(YYYY, MM, DD)
def age_teller(birthDate: 'date') -> int:
    '''
    The function takes birth date in date format i.e. date(2000, 11, 4) and returns the age in int format.
    Obviously, a crude approximation -- finding total number of days in between today and birth date and dividing
    it by 365.24. We can remove the int to return the age in float too.
    :param birthDate: in date format
    :return: int
    '''
    num_days = 365.24
    if isinstance(birthDate, date):
        age = int((date.today() - birthDate).days / num_days)
        return age
    else:
        return f'ValueError: Enter birthDate in date format, eg. date(2000, 11, 4)'

# Faker() has an in-built random generator and hence its just enough to generate profiles
# using an iterator. Here seed() function is used to generate repeatable instances of profiles.

Faker.seed(10)
myFaker = Faker()
sample_size = 10000
dp = [myFaker.profile() for i in range(sample_size)]

# Faker() gives profile in dictionary form, and I thought it is better to add the age as an additonal (key, value)
# pair so that we don't continue the use of dictionary while using namedtuple as we need to compare the execution time.

# Adding one more (key, value) pair to the profiles dictionary
for item in dp:
    if 'age' not in item.keys():
        item['age'] = age_teller(item['birthdate'])


# namedtuple operation -- Average Age
# Find Average age among profiles

Age = namedtuple('Age', 'age')
total = 0
num_ops = 1000
for i in range(num_ops):
    start = perf_counter()
    ageList = [Age(item['age']) for item in dp]
    x = Age(*map(mean, zip(*ageList)))
    total += perf_counter() - start
aveAge_ntuple_time = total/num_ops
print(f'Average Age for a set of {sample_size} random profiles is {x.age}')
print(f'and the average execution time is {aveAge_ntuple_time} secs')

# Another method to get the average age using namedtuple's name operator, i.e. x.age
ave_age = mean(list(map(lambda x: x.age, ageList)))
print(f'Average Age by name operator is {ave_age}')

Age.__doc__ = '''\
Age is a namedtuple with a single field variable "age"'''

Age.age.__doc__ = '''\
"age" is a field variable for the namedtuple "Age", and "age" is not present in Faker(). 
It is added as a last (key, value) pair using age_teller function in this notebook'''

# namedtuple operation -- Oldest Person's Age
# find the maximum age among profiles

# Age = namedtuple('Age', 'age') # We can remove this -- already defined above

total = 0
num_ops = 1000
for i in range(num_ops):
    start = perf_counter()
    ageList = [Age(item['age']) for item in dp]
    x = max(list(map(lambda x: x.age, ageList)))
    total += perf_counter() - start
maxAge_ntuple_time = total/num_ops
print(f'Oldest Person\'s\' age for a set of {sample_size} random profiles is {x}')
print(f'and the average execution time is {maxAge_ntuple_time} secs')

# Another method to get the oldest age using namedtuple and map
old_Person = Age(*map(max, zip(*ageList)))
print(f'Average Age by name operator is {old_Person.age}')

# namedtuple operation -- Mean Current Location

# Actually this method of obtaining mean current location is flawed. Suppose we have a positive
# latitude of X, and another a latitude of negative X, mean location ends up as 0. The preferred
# method of caluclating mean current location in terms of latitude and longitude involves inclusion
# of trigonometrical functions

C_Location = namedtuple('C_Location', ('lat', 'long'))
total = 0
num_ops = 1000
for i in range(num_ops):
    start = perf_counter()
    locList = [C_Location(*item['current_location']) for item in dp]
    x = C_Location(*map(mean, zip(*locList)))
    total += perf_counter() - start
curLoc_ntuple_time = total/num_ops
print(f'The mean of current location clusters for {sample_size} random profiles is {x}')
print(f'and the average execution time is {curLoc_ntuple_time} secs')

C_Location = namedtuple('C_Location', ('lat', 'long'))
C_Location.__doc__ = '''\
Named Tuple having 2 fields, first field for latitude and the second one for longitude'''

C_Location.lat.__doc__ = '''\
This field stores the latitude of the current location.'''

C_Location.long.__doc__ = '''\
The "long" field stores the longitude data of the current location'''

# namedtuple operation -- Largest Blood Type
# Slightly hard or I don't know how to use namedtuple to the best here

Bloodgroup = namedtuple('Bloodgroup', 'blood_group')
total = 0
num_ops = 1000
for i in range(num_ops):
    start = perf_counter()
    bgList = [Bloodgroup(item['blood_group']) for item in dp]
    x = Counter(bgList).most_common(1)[0]
    ntime = Counter(bgList).most_common(1)[0][1]
    bg_x = x[0].blood_group
    total += perf_counter() - start
bgroup_ntuple_time = total/num_ops
print(f'The largest occurring blood_group type for {sample_size} random profiles is "{bg_x}"')
print(f'which occurred {ntime} times')
print(f'and the average execution time is {bgroup_ntuple_time} secs')

Bloodgroup.__doc__ = '''\
Named Tuple for storing the blood type data.'''

Bloodgroup.blood_group.__doc__ = '''\
The blood type is recorded as a string.'''

# Dictionary operation -- Average Age
# Find Average age among profiles

total = 0
num_ops = 1000
for i in range(num_ops):
    start = perf_counter()
    x = mean([item['age'] for item in dp])
    total += perf_counter() - start
aveAge_dict_time = total/num_ops
print(f'Average Age for a set of {sample_size} random profiles is {x}')
print(f'and the average execution time is {aveAge_dict_time} secs')

# Dictionary operation -- Oldest Person's Age

# The application of dictionary in calculating oldest person's age seems not justifiable
# as most of the time consuming operations are done in extracting maximum out a list that is
# obtained from already existing dictionary.

total = 0
num_ops = 1000
for i in range(num_ops):
    start = perf_counter()
    x = max([item['age'] for item in dp])
    total += perf_counter() - start
maxAge_dict_time = total/num_ops
print(f'Oldest Person\'s\' age for a set of {sample_size} random profiles is {x}')
print(f'and the average execution time is {maxAge_dict_time} secs')

# Dictionary operation -- Oldest Person's Age --- Method 2 (Only using dict, even faster)

# The application of dictionary in calculating oldest person's age seems not justifiable
# as most of the time consuming operations are done in extracting maximum out a list that is
# obtained from already existing dictionary.

total = 0
num_ops = 1000
for i in range(num_ops):
    start = perf_counter()
    max_age = 0
    for item in dp:
        if item['age'] > max_age:
            max_age = item['age']
    x = max_age
    total += perf_counter() - start
maxAge_dict_time2 = total/num_ops
print(f'Oldest Person\'s\' age for a set of {sample_size} random profiles is {x}')
print(f'and the average execution time is {maxAge_dict_time2} secs')

# Dictionary operation -- Mean Current Location

total = 0
num_ops = 1000
for i in range(num_ops):
    start = perf_counter()
    x = C_Location(*map(mean, zip(*locList)))
    total += perf_counter() - start
curLoc_dict_time = total/num_ops
print(f'The mean of current location clusters for {sample_size} random profiles is {x}')
print(f'and the average execution time is {curLoc_dict_time} secs')

# Another method to get locList above
loc_dict = []
for item in dp:
    loc_dict.append(item['current_location'])

locList_2 = list(map(mean, zip(*loc_dict)))

# Dictionary operation -- Largest Blood Type

total = 0
num_ops = 1000
for i in range(num_ops):
    start = perf_counter()
    bgDict = dict()
    for item in dp:
        key = item.get('blood_group')
        if key not in bgDict:
            bgDict[key] = 1
        else:
            bgDict[key] += 1
    rev_dict = {v:k for k,v in bgDict.items()}
    x = rev_dict[max(rev_dict)]
    ntime = max(rev_dict)
    total += perf_counter() - start
bgroup_dict_time = total/num_ops
print(f'The largest occurring blood_group type for {sample_size} random profiles is "{x}"')
print(f'which occurred {ntime} times')
print(f'and the average execution time is {bgroup_dict_time} secs')

# This marks the end of session 9 namedtuple assignment - Part 1 and 2

# From here, I will add the Part 3 of the Assignment.
# Part 3 of Assignment
# Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name,
# symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock
# market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close
# are not totally random. You can only use namedtuple.









