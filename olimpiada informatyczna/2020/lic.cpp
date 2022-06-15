#include<iostream>
#include<cmath>
using namespace std;
int main(){
	long int dlugosc_wyswietlacza, liczba_operacji;
	cin>>dlugosc_wyswietlacza>>liczba_operacji;
	long int dlug_1, dlug_2;
	cin>>dlug_1>>dlug_2;
	long int suma = dlug_1+dlug_2;
	while(liczba_operacji--){
		char typ_operacji;
		cin>>typ_operacji;
		if (typ_operacji=='W'){
			long int numer_liczby = 0;
			cin>>numer_liczby;
			long int nowa_liczba = 0;
			cin>>nowa_liczba;
			long int x;
			long int pom = pow(10,numer_liczby);
			long int pom1 = pow(10,numer_liczby-1);
			//long int pom2 = pow(10,numer_liczby-2);
			x = ((dlug_1)%pom)/pom1;
			dlug_1 -= x*pom1;
			dlug_1 += nowa_liczba * pom1;
			/*cout<<"pom"<<"\n";
			cout<<pom<<"\n";
			cout<<"pom1"<<"\n";
			cout<<pom1<<"\n";
			cout<<"x"<<"\n";
			cout<<x<<"\n";
			cout<<"po zmianie"<<"\n";*/
			//cout<<dlug_1<<"\n";
		}
		else if (typ_operacji=='Z'){
			long int numer_liczby = 0;
			cin>>numer_liczby;
			long int nowa_liczba = 0;
			cin>>nowa_liczba;
			long int x;
			long int pom = pow(10,numer_liczby);
			long int pom1 = pow(10,numer_liczby-1);
			x = ((dlug_2)%pom)/pom1;
			dlug_2 -= x*pom1;
			dlug_2 += nowa_liczba * pom1;
			//cout<<"po zmianie"<<"\n";
			//cout<<dlug_2<<"\n";
		}
		else if (typ_operacji=='S'){
			long int numer_liczby = 0;
			cin>>numer_liczby;
			long int x;
			//x = ((dlug_1+dlug_2)%pow(10, numer_liczby))/pow(10,numer_liczby-1)
			long int pom = pow(10,numer_liczby);
			long int pom1 = pow(10,numer_liczby-1);
			x = ((dlug_1+dlug_2)%pom)/pom1;
			cout<<x<<"\n";
		}
		//cout<<typ_operacji;
	}
	//int s = 2;
	//cout<<pow(10,s);
	//system("pause");
	return 0;
}

