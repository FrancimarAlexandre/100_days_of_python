# EXEMPLO
print('exemplo')
i = 1
while i<6: # enquanto i for manor que 6 ele executa.
    print(i)
    i +=1

# BREAK
print("break")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i +=1

# CONTINUE
print('continue')
i = 1
while i < 6:
    i +=1
    if i == 3:
        continue
    print(i)

# ELSE
print('else')
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i não é mais inferior a 6")