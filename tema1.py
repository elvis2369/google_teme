teren=[[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]
nr_mutari=1
teren[1].pop(0)
teren[1].insert(0,'x')
while nr_mutari<=9:
       nr_x=teren.count("x")
       nr_o=teren.count("o")
       if nr_o == nr_x:
              poz_teren=input("introduceti linia din matrice pt inserare")
              punct=input("introduceti pozitia pe grila de inserat pt X")
              teren[poz_teren].pop(punct)
              teren[poz_teren].insert(punct,'x')
       else:
              poz_teren = input("introduceti linia din matrice pt inserare")
              punct = input("introduceti pozitia pe grila de inserat pt O")
              teren[poz_teren].pop(punct)
              teren[poz_teren].insert(punct, 'o')
       if teren[0][0] == "x" and teren[0][1] == 'x' and teren[0][2] == 'x':
              print("a castigat player 1 cu x")
              break
       elif



print(teren)