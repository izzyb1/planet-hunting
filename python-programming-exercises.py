# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
x,y = np.loadtxt("DATA/xy.txt",unpack=True)
# %%
"""
1. Write a program that outputs ‘Hello World’ to the terminal
"""
print("Hello World")

# %%
"""
2. Write a program that outputs ‘Hello World’ 50 times using a for loop
"""
_ = [print(f"{x+1}:Hello World") for x in range(50)]

# %%
"""
3. Write a program with a for loop that iterates 50 times and outputs ‘Hello
World’ after every 5 iterations.
"""
for i in range(50):
    if (i+1) % 5 == 0:
        print(f"{i+1}:Hello World")

# %%
"""
4. Write a program with a for loop with 50 iterations and outputs ‘Hello
World’ every odd value of the loop counter and, and ‘Goodbye World’
every even value.
"""
for i in range(50):
    msg = "Hello World" if (i+1) % 2 == 0 else "Goodbye World"
    print(f"{i+1}:{msg}")

# %%
"""
5. Read in the text file ‘xy.txt’ and print the data to the terminal in 2 columns
"""
(x,y) = np.loadtxt("DATA/xy.txt",unpack=True)
for i in range(len(x)):
    print(f"{x[i]},{y[i]}")

# %%
"""
6. Plot the data in ‘xy.txt’ with blue dots
"""
plt.figure()
plt.plot(x,y,"b.")

# %%
"""
7. Plot the data in ‘xy.txt’ with read crosses
"""
plt.figure()
plt.plot(x,y,"rx")

# %%
"""
8. Plot the data in ‘xy.txt’ as a line plot
"""
plt.figure()
plt.plot(x,y,"b-")

# %%
"""
9. Find the individual sums of the ‘x’ data and the ‘y’ data and print them to
the terminal
"""
print(f"x:{np.sum(x):n} y:{np.sum(y):n}")

# %%
"""
10. Determine the individual means for the ‘x’ and ‘y’ data and print them to
the terminal
"""
print(f"x:{np.mean(x):n} y:{np.mean(y):n}")

# %%
"""
11. Write a code that creates 3 variables called ‘day’, ‘month’, ‘year’. Get
 the code to ask the user to input values for each variable, and then output
 the values is the form “Todays date is:” dd/mm/yyyy. Now run the code using
 todays date as the input.
"""
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
print(f"Today's date is: {day:02}/{month:02}/{year:04}")