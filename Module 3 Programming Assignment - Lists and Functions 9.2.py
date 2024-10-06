#9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.

def get_odds():
    for number in range(10):
        # Make an equation that will find an odd number in my range of 10 
        if number % 2 != 0:
            #Use yield instead of return so that the program can continue until i want it to print the off numbers.
            yield number

odds = get_odds()

# Print the odd numbers using 'odds'
for odd in odds:
    print(odd)
