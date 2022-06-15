#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <string>

using namespace std;

string temat, nick;
string tresc[100];
string odpA[100], odpB[100], odpC[100], odpD[100];
string poprawna[100];
string odpowiedz;
float punkty=0;
string deszyfrujCezar(int klucz, string tekst)
{
    char kod;
    int dl = tekst.length();
    string jawny = "";

    for (int i=0; i<dl; i++)
    {
    	if(toupper(tekst[i])>='A' && toupper(tekst[i])<='Z'){
    		if (tekst[i] == ' ') kod = ' ';
        else
        {
            kod = tekst[i] - klucz;
            if (kod<'A') kod = kod + 26;
        }
        jawny = jawny + kod;
		}
		else{
			jawny = jawny + tekst[i];
		}
        
    }
    return jawny;
}
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
    int nr_linii=1;
    string linia;
    int nr_pytania=0;
	char in[100];
	char out[100];
	char out1[100];
	cout<<"Podaj nazwe pliku z zaszyfrowanym quizem z rozszezeniem .txt\n";
	cin>>in;
	
//	char a[10]  = "quiz.txt";
//    ifstream wejscie(in);
//    ofstream wyjscie(out);
    fstream plik;
    plik.open(in,ios::in);
    int klucz;
    cout<<"Podaj klucz w jakim zaszyfrowany zostal quiz\n";
    cin>>klucz;

    if (plik.good()==false)
    {
        cout<<"Nie udalo sie otworzyc pliku!";
        exit(0);
    }
	
    while(getline(plik,linia))
    {
    	linia = deszyfrujCezar(klucz,linia);
        switch(nr_linii)
        {
            case 1: temat=linia;                     break;
            case 2: nick=linia;                      break;
            case 3: tresc[nr_pytania] = linia;       break;
            case 4: odpA[nr_pytania] = linia;        break;
            case 5: odpB[nr_pytania] = linia;        break;
            case 6: odpC[nr_pytania] = linia;        break;
            case 7: odpD[nr_pytania] = linia;        break;
            case 8: poprawna[nr_pytania] = linia;    break;
        }

        if (nr_linii==8) {nr_linii=2; nr_pytania++;}
        nr_linii++;
    }
//	cout<<nr_pytania<<"\n";
    plik.close();

    for (int i=0; i<=nr_pytania-1; i++)
    {
        cout<<endl<<tresc[i]<<endl;
        cout<<"A. "<<odpA[i]<<endl;
        cout<<"B. "<<odpB[i]<<endl;
        cout<<"C. "<<odpC[i]<<endl;
        cout<<"D. "<<odpD[i]<<endl;

        cout<<"Twoja odpowiedz: ";
        cin>>odpowiedz;

        transform(odpowiedz.begin(), odpowiedz.end(), odpowiedz.begin(), ::toupper);

        if (odpowiedz==poprawna[i])
        {
            cout<<"Dobrze! Zdobywasz punkt!"<<endl;
            punkty++;
        }
        else cout<<"Zle! Brak punktu! Poprawna odpowiedz: "<<poprawna[i]<<endl;

    }
	float max = nr_pytania;
//	cout<<nr_pytania;
    cout<<"Temat quizu: "<<temat<<" Nick: "<<nick<<" Zdobyte punkty: "<<punkty<<" na "<<nr_pytania<<" mozliwych, procentowy wynik: "<<punkty/max<<" %. \n";
	
	
	cout<<"Podaj nazwe pliku, do ktorego ma zostac zapisany niezaszyfrowany wynik quizu z rozszezeniem .txt\n";
	cin>>out;
	ofstream wyjscie1(out);
	
	wyjscie1<<"Temat quizu: "<<temat<<" Nick: "<<nick<<" Zdobyte punkty: "<<punkty<<" Maksymalna liczba zdobytych punktow: "<<nr_pytania<<" , procentowy wynik: "<<punkty/max<<" %. \n";
    wyjscie1.close();
    cout << "Plik o podanej nazwie zostal utworzony\n";
    
    ifstream wejscie(out);
    cout<<"Podaj nazwe pliku, do ktorego ma zostac zapisany zaszyfrowany wynik quizu z rozszezeniem .txt\n";
	cin>>out1;
    ofstream wyjscie(out1);

    string s;
    int klucz1;

    cout << "Podaj klucz w jakim zaszfrowany ma byc plik z wynikami: ";
    cin >> klucz1;

    while(!wejscie.eof())
    {
        getline(wejscie, s);
        wyjscie << Cezar(s, klucz1) << endl;
    }

    wejscie.close();
    wyjscie.close();
    cout << "Plik o podanej nazwie zostal utworzony.";
	return 0;
}
