#include "Cgmina.h"
#include "Cwioska.h"
//import <random>;
import <ctype.h>;
import <iostream>;
Cgmina::Cgmina(int n) : numer(n) {
    rozmiar = gen_int_pomiedzy(2, 8);
    wioski = new Cwioska * [rozmiar];
    for (size_t ind = 0; ind < rozmiar; ind++)
        wioski[ind] = new Cwioska;
 }
Cgmina::~Cgmina() {
    for (size_t ind = 0; ind < rozmiar; ind++)
        delete wioski[ind];
    delete[] wioski;
    wioski = nullptr;
    rozmiar = 0;
}
Cgmina::Cgmina(const Cgmina& gmina, int n) : numer(n) {
    rozmiar = gmina.rozmiar;
    wioski = new Cwioska * [rozmiar];
    for (size_t ind = 0; ind < rozmiar; ind++)
        wioski[ind] = new Cwioska(*gmina.wioski[ind]);
}
void Cgmina::pokaz() const {
    std::cout << "<========== Wioski ==========>" << std::endl;
    std::cout << "<rok\tnazwa\t\tpop>" << std::endl;
    for (size_t ind = 0; ind < rozmiar; ind++) {
        /*std::cout << wioski[ind]->rok_zalozenia << "\t" << wioski[ind]->nazwa << "\t"
            << wioski[ind]->liczba_ludnosci << std::endl;*/
        wioski[ind]->pokaz();
    }
}
void Cgmina::dodaj_losowa_wioske()  {
    Cwioska** temp = new Cwioska * [rozmiar + 1];
    if (rozmiar == 0) {
        temp[rozmiar] = new Cwioska;
    }
    else {
        for (size_t i = 0; i < rozmiar; ++i)
            temp[i] = wioski[i];
        temp[rozmiar] = new Cwioska;
        delete[] wioski;
    }
    wioski = temp;
    ++rozmiar;
}
void Cgmina::usun_ostatnia_wioske() {
    int index = gen_int_pomiedzy(0, rozmiar-1);
    Cwioska** temp = new Cwioska * [rozmiar + 1];
    if (rozmiar == 0) {
        temp[rozmiar] = new Cwioska;
    }
    else {
        for (size_t i = 0; i < rozmiar; ++i)
            temp[i] = wioski[i];
        temp[rozmiar] = new Cwioska;
        delete[] wioski;
    }
    wioski = temp;
    ++rozmiar;
}

void Cgmina::dodaj_wlasna_wioske1() {
    Cwioska** temp = new Cwioska * [rozmiar + 1];
    if (rozmiar == 0) {
        temp[rozmiar] = new Cwioska;
        temp[rozmiar]->gen_data_wlasne();
    }
    else {
        for (size_t i = 0; i < rozmiar; ++i)
            temp[i] = wioski[i];
        temp[rozmiar] = new Cwioska;
        temp[rozmiar]->gen_data_wlasne();
        delete[] wioski;
    }
    wioski = temp;
    ++rozmiar;
}
void Cgmina::wyswietl_rok_mniejszy_od1(int rok) const {
        std::cout << "<========== Wioski zalozone przed " << rok << " ==========>" << std::endl;
        std::cout << "<rok\tnazwa\t\tpop>" << std::endl;
        for (size_t ind = 0; ind < rozmiar; ind++) {
            if (wioski[ind]->get_rok() < rok)
                wioski[ind]->pokaz();
        }
}
void Cgmina::stworz_wioski() {
    wioski = new Cwioska * [rozmiar];
    for (size_t ind = 0; ind < rozmiar; ind++)
        wioski[ind] = new Cwioska;
}
Cgmina::Cwioska::Cwioska() {
    liczba_ludnosci = gen_int_pomiedzy(1, 3000);
    rok_zalozenia = gen_int_pomiedzy(1000, 2000);
    nazwa = "Wioska_nr_" + std::to_string(gen_int_pomiedzy(1, 2000));
}
void Cgmina::Cwioska::gen_data_wlasne() {
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // zignoruj wszystkie znaki w buforze a¿ do znaku nowej linii
    while (true) {
        std::cout << "Podaj nazwe wioski , rok zalozenia i populacje oddzielone spacja: ";
        std::string s = "";

        std::getline(std::cin, s);
        s.append(" ");
        int j = 0;
        size_t pos = 0;
        std::string token[3] = { "" };
        while ((pos = s.find_first_of(' ')) != std::string::npos and j < 3) {
            token[j] = s.substr(0, pos);
            j++;
            s.erase(0, pos + 1);
        }
        bool ok = true;
        std::cout << token[0] << token[1] << token[2] << "\n";
        for (auto c : token[2]) {
            if (not std::isdigit(c)) {
                ok = false;
            }
        }

        for (auto c : token[1]) {
            if (not std::isdigit(c)) {
                ok = false;
            }
        }
        if (token[0] == "" or token[1] == "" or token[2] == "")ok = false;
        int i, i1;
        if (ok) {
            i = std::stoi(token[2]);
            liczba_ludnosci = i;
            i1 = std::stoi(token[1]);
            rok_zalozenia = i1;
            nazwa = token[0];
            break;
        }
        else {
            std::cout << "Wprowadzono nieprawidlowe dane\n";
        }
    }
}
void Cgmina::Cwioska::pokaz() const {
    std::cout << rok_zalozenia << "\t" << nazwa << "\t"
        << liczba_ludnosci << std::endl;
}
void stworz(Cgmina**& gminy, const int rozmiar) {
    gminy = new Cgmina * [rozmiar];
    for (int ind = 0; ind < rozmiar; ind++) {
        gminy[ind] = new Cgmina{ind};
    }   
}

void print(Cgmina* gmina) {
    gmina->pokaz();
}
void print(Cgmina** gminy, const int rozmiar) {
    for (size_t ind = 0; ind < rozmiar; ind++) {
        std::cout << "<========== Gmina nr " << ind+1 << " ==========>\n";
        print(gminy[ind]);
    }
}
void usun(Cgmina*& gminy) {
    delete gminy;
    gminy = nullptr;
}
void usun(Cgmina**& gminy, int rozmiar) {
    for (size_t ind = 0; ind < rozmiar; ind++) {
        usun(gminy[ind]);
    }
    gminy = nullptr;
}
int Cgmina::Cwioska::get_rok() const {
    return rok_zalozenia;
}
