''' Emulate a web service flow of data processing. A bit of scaffolding
has been done in the code.

>>> data = '{"username": "oscar", "password": "trashcan", "account": 1234, "amount": 12.03}'
>>> deposit(data)
'OK'
>>> data = '{"username": "oscar", "password": "trash", "account": 1234, "amount": 14.98}'
>>> deposit(data)
'Invalid Password'
>>> data = '{"username": "oscar", "password": "trashcan", "account": 1234, "amount": 4.12}'
>>> withdraw(data)
'OK'
>>> data = '{"username": "oscar", "password": "trashcan", "account": 1235, "amount": 2.54}'
>>> withdraw(data)
'Invalid Account'
>>> data = '{"username": "oscar", "password": "trashcan", "account": 1234}'
>>> balance(data)
'7.91'
>>> data = '{"username": "oscar", "password": "trashcan"}'
>>> balance(data)
'No Account Number Provided'
'''

import json 
from decimal import Decimal


user = {
        "password" : "trashcan",
        "account" : 1234,
        "balance" : Decimal(0)      # we Decimal-ify this because we want to freeze the sig digits of our numbers
    }

def data_parser(fn):
    """
    Parses JSON data and returns it
    """
    def parsed(data):
        # after job is done, parsing data up to the function passed in
        data = json.loads(data)
        if 'amount' in data: 
            data['amount'] = Decimal(str(data['amount']))
        return fn(data)
    # in this pipeline, we need to return the last function 
    return parsed


def validate(fn):
    """
    Validates incoming data and returns errors if they exist
    """
    def valid(data):
        if 'account' not in data: 
            return 'No Account Number Provided'
        elif data['password'] != user['password']:
            return 'Invalid Password'
        elif user['account'] != data['account']:
            return 'Invalid Account'
        else:  
            return fn(data)
    return valid


@data_parser
@validate
def deposit(transaction):
    user['balance'] += transaction['amount']
    return 'OK'     # separate concerns of deposit and parse/validate 



@data_parser
@validate
def withdraw(transaction):
    user['balance'] -= transaction['amount']
    return 'OK'


@data_parser
@validate
def balance(transaction):
    return str(user['balance'])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
#     def incrementor(fn):
#         def wrapped(x):
#             return fn(x) + 42
#         return wrapped
#     
#     @incrementor
#     def echo(x):
#         return x
#     
#     print echo(42)
    