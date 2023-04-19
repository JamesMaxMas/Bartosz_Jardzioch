#pragma once
//#include "Cwioska.h"
import <string>;
class Cgmina
{
    const int numer;
    int rozmiar;
    class Cwioska {
        friend class Cgmina;
    public:
        Cwioska();
        void gen_data_wlasne();
        void pokaz() const;
        int get_rok() const;
    private:
        int rok_zalozenia;
        int liczba_ludnosci;
        std::string nazwa;
    };
    Cwioska** wioski;
public:
    Cgmina(int n = 0);
    Cgmina(const Cgmina&, int n = 0);
    ~Cgmina();
    int get_numer() const { return numer; }
    void pokaz() const;
    void dodaj_losowa_wioske();
    void stworz_wioski();
    void pokaz_wioski();
    void usun_ostatnia_wioske();
    void dodaj_wlasna_wioske1();
    void wyswietl_rok_mniejszy_od1(int rok = 1500) const;
};
void stworz(Cgmina*&);
void usun(Cgmina*& gminy);
void usun(Cgmina**& gminy, int rozmiar);
int gen_int_pomiedzy(int begin, int end);
void stworz(Cgmina**& gminy, const int rozmiar);
void print(Cgmina** gminy, const int rozmiar);
void print(Cgmina* gmina);
