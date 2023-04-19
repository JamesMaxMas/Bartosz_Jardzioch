// Lab1.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//

// Lab2:
// generowanie liczb losowych, agregacja, 
// zarzadzanie tablica obiektow wewnatrz struktury #agregacja
// wprowadzanie danych jednego obiektu za pomoca funkcji getline wszystko w jednej linijce
// sprawdzenie poprzez ctype #string
// użycie losowosci jak w przykladzie
// 3
// jedna wybrana strukture agreguje podwujny wskaznik, przerobic na klase, zdefiniować konstruktor, destruktor i zademonstrować użycie listy inicjalizacyjnej w konteksscie pola stałego klasy.
//lab4
//klasa zagniezdzona, konstruktor kopiujacy, przyjazn klasy zagnieżdonej z klasą bazową.
// 
//
#include "Cwioska.h"
#include "Cmiasto.h"
#include "Cgmina.h"
#include "Cpanstwo.h"
import <iostream>;
//import <string>;
//import<cstdlib>;   // nie używamy <cstdio>, ponieważ ta biblioteka zawiera <cstdio>, srand(), rand()
//import <locale>;
//import <random>;





void lab3() {
	int n = 0;
	Cgmina* G1{ nullptr };
	Cpanstwo* P1{ nullptr };
	while (n != 13) {
		std::cout << "Podaj liczbe od 1 do 6 lub 13\n1-6:operacje na wioskach w gminie\n1-stworz\n2-wyswietl\n3-wyswietl wioski zalozone przed 1500\n4-dodaj\n5-usun losowe\n6-dodaj wlasne dane\n\n9-stworz panstwo\n10-wyswietl panstwo\n11-wyswietl wszystkie miasta i wioski w pansktwie\n12-stworz gmine o stalym numerze 49\n13-koniec\n\n";
		std::cin >> n;
		if (n == 1) {
			G1 = new Cgmina;
			std::cout << "zrobione\n";
		}
		else if (n == 2) {
			if (G1 != nullptr) {
				G1->pokaz();
				std::cout << "zrobione\n";
			}
			else std::cout << "tablica nie stworzona\n";
		}
		else if (n == 3) {
			if (G1 != nullptr) {
				G1->wyswietl_rok_mniejszy_od1();
				std::cout << "zrobione\n";
			}
			else std::cout << "tablica nie stworzona\n";
		}
		else if (n == 4) {
			if (G1 != nullptr) {
				G1->dodaj_losowa_wioske();
				std::cout << "zrobione\n";
			}
			else std::cout << "tablica nie stworzona\n";
		}
		else if (n == 5) {
			if (G1 != nullptr) {
				G1->usun_ostatnia_wioske();
				std::cout << "zrobione\n";

			}
			else std::cout << "tablica nie stworzona\n";
		}
		else if (n == 6) {
			G1->dodaj_wlasna_wioske1();
			std::cout << "zrobione\n";
		}
		else if (n == 9) {
			//stworz(P1);
			P1 = new Cpanstwo;
			std::cout << "zrobione\n";
		}
		else if (n == 10) {
			P1->pokaz();
			//print(P1);
			//print(P1->miasta, P1->liczba_miast);
			std::cout << "zrobione\n";
		}
		else if (n == 11) {
			P1->wyswietl_pop_wieksza_od1();
			//print(P1);
			//print(P1->miasta, P1->liczba_miast);
			std::cout << "zrobione\n";
		}
		else if (n == 12) {
			Cgmina G2{ 49 };
			std::cout << G2.get_numer() << "\n";
			std::cout << "zrobione\n";
		}
		else if (n == 13) {
			if (G1 != nullptr) {
				G1->~Cgmina();
				G1 = nullptr;
			}
			if (P1 != nullptr) {
				P1->~Cpanstwo();
				P1 = nullptr;
			}
			std::cout << "zrobione\n";
		}
		else {
			std::cout << "wprowadzono nieprawidlowa liczbe\n";
		}
		std::cout << "\n\n";
		//system("CLS");
	}

	if (G1 != nullptr) G1->~Cgmina();
	if (P1 != nullptr) P1->~Cpanstwo();;
	std::cout << "usunieto pamiec!\n";
}
int main()
{
	lab3();



}

// Uruchomienie programu: Ctrl + F5 lub menu Debugowanie > Uruchom bez debugowania
// Debugowanie programu: F5 lub menu Debugowanie > Rozpocznij debugowanie

// Porady dotyczące rozpoczynania pracy:
//   1. Użyj okna Eksploratora rozwiązań, aby dodać pliki i zarządzać nimi
//   2. Użyj okna programu Team Explorer, aby nawiązać połączenie z kontrolą źródła
//   3. Użyj okna Dane wyjściowe, aby sprawdzić dane wyjściowe kompilacji i inne komunikaty
//   4. Użyj okna Lista błędów, aby zobaczyć błędy
//   5. Wybierz pozycję Projekt > Dodaj nowy element, aby utworzyć nowe pliki kodu, lub wybierz pozycję Projekt > Dodaj istniejący element, aby dodać istniejące pliku kodu do projektu
//   6. Aby w przyszłości ponownie otworzyć ten projekt, przejdź do pozycji Plik > Otwórz > Projekt i wybierz plik sln
