# Tuples and Named Tuples

Tuples are immutable, and Classes are mutable. Named Tuples offers the best of the both containers. Named Tuples are immutable but offers class-like name operator for clarity. In addition, Named Tuples enables faster instancing of objects of desired structure.

### Assignment 9:
1) Use Faker library to get 10000 random profiles. a) Using namedtuple, calculate the largest blood type, mean current_location, oldest_person_age, and average age. b) Add proper doc-strings c) Include 5 test cases

##### Faker() has an in-built random generator and hence its just enough to generate profiles using an iterator. Here seed() function is used to generate repeatable instances of profiles.

I have included a function age_teller(birthDate) to add a (key, value) pair to the profile created from Faker(). The function takes the birthdate from the profile and converts to age in years.

I found that the dictionary operations to be faster than the namedtuple operations. Probably because the Faker() data profiler creates data in dictionary format, and hence available for dictionary operations.

