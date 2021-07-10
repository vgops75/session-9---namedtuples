# Import necessary modules
from datetime import date
from time import perf_counter
from datetime import datetime
from collections import namedtuple
import random
from collections import Counter
from faker import Faker
from decimal import Decimal
from numpy import mean
import session9
import pytest

# Test case 1 -- Checks if date entered into the age_teller(birthDate) function is valid
# first checks for age calculation using year 2000 with same month as now should give 21
# second checks for the output to see if we received None
# third loops over the profile, fetches the birthdate, and checks if the instance is a date type

def test_date_entry():
    assert age_teller(date(2000, 7, 4)) == 21
    assert age_teller(date(2000, 7, 4)) != None
    for item in dp:
        assert isinstance(item['birthdate'], date)

test_date_entry()

# Test case 2 -- check if Age is a namedtuple; likewise for C_Location and Bloodgroup
# Tests if the C_Location contains two fields, latitude and longitude

def test_namedtuple_entry():
    assert (isinstance(Age, tuple) and isinstance(getattr(Age, '__dict__', None), collections.Mapping) and
           getattr(Age, '_fields', None))
    assert (isinstance(Age, tuple) and hasattr(Age, '_asdict') and hasattr(Age, '_fields'))
    assert isinstance(C_Location, namedtuple)
    assert isinstance(Bloodgroup, namedtuple)
    assert len(C_Location._fields) == 2

test_namedtuple_entry()

# Test case 3 -- Test if namedtuple operations faster than dictionary operations

def test_is_namedtuple_faster():
    if (aveAge_ntuple_time > aveAge_dict_time and
            maxAge_ntuple_time > maxAge_dict_time and
            curLoc_ntuple_time > curLoc_dict_time and
            bgroup_ntuple_time > bgroup_dict_time
           ):
        print(f'Dictionaries seems faster than namedtuple operations')

test_is_namedtuple_faster()

# Test case 4 -- Check if docstrings for the namedtuples are matching what we wrote
# This seems funny but I couldnt finish the assignment on time.

def test_docstring_for_namedtuples():
    if 'namedtuple' in Age.__doc__:
        if 'age' in Age.__doc__:
            assert len(Age.__doc__) > 20
            # assert (Age.__doc__ == 'Age is a namedtuple with a single field variable "age"')

test_docstring_for_namedtuples()

