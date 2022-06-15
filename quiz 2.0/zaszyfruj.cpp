/*
Napisz program, ktory zaszyfruje szyfrem Cezara tekst wczytany z pliku tekstowego przekazanego przez nauczyciela (np. tekst_jawny_1.txt). Klucz powinien byc wiekszy od 0 i mniejszy od 26. Do obslugi plikow tekstowych (w szczegolnosci obejrzenia pliku wynikowego) mozesz uzyc systemowego notatnika.
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <algorithm>
using namespace std;

string Cezar(string s, int klucz)
{
    string szyfrogram = "";
    int kod;
    for(int i = 0; i < s.size(); i++)
    {
        if(toupper(s[i])>='A' && toupper(s[i])<='Z')
        {
            kod = s[i] + klucz;

            if ((s[i]<='Z' && kod>'Z') || (s[i]>='a' && kod>'z'))
                kod = kod - 26;

            szyfrogram = szyfrogram + char(kod);
        }
        else
            szyfrogram = szyfrogram + s[i];
    }
	
	transform(szyfrogram.begin(), szyfrogram.end(), szyfrogram.begin(), ::toupper);
    return szyfrogram;
}

int main()
{
	char in[100];
	char out[100];
	cout<<"Podaj nazwe pliku z quizem z rozszezeniem .txt\n";
	cin>>in;
	cout<<"Podaj nazwe pliku, do ktorego ma zostac zapisany zaszyfrowany quiz z rozszezeniem .txt\n";
	cin>>out;
//	char a[10]  = "quiz.txt";
    ifstream wejscie(in);
    ofstream wyjscie(out);
    

    string s;
    int klucz;

    cout << "Klucz: ";
    cin >> klucz;

    while(!wejscie.eof())
    {
        getline(wejscie, s);
//        cout<<s<<"\n";
        wyjscie << Cezar(s, klucz) << endl;
    }

    wejscie.close();
    wyjscie.close();

    cout << "Plik o podanej nazwie zostal utworzony";

    return 0;
}

