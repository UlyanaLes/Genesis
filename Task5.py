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


