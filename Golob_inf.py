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
import random
lodg = []
lpit = []
red = []
lbr = []
lpon = []
ln = []
odg = ''
to = no = x = r = 0
print('Dobrodošli u flashcards-type igru za ponavljanje!\nUbacite popis/e pojmova u isti folder koji su s znakom - odvojeni od svoje definicije/značenja/itd. Svaki pojam mora biti u novom redu.')
ime = input('Naziv datoteke: ')
file = open(ime,'r')
lredovi = file.readlines()
for i in range(len(lredovi)):
        red = lredovi[i]
        a = red.split('-')
        lodg.append(a[0])
        lpit.append(a[1].replace('\n',''))
        lbr.append(i)
if len(lbr)>20:
        lpon = ['a','b','c','d','e','f','g','h',]
elif len(lbr)>10:
        lpon = ['a','b','c','d']
elif len(lbr)>5:
        lpon = ['a','b']
while 'KRAJ' not in odg:
        x = int(random.choice(lbr))
        print(lpit[x])
        odg = input()
        if odg in lodg[x] and odg not in 'KRAJ':
                to += 1
        elif odg not in lodg[x] and odg not in 'KRAJ':
                no += 1
                ln.append(x)
        lbr.remove(x)
        lpon.append(x)
        r = lpon.pop(0)
        if isinstance(r,int) == True:
                lbr.insert(r,r)
file.close
print('Točnih odgovora je bilo {}, a netočnih {}. Spremi igru (Y/N)?'.format(to,no))
s = input()
if s in 'Y':
        file = open(ime, 'a')
        file.write('\n')
        for i in range(len(ln)):
                sbr = ln[i]
                save = lodg[sbr] + '-' + lpit[sbr] + '\n'
                file.write(save)
file.close()
