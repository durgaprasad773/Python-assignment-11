s=input()
if s.isdigit():
    print("Digit")
elif s.islower():
    print("Lowercase Letter")
elif s.isupper():
    print("Uppercase Letter")
else:
    print("Special Character")