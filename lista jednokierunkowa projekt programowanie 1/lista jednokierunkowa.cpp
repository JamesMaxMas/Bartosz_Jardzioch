//Bartosz Jardzioch  2022/23
#include <iostream>
#include <string>
#include <cstdlib>
#include <stdio.h>
#include <fstream>
#include <algorithm>
using namespace std;

struct osoba {
    string imie;
    string nazwisko;
    int wiek;
    osoba* nastepna;
};

void dodaj_osobe1(osoba* pierwsza_osoba, string imie, string nazwisko, int wiek)
{
    osoba* os = new osoba;
    
    os->imie = imie;
    os->nazwisko = nazwisko;
    os->wiek = wiek;
    os->nastepna = 0;
    if (pierwsza_osoba->nastepna == 0) {
        pierwsza_osoba->nastepna = os;
    }
    else {
        osoba* pom = pierwsza_osoba;
        while (pom->nastepna != 0)
        {
            pom = pom->nastepna;
        }
        pom->nastepna = os;
    }


}
void dodaj_osobe(osoba* pierwsza_osoba) {
    string imie;
    string nazwisko;
    int wiek;
    cout << "podaj imie\n";
    cin >> imie;
    cout << "podaj nazwisko\n";
    cin >> nazwisko;
    cout << "podaj wiek\n";
    cin >> wiek;
    dodaj_osobe1(pierwsza_osoba, imie, nazwisko, wiek);
}

void wyswietl_liste(osoba* pierwsza_osoba)
{
    int licz = 1;
    if (pierwsza_osoba->nastepna == 0) {
        cout << "lista jest pusta\n";
    }
    
    else {
        osoba* pom = pierwsza_osoba;
        do
        {
            cout << "----------------nr: " << licz << "--------------\n";
            pom = pom->nastepna;
            cout << "imie: " << pom->imie;
            cout << "\nnazwisko: " << pom->nazwisko;
            cout << "\nwiek: " << pom->wiek << "\n";
            licz++;

        } while (pom->nastepna != 0);
    }


}
void usun_osobe_nr1(osoba* pierwsza_osoba, int nr)
{
    
    osoba* pomprzed = pierwsza_osoba;
    for (int i = 0; i < (nr - 1); i++) {
        if (pomprzed->nastepna == 0) {
            cout << "nie ma tego numeru\n";
            break;
        }
        pomprzed = pomprzed->nastepna;
    }
    if (pomprzed->nastepna != 0) {
        osoba* pom = pomprzed->nastepna->nastepna;
        delete pomprzed->nastepna;
        pomprzed->nastepna = pom;
    }
    
    ;
}
void usun_osobe_nr(osoba* pierwsza_osoba) {
    int nr;
    cout << "podaj numer w liscie\n";
    cin >> nr;
    usun_osobe_nr1(pierwsza_osoba, nr);
}
void dodaj_osobe_nr_1(osoba* pierwsza_osoba, string imie, string nazwisko, int wiek, int nr)
{

    
    osoba* os = new osoba;

    os->imie = imie;
    os->nazwisko = nazwisko;
    os->wiek = wiek;
    osoba* pomprzed = pierwsza_osoba;
    for (int i = 0; i < (nr - 1); i++) {
        if (pomprzed->nastepna == 0) {
            cout << "nie ma tego numeru\n";
            delete os;
            break;
        }
        pomprzed = pomprzed->nastepna;
    }
    if (pomprzed->nastepna != 0) {
        cout << "xxxxxxxxxx";
        os->nastepna = pomprzed->nastepna;
        pomprzed->nastepna = os;
        /*cout << pomprzed->nastepna->imie;
        cout << pomprzed->imie;
        cout << os->nastepna->imie;*/

    }
    else {
        cout << "2";
        os->nastepna = 0;
        pomprzed->nastepna = os;
    }

}
void dodaj_osobe_nr(osoba* pierwsza_osoba) {
    int nr;
    cout << "podaj numer w liscie\n";
    cin >> nr;
    string imie;
    string nazwisko;
    int wiek;
    cout << "podaj imie\n";
    cin >> imie;
    cout << "podaj nazwisko\n";
    cin >> nazwisko;
    cout << "podaj wiek\n";
    cin >> wiek;
    dodaj_osobe_nr_1(pierwsza_osoba, imie, nazwisko, wiek, nr);
}
void zapisz(osoba* pierwsza_osoba) {
    char out[100];
    cout << "Podaj nazwe pliku, do ktorego ma zostac zapisana lista z rozszezeniem .txt\n";
    cin >> out;
    ofstream wyjscie1(out);
    if (pierwsza_osoba->nastepna == 0) {
        cout << "lista jest pusta\n";
    }

    else {
        osoba* pom = pierwsza_osoba;
        do
        {
            pom = pom->nastepna;
            wyjscie1 << pom->imie;
            cout << pom->imie<<"----------------------------";
            wyjscie1 << "\n" << pom->nazwisko;
            wyjscie1 << "\n" << pom->wiek << "\n";

        } while (pom->nastepna != 0);
    }
    wyjscie1.close();
}
void wczytaj(osoba* pierwsza_osoba) {
    while (pierwsza_osoba->nastepna != 0) {
        usun_osobe_nr1(pierwsza_osoba, 1);
    }
    char in[100];
    cout << "Podaj nazwe pliku z lista z rozszezeniem .txt\n";
    cin >> in;
    fstream plik;
    plik.open(in, ios::in);
    if (plik.good() == false)
    {
        cout << "Nie udalo sie otworzyc pliku!";
        exit(0);
    }
    string linia;
    int nr_linii = 1;
    string imie;
    string nazwisko;
    int wiek;
    while (getline(plik, linia))
    {
        switch (nr_linii)
        {
        case 1: imie = linia;                     break;
        case 2: nazwisko = linia;                      break;
        case 3: wiek = stoi(linia);       break;
        
        }

        if (nr_linii == 3) {
            nr_linii = 0;
            dodaj_osobe1(pierwsza_osoba, imie, nazwisko, wiek);
        }
        nr_linii++;
    }
    plik.close();
}
int main()
{

    osoba* pierwsza_osoba = new osoba;
    pierwsza_osoba->imie = "none";
    pierwsza_osoba->nazwisko = "x";
    pierwsza_osoba->wiek = 0;
    pierwsza_osoba->nastepna = 0;
    //	cout<<pierwsza_osoba;
    int b = 1;
    while (b != 0) {

        cout << "menu:\n";
        cout << "1-dodaj osobe na koniec listy\n";
        cout << "2-dodaj osobe na mijsce nr\n";
        cout << "3-usun osobe\n";
        cout << "4-wyswietl liste\n";
        cout << "5-zapisz\n";
        cout << "6-wczytaj\n";
        cout << "0-zakoncz\n";
        cin >> b;

        if (b == 1)dodaj_osobe(pierwsza_osoba);
        else if (b == 2)dodaj_osobe_nr(pierwsza_osoba);
        else if (b == 3)usun_osobe_nr(pierwsza_osoba);
        else if (b == 4)wyswietl_liste(pierwsza_osoba);
        else if (b == 5)zapisz(pierwsza_osoba);
        else if (b == 6)wczytaj(pierwsza_osoba);

        //		cout<<"jestem2";
    }

    return 0;
}
