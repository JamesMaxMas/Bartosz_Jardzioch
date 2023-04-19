#pragma once
import <string>;
class Cmiasto {
public:
	Cmiasto();
	Cmiasto(const Cmiasto&);
	void pokaz() const;
	int get_pop() const;

private:
	int rok_zalozenia;
	int liczba_ludnosci;
	std::string nazwa;
};
void stworz(Cmiasto*& miasta, const int rozmiar);
void usun(Cmiasto*& miasta, const int rozmiar);
void gen_data(Cmiasto& miasto, int ind);
//void ini(Cmiasto* const miasta, const int rozmiar);
void print(Cmiasto* miasta, const int rozmiar);
void dodaj(Cmiasto*& miasta, int& size);
void usun(Cmiasto*& miasta, int& size, int index);
void wyswietl_pop_wieksza_od(Cmiasto* miasta, const int rozmiar, int pop);
