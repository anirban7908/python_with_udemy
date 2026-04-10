import random
#print number >= 0 and <1 ex: 0.985478522, 0.25487512
# random.random(): Returns a random floating-point number between 0.0 (inclusive) and 1.0 (exclusive).
# print(random.random())

# random.uniform(a, b): Returns a random floating-point number within the specified range [a, b].
# print(random.uniform(1,10))

# random.randint(a, b): Returns a random integer N such that a <= N <= b.
# print(random.randint(1,10))
# random.randrange(start, stop, step): Returns a randomly selected element from range(start, stop, step).
# random.gauss(mu, sigma): Returns a random floating-point number following a Gaussian (normal) distribution with a given mean (mu) and standard deviation (sigma).
response = ''
rand_num = random.randint(0,1)
user_input = input("Flip the coin by typing Heads(H) or Tails(T): ")
if user_input == 'H' and rand_num == 1:
    response = 'Win'
elif user_input == 'T' and rand_num == 0:
    response = 'Win'
else:
    response = 'Loose'
print(rand_num)
print(user_input)
print(response)
