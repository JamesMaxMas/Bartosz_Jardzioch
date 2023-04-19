#include "Cwioska.h"
//import <iostream>;
//import <ctype.h>;
import <random>;

int gen_int_pomiedzy(int begin, int end) {
	static std::random_device rd;
	static std::default_random_engine dfe(rd());
	std::uniform_int_distribution<int> rozmiar(begin, end);
	return rozmiar(dfe);
}
//Cwioska::Cwioska() {
//	liczba_ludnosci = gen_int_pomiedzy(1, 3000);
//	rok_zalozenia = gen_int_pomiedzy(1000, 2000);
//	nazwa = "Wioska_nr_" + std::to_string(gen_int_pomiedzy(1, 2000));
//}
//void Cwioska::pokaz() const {
//	std::cout << rok_zalozenia << "\t" << nazwa << "\t"
//		<< liczba_ludnosci << std::endl;
//}
//int Cwioska::get_rok() const {
//	return rok_zalozenia;
//}
//void Cwioska::gen_data_wlasne() {
//std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // zignoruj wszystkie znaki w buforze a¿ do znaku nowej linii
//	while (true) {
//		std::cout << "Podaj nazwe wioski , rok zalozenia i populacje oddzielone spacja: ";
//		std::string s = "";
//	
//		std::getline(std::cin, s);
//		s.append(" ");
//		int j = 0;
//		size_t pos = 0;
//		std::string token[3]={""};
//		while ((pos = s.find_first_of(' ')) != std::string::npos and j < 3) {
//			token[j] = s.substr(0, pos);
//			j++;
//			s.erase(0, pos + 1);
//		}
//		bool ok = true;
//		std::cout << token[0] << token[1] << token[2] << "\n";
//		for (auto c : token[2]) {
//			if (not std::isdigit(c)) {
//				ok = false;
//			}
//		}
//		
//		for (auto c : token[1]) {
//			if (not std::isdigit(c)) {
//				ok = false;
//			}
//		}
//		if (token[0] == "" or token[1] == "" or token[2] == "")ok = false;
//		int i, i1;
//		if (ok) {
//			i = std::stoi(token[2]);
//			liczba_ludnosci = i;
//			i1 = std::stoi(token[1]);
//			rok_zalozenia = i1;
//			nazwa = token[0];
//			break;
//		}
//		else {
//			std::cout << "Wprowadzono nieprawidlowe dane\n";
//		}
//	}
//}
//void stworz(Cwioska**& wioski, const int rozmiar) {
//	wioski = new Cwioska * [rozmiar];
//	for (size_t ind = 0; ind < rozmiar; ind++)
//		wioski[ind] = new Cwioska;
//}
//void usun(Cwioska**& wioski, int& rozmiar) {
//	for (size_t ind = 0; ind < rozmiar; ind++)
//		delete wioski[ind];
//	delete[] wioski;
//	wioski = nullptr;
//	rozmiar = 0;
//}
//void print(Cwioska** wioski, const int rozmiar) {
//	std::cout << "<========== Wioski ==========>" << std::endl;
//	std::cout << "<rok\tnazwa\t\tpop>" << std::endl;
//	for (size_t ind = 0; ind < rozmiar; ind++) {
//		/*std::cout << wioski[ind]->rok_zalozenia << "\t" << wioski[ind]->nazwa << "\t"
//			<< wioski[ind]->liczba_ludnosci << std::endl;*/
//		wioski[ind]->pokaz();
//	}
//}
//
//void dodaj_losowe(Cwioska**& wioski, int& size) {
//	Cwioska** temp = new Cwioska * [size + 1];
//	if (size == 0) {
//		temp[size] = new Cwioska;
//	}
//	else {
//		for (size_t i = 0; i < size; ++i)
//			temp[i] = wioski[i];
//		temp[size] = new Cwioska;
//		delete[] wioski;
//	}
//	wioski = temp;
//	++size;
//}
//void usun(Cwioska**& wioski, int& size, int index) {
//	if (index < size) {
//		Cwioska** temp = new Cwioska * [size - 1];
//		short int j{ -1 };
//		for (size_t i = 0; i < size; ++i)
//			if (i != index) {
//				++j;
//				temp[j] = wioski[i];
//			}
//		delete[] wioski;
//		wioski = temp;
//		--size;
//	}
//	else
//		std::cout << "ERROR: Index jest nieprawid³owy ! " << std::endl;
//}
//void wyswietl_rok_mniejszy_od(Cwioska** wioski, const int rozmiar, int rok) {
//	std::cout << "<========== Wioski zalozone przed " << rok << " ==========>" << std::endl;
//	std::cout << "<rok\tnazwa\t\tpop>" << std::endl;
//	for (size_t ind = 0; ind < rozmiar; ind++) {
//		if (wioski[ind]->get_rok() < rok)
//			wioski[ind]->pokaz();
//	}
//}
//void dodaj_wlasna_wioske(Cwioska**& wioski,  int &size){
//	Cwioska** temp = new Cwioska * [size + 1];
//	if (size == 0) {
//		temp[size] = new Cwioska;
//		temp[size]->gen_data_wlasne();
//	}
//	else {
//		for (size_t i = 0; i < size; ++i)
//			temp[i] = wioski[i];
//		temp[size] = new Cwioska;
//		temp[size]->gen_data_wlasne();
//		delete[] wioski;
//	}
//	wioski = temp;
//	++size;
//}