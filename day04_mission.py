# 8.1

e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)

# 8.2

print({e2f['walrus']})

# 8.3
f2e = {}
for k, v in e2f.items():
    f2e[v] = k
print(f2e)

# 8.4
print({f2e['chien']})

#8.5
for k in e2f.keys():
    print(k)

