# varibles

# Best practices

# -- snake_case naming
# -- start with lowercase or underscore
# -- Letters, numbers, underscores
# -- Case sensitive
# -- Don't overwrite keywords

user_iq = 190
user_age = user_iq/4

print(user_age)

# gotcha
# -- constants
PI = 3.14 # should never reasign this varibles
# -- dunder varibles
print(__name__) # dunder variables, we should not use this 
                # kind of naming conventions for our local
                # variables

username = 'coder'
password = 'secret'
