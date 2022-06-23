zdania = ['Dzien dobry', 'Zycze milego dzionka','pozdrawiam']
with open('zadanie5tekst.txt', 'w') as f:

    for line in zdania:
        f.write(line)
        f.write('\n')
with open('zadanie5tekst.txt', 'r') as c:
    t=c.read()
    print(t)