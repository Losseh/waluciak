#!/usr/bin/python


def rata(kapital, oprocentowanie_roczne, raty_na_rok, calk_liczba_rat):
    mnoznik = 0
    for i in xrange(calk_liczba_rat):
        procent_rata = (1 + oprocentowanie_roczne / float(raty_na_rok))**(-i)
        mnoznik = mnoznik + procent_rata

    return kapital / mnoznik

def licz_kredyt(kapital, wibor3m, marza, raty_na_rok, calk_liczba_rat):
    oprocentowanie_roczne = wibor3m + marza
    rata_miesieczna = rata(kapital, oprocentowanie_roczne, raty_na_rok, calk_liczba_rat)
    print '**********'
    print 'wibor3m: ' + str(100*wibor3m) + '%'
    print 'liczba rat: ' + str(calk_liczba_rat)
    print 'pozyczono: ' + str(kapital)
    print 'rata: ' + str(rata_miesieczna)
    print 'koszt kredytu: ' + str(rata_miesieczna*calk_liczba_rat - kapital)


lata_kredytu = [5]
wibor3m_dzisiaj = 0.0171
wibor3m = [wibor3m_dzisiaj, 2*wibor3m_dzisiaj]
kapital = 120000
marza = 0.02
raty_na_rok = 12

for wibor3m_i in wibor3m:
    for lata_kredytu_i in lata_kredytu:
        calk_liczba_rat = int(lata_kredytu_i * 12)
        licz_kredyt(kapital, wibor3m_i, marza, raty_na_rok, calk_liczba_rat)
