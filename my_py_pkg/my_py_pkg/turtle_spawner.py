x = input("Input score (or ENTER to finish): ")
a = []
g = []
X = 0
while x != "":
    x = int(x)
    a.append(x)
    x = input("Input score (or ENTER to finish): ")
avg = sum(a)/len(a)
print(f"Average score is {avg:.2f}")
for i in range(len(a)):
    X = (X+(a[i]-avg)**2)
SD = (X/(len(a)-1))**0.5
print(f"Standard deviation is {SD:.2f}")
for i in range(len(a)):
    Xi = a[i]
    if Xi < avg-1.5*SD:
        g.append("F")
    elif Xi < avg-1.0*SD:
        g.append("D")
    elif Xi < avg-0.5*SD:
        g.append("D+")
    elif Xi < avg:
        g.append("C")
    elif Xi < avg+0.5*SD:
        g.append("C+")
    elif Xi < avg+1.0*SD:
        g.append("B")
    elif Xi < avg+1.5*SD:
        g.append("B+")
    else:
        g.append("A")
for i in range(len(a)):
    print(f"Student #{i+1} score: {a[i]} grade: {g[i]}")