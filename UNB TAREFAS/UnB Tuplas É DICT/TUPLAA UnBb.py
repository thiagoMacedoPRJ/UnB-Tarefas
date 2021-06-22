c = int(input())
b = input()

a = []
for i in range(0,c):
    x = input()
    a += [x]

y = 0
k = b.replace(' ','')
b = "abcdefghijklmnopqrstuvwxyz-."
nm = "0123456789-."
t = True
while t:
    n = a[y].lower()
    for old in b:
        n = n.replace(' ','')
        n = n.replace(old,"")

    if n == k:
        print('deu bom!')
        j = a[y]
        for old in nm:
            j = j.replace(' ','')
            j = j.replace(old,"")
        print(j)
        t = False
    else:
        y = y + 1
        if y == len(a):
            print('não foi dessa vez /:')
            t = False
        else:
            pass

#print(a)
        
#TESTE DESTE EXEMPLO!     
'''
5
1 2 3 4 5 6
Paco-1 20 30 2 3 4
Luna-1 2 3 4 5 6
Batatinha-10 11 14 16 20 22
Sr. Bigode-14 20 44 90 99 92
Fifi-22 23 25 28 33 38
deu bom!
Luna
deu bom!
Luna
5
20 2 3 11 14 28
Paco-1 20 30 2 3 4
Luna-1 2 3 4 5 6
Batatinha-10 11 14 16 20 22
Sr. Bigode-14 20 44 90 99 92
Fifi-22 23 25 28 33 38
não foi dessa vez /:
não foi dessa vez /:
5
69 582 241 633 720 967
Banguela-274 302 896 926 178 226
Miau-783 822 13 172 927 282
Mandachuva-69 582 241 633 720 967
George-81 98 227 622 480 85
LindinhaDocinho-92 725 294 14 803 355
deu bom!
Mandachuva
deu bom!
Mandachuva

10
799 610 889 39 777 591
Cegonha-121 826 587 65 214 256
Banana-591 363 975 535 235 508
Luna-974 996 877 885 493 777
Fifi-884 690 433 523 242 338
Frajola-696 622 367 90 924 245
Batatinha-85 25 610 423 760 660
Gatinho-379 889 839 996 854 86
Criss-336 358 488 60 39 749
George-799 717 219 475 830 384
Khali-799 619 12 23 44 88

não foi dessa vez /:
não foi dessa vez /:


10# Começa daqui
694 230 736 453 164 935
Shawn-620 373 619 97 866 188
Bruna-953 952 305 811 155 790
Bob-814 838 33 807 443 255
Felix-44 805 463 990 779 753
Lary-357 36 882 734 624 861
LindinhaDocinho-847 402 620 958 302 598
George-495 886 629 51 52 765
Ceguinho-274 495 847 325 880 278
Gatinho-740 832 107 761 364 730
Luna-694 230 736 453 164 935

#Resultado
deu bom!
Luna
deu bom!
Luna


20 # Começa daqui
713 343 775 874 495 536
Miado-571 408 624 864 727 542
Mandachuva-191 592 576 166 658 987
Cegonha-224 872 509 293 389 942
Banana-444 989 164 977 731 230
Buni-178 120 742 844 837 882
Fifi-713 343 775 874 495 536
Gatinho-634 135 448 660 622 747
Bolo-384 462 322 30 843 724
Morango-217 918 194 898 675 597
Dune-167 654 401 385 63 770
Miau-755 784 365 780 84 697
Bruna-700 825 289 132 785 1000
Felix-118 412 244 223 491 645
Gary-500 162 187 387 511 344
Sr. Bigodes-145 391 798 654 707 367
Guerreira-37 773 426 270 588 998
Helix-709 836 305 567 778 340
Lary-31 95 87 199 426 194
Bichano-367 511 340 847 626 988
Toothless-488 578 657 216 521 201

#Resultado
deu bom!
Fifi
deu bom!
Fifi

'''