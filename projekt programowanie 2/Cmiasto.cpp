#include "Cmiasto.h"
#include "Cwioska.h"
import <iostream>;
import <string>;
//import<cstdlib>;   // nie u¿ywamy <cstdio>, poniewa¿ ta biblioteka zawiera <cstdio>, srand(), rand()
//import <locale>;
Cmiasto::Cmiasto(){
	liczba_ludnosci = gen_int_pomiedzy(20000, 30000);
	rok_zalozenia = gen_int_pomiedzy(100, 3000);
	nazwa = "Miasto_nr_" + std::to_string(gen_int_pomiedzy(1, 10000));
}
Cmiasto::Cmiasto(const Cmiasto& miasto) {
	liczba_ludnosci = miasto.liczba_ludnosci;
	rok_zalozenia = miasto.rok_zalozenia;
	nazwa = miasto.nazwa;
}
void Cmiasto::pokaz() const {
	std::cout << rok_zalozenia << "\t" << nazwa << "\t"
		<< liczba_ludnosci << std::endl;
}
int Cmiasto::get_pop() const {
	return liczba_ludnosci;
}
void stworz(Cmiasto*& miasta, const int rozmiar) {
	miasta = new Cmiasto[rozmiar];
}
void usun(Cmiasto*& miasta, const int rozmiar) {
	delete[] miasta;
	miasta = nullptr;
}
void print(Cmiasto* miasta, const int rozmiar) {
	std::cout << "<========= Miasta =========>" << std::endl;
	std::cout << "<rok\tnazwa\t\tpop>" << std::endl;
	for (size_t ind = 0; ind < rozmiar; ind++) {
		miasta[ind].pokaz();
	}
}
void dodaj(Cmiasto*& miasta, int& size) {
	Cmiasto* temp = new Cmiasto[size + 1];
	for (size_t i = 0; i < size; ++i)
		temp[i] = miasta[i];
	delete[] miasta;
	miasta = temp;
	++size;
}
void usun(Cmiasto*& miasta, int& size, int index) {
	if (index < size) {
		Cmiasto* temp = new Cmiasto[size - 1];
		short int j{ -1 };
		for (size_t i = 0; i < size; ++i)
			if (i != index) {
				++j;
				temp[j] = miasta[i];
			}
		delete[] miasta;
		miasta = temp;
		--size;
	}
	else
		std::cout << "ERROR: Index jest nieprawid³owy ! " << std::endl;
}

void wyswietl_pop_wieksza_od(Cmiasto* miasta, const int rozmiar, int pop) {
	std::cout << "<========= Miasta o populacji wiekszej od " << pop << " =========>" << std::endl;
	std::cout << "<rok\t nazwa\t\tpop>" << std::endl;
	for (size_t ind = 0; ind < rozmiar; ind++) {
		if (pop < miasta[ind].get_pop())
			miasta[ind].pokaz();
	}
}