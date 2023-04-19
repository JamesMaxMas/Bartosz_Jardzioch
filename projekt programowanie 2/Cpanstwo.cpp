#include "Cpanstwo.h"
#include "Cwioska.h"
#include "Cmiasto.h"
#include "Cgmina.h"
Cpanstwo::Cpanstwo() {
    liczba_miast = gen_int_pomiedzy(5, 8);
    liczba_gmin = gen_int_pomiedzy(5, 8);
    stworz(gminy, liczba_gmin);
    stworz(miasta, liczba_miast);
}
Cpanstwo::~Cpanstwo() {
    usun(gminy, liczba_gmin);
    usun(miasta, liczba_miast);
}

void Cpanstwo::pokaz()const{
    print(gminy,liczba_gmin);
    print(miasta, liczba_miast);
}
void Cpanstwo::wyswietl_pop_wieksza_od1(int pop )const {
    wyswietl_pop_wieksza_od(miasta, liczba_miast, pop);
}
