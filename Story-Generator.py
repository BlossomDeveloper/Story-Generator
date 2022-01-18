# Generate a random story with given details 

import random

name = ['Marie', 'Hannah', 'Philip', 'Josh', 'Claire', 'Robert']
holidays = ['Sidney', 'Paris', 'Prague', 'Lisbon', 'London', 'Tokyo']
job = ['dentist', 'hairdresser', 'customer service representative', 'police', 'developer', 'singer']
when = ['five days ago', 'yesterday', 'two months ago', 'a couple of years ago', 'a year ago', 'three years']
holiday_places = ['coffee', 'theater', 'museum', 'bar', 'garden', 'restaurant']
what_happened = ['meet new people', 'dance with a stranger', 'received flowers', 'ate best pasta ever',
                 'spent 4 hours in Louvre', 'drank coffee with matcha']

print(random.choice(name) + ' went for holidays in ' + random.choice(holidays) + ', as a ' + random.choice(job) + ' and '
      + random.choice(when) + ' visited ' + random.choice(holiday_places) + ' and ' + random.choice(what_happened))

print(random.choice(name) + ' went for holidays in ' + random.choice(holidays) + ', as a ' + random.choice(job) + ' and '
      + random.choice(when) + ' visited ' + random.choice(holiday_places) + ' and ' + random.choice(what_happened))

print(random.choice(name) + ' went for holidays in ' + random.choice(holidays) + ', as a ' + random.choice(job) + ' and '
      + random.choice(when) + ' visited ' + random.choice(holiday_places) + ' and ' + random.choice(what_happened))

print(random.choice(name) + ' went for holidays in ' + random.choice(holidays) + ', as a ' + random.choice(job) + ' and '
      + random.choice(when) + ' visited ' + random.choice(holiday_places) + ' and ' + random.choice(what_happened))
