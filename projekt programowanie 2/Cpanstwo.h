#pragma once
#include "Cwioska.h"
#include "Cmiasto.h"
#include "Cgmina.h"
class Cpanstwo
{
public:
	Cpanstwo();
	~Cpanstwo();
	void pokaz()const;
	void wyswietl_pop_wieksza_od1(int pop = 25000) const;
private:
	int liczba_gmin;
	int liczba_miast;
	Cmiasto* miasta;
	Cgmina** gminy;
};

