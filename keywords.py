greeting = [
    'hi',
    'hello',
    'wassup',
    'hey',
    'ola',
]

farewell = [
    'bye',
    'cya',
    'see you soon',
    'adios',
    'laters'
]

import random

def send_greeting(x):
    temp = greeting.copy()
    return random.choice(temp.remove(x))

    