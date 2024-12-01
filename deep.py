# User input here:
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

# In case of Input 42/ Forty-two print Yes:
if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")

# Or else NO.
else:
    print("No")
