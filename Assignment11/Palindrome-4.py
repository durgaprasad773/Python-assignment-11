s=input().lower()
s = s.replace("'","")
s=s.replace(" ","")
if s[::-1] == s:
    print(True)
else:
    print(False)