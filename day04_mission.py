# 7.8

surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)

# 7.9

surprise[-1] = surprise[-1].lower()
print(surprise)

harpo_list = list(surprise[-1])
print(harpo_list)

harpo_list.reverse()
print(harpo_list)

harpo_list[0] = harpo_list[0].title()
print(harpo_list)

print(''.join(harpo_list))

surprise[-1] = ''.join(harpo_list)
print(surprise)