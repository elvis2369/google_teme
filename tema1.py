teren=[[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]
nr_o=0
nr_x=0
nr_mutari=0
while nr_mutari<=9:
       if nr_o >= nr_x:
              poz_teren=input("introduceti linia din matrice pt inserare")
              punct=input("introduceti pozitia pe grila de inserat pt X")
              teren[int(poz_teren)].pop(int(punct))
              #teren[
              teren[int(poz_teren)].insert(int(punct),'x')
              nr_x+=1
              print(teren)
       else:
              poz_teren = input("introduceti linia din matrice pt inserare")
              punct = input("introduceti pozitia pe grila de inserat pt O")
              teren[int(poz_teren)].pop(int(punct))
              teren[int(poz_teren)].insert(int(punct), 'o')
              print(teren)
              nr_o+=1
       if teren[0][0] == "x" and teren[0][1] == 'x' and teren[0][2] == 'x':#3 pe aceeasi linie prima
              print("a castigat player 1 cu x")
              break
       elif teren[0][0] == "x" and teren[1][0] == 'x' and teren[2][0] == 'x':#3 pe prima coloana
              print("a castigat player 1 cu x")
              break
       elif teren[0][0] == "x" and teren[1][1] == 'x' and teren[2][2] == 'x':#3 pe diag principala
              print("a castigat player 1 cu x")
              break
       elif teren[0][2] == "x" and teren[1][2] == 'x' and teren[2][2] == 'x':#3 pe ultima coloana
              print("a castigat player 1 cu x")
              break
       elif teren[0][1] == "x" and teren[1][1] == 'x' and teren[2][1] == 'x':#3 pe col de mijloc
              print("a castigat player 1 cu x")
              break
       elif teren[0][2] == "x" and teren[1][2] == 'x' and teren[2][2] == 'x':#3 pe ultima col
              print("a castigat player 1 cu x")
              break
       elif teren[2][0] == "x" and teren[1][1] == 'x' and teren[0][2] == 'x':#3 pe diag secundara
              print("a castigat player 1 cu x")
              break
       elif teren[1][0] == "x" and teren[1][1] == 'x' and teren[1][2] == 'x':#3 pe aceeasi linie din mijloc
              print("a castigat player 1 cu x")
              break
       elif teren[2][0] == "x" and teren[2][1] == 'x' and teren[2][2] == 'x':#3 pe ultima linie de jos
              print("a castigat player 1 cu x")
              break
       else:
              if teren[0][0] == "o" and teren[0][1] == 'o' and teren[0][2] == 'o':  # 3 pe aceeasi linie prima
                     print("a castigat player 1 cu o")
                     break
              elif teren[0][0] == "o" and teren[1][0] == 'o' and teren[2][0] == 'o':  # 3 pe prima coloana
                     print("a castigat player 1 cu o")
                     break
              elif teren[0][0] == "o" and teren[1][1] == 'o' and teren[2][2] == 'o':  # 3 pe diag principala
                     print("a castigat player 1 cu o")
                     break
              elif teren[0][2] == "o" and teren[1][2] == 'o' and teren[2][2] == 'o':  # 3 pe ultima coloana
                     print("a castigat player 1 cu o")
                     break
              elif teren[0][1] == "o" and teren[1][1] == 'o' and teren[2][1] == 'o':  # 3 pe col de mijloc
                     print("a castigat player 1 cu o")
                     break
              elif teren[0][2] == "o" and teren[1][2] == 'o' and teren[2][2] == 'o':  # 3 pe ultima col
                     print("a castigat player 1 cu o")
                     break
              elif teren[2][0] == "o" and teren[1][1] == 'o' and teren[0][2] == 'o':  # 3 pe diag secundara
                     print("a castigat player 1 cu o")
                     break
              elif teren[1][0] == "o" and teren[1][1] == 'o' and teren[1][2] == 'o':  # 3 pe aceeasi linie din mijloc
                     print("a castigat player 1 cu o")
                     break
              elif teren[2][0] == "o" and teren[2][1] == 'o' and teren[2][2] == 'o':  # 3 pe ultima linie de jos
                     print("a castigat player 1 cu o")
                     break
       nr_mutari+=1
print(teren)