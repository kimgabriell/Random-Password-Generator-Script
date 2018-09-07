import string
from random import *
import random

length = random.randint(10, 17)

characters = string.ascii_letters + string.punctuation  + string.digits

password =  "".join(choice(characters) for x in range(randint(8, 16)))

print (password)
