# ### Task 5
#
# Write a class that represents a connection hook and takes as initialisation arguments access_id and access_key.
# Create a decorator to validate if access_key is valid for provided access_id. If not print an error message into console.
#
#
# ConnectionHook(access_id=“Jane@mail.com”, access_key=“cat_12_l”)
#
# >>> Authorization successful.
#
#
# ConnectionHook(access_id=“Jane@mail.com”, access_key=“cat_12_”)
#
# >>> Wrong key, access denied!
#
# Optional:
# Implement solution that will not store the access keys right in code. Think about other way to store and check access_key value.
import logging


# такой формат декоратора вообще ОК или лучше по-другому???
def decorator(ConnectionHook):
    def wrapper(access_id, access_key):
        ConnectionHook(access_id, access_key)
        # здесь лучше присваивать переменную или дважды ходить в дикт???
        if wrapper.access.get(access_id, None) is None or wrapper.access.get(access_id) != hash(access_key):
            logging.error('Wrong key, access denied!')
        else:
            logging.warning('Authorization successful.')
        return ConnectionHook

    wrapper.access = {'Jane@mail.com': hash('cat_12_'), 'Yourmail@mail.com': hash('cat_12_l')}
    return wrapper


@decorator
class ConnectionHook():
    def __init__(self, access_id, access_key):
        self.access_id = access_id
        self.access_key = hash(access_key)
        # почему при печати выводится каждый раз разное значение хэша???
        logging.warning(f'id >> {self.access_id} key >> {access_key} key_hash >> {self.access_key}')


ConnectionHook(access_id='Jane@mail.com', access_key='1')
ConnectionHook(access_id='Jane@mail.com', access_key='cat_12_')
ConnectionHook(access_id='Jane@mail.com', access_key='cat_12_l')
ConnectionHook(access_id='Yourmail@mail.com', access_key='123')
ConnectionHook(access_id='Yourmail@mail.com', access_key='cat_12_l')
