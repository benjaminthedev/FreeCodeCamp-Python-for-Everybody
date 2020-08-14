# Which does the same thing as the following code?:

lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)


# Answer:

print(sorted([(v, k) for k, v in counts.items()], reverse=True))
