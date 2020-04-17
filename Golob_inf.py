import random
lodg = lpit = red = br = a = []
odg = ''
t = n = x = 0
print('Dobrodošli u flashcards-type igru za ponavljanje!\nUbacite popis/e pojmova u isti folder koji su s znakom - odvojeni od svoje definicije/značenja/itd. Svaki pojam mora biti u novom redu.')
ime = input('Naziv datoteke: ')
lredovi = open(ime,'r').readlines()
for i in range(len(lredovi)):
        red = lredovi[i]
        a = red.split('-')
        lodg.append(a[0])
        lpit.append(a[1].replace('\n',''))
br = range(len(lpit))
while 'kraj' not in odg:
        x = int(random.choice(br))
        print(lpit[x])
        odg = input()
        if odg in lodg[x-1] and odg not in 'kraj':
                t += 1
        else:
                n += 1
print('Točnih odgovora je bilo {}, a netočnih {}. Spremi igru (Y/N)?'.format(t,n))
