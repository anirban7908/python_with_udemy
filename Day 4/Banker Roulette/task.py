import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# by random number
rand_name = random.randint(0, (len(friends) - 1))
print(friends[rand_name])

# by random choice
rand_name = random.choice(friends)
print(rand_name)