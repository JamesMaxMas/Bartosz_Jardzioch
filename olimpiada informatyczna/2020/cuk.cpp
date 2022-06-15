#include<iostream>
#include<cmath>
using namespace std;
int main(){
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	int n;
	cin>>n;
	int a,b,c;
	int p = n;
	int suma_a=0,suma_b=0, suma_c = 0;
	int liczba_pustych=0;
//	int liczba_z_tylko_a=0,liczba_z_najwiecej_b=0,liczba_z_tylko_c=0 ;
	int liczba_z_najwiecej_a=0,liczba_z_najwiecej_b=0,liczba_z_najwiecej_c=0 ;
	int liczba_a_do_przeniesienia=0,liczba_b_do_przeniesienia=0,liczba_c_do_przeniesienia=0;
	//int liczba_tyle_samo_ab = 0, liczba_tyle_samo_ac = 0, liczba_tyle_samo_bc = 0;
	//int liczba_tyle_samo_ab = 0, liczba_tyle_samo_ac = 0, liczba_tyle_samo_bc = 0;
	//int najmniejsza_roznica_ab = 2000000001;
	// int najmniejsza_roznica_ac = 2000000001;
	//  int najmniejsza_roznica_bc = 2000000001;
	  int najmniejsza_roznica_a = 2000000001;
	 int najmniejsza_roznica_b = 2000000001;
	  int najmniejsza_roznica_c = 2000000001;
	int do_przelozenia_a = 0, do_przelozenia_b = 0, do_przelozenia_c = 0;
	//int T[n][3];
	while(n--){
		//cout<<n<<"\n";
		//cout<<(p-n);
		cin>>a>>b>>c;
		//T[n][0]=a;
		//T[n][1]=c;
		//T[n][2]=a;
		if (a==0 and b==0 and c == 0) liczba_pustych+=1;
		/*else if (a!=0 and b==0 and c == 0) liczba_z_najwiecej_a+=1;
		else if (a==0 and b!=0 and c == 0) liczba_z_najwiecej_b+=1;
		else if (a==0 and b==0 and c != 0) liczba_z_najwiecej_c+=1;*/
		else if (a>=b and a>=c){//nie powinno byc =
			if (najmniejsza_roznica_b > a-b) najmniejsza_roznica_b = a-b;
			if (najmniejsza_roznica_c > a-c) najmniejsza_roznica_c = a-c;
			liczba_z_najwiecej_a+=1;
			liczba_b_do_przeniesienia +=b;
			liczba_c_do_przeniesienia +=c;
		}
		else if (b>=a and b>=c){
			if (najmniejsza_roznica_a > b-a) najmniejsza_roznica_a = b-a;
			if (najmniejsza_roznica_c > b-c) najmniejsza_roznica_c = b-c;
			liczba_z_najwiecej_b+=1;
			liczba_a_do_przeniesienia +=a;
			liczba_c_do_przeniesienia +=c;
		}
		else if (c>=a and c>=b){
			if (najmniejsza_roznica_b > c-b) najmniejsza_roznica_b = c-b;
			if (najmniejsza_roznica_a > c-a) najmniejsza_roznica_a = c-a;
			liczba_z_najwiecej_c +=1;
			liczba_a_do_przeniesienia +=a;
			liczba_b_do_przeniesienia +=b;
		}
		/*if (abs(a-b) <najmniejsza_roznica_ab) {
			najmniejsza_roznica_ab =abs(a-b);
			do_przelozenia_a = a;
			do_przelozenia_b = b;
		}
		if (abs(a-c) <najmniejsza_roznica_ac) {
			najmniejsza_roznica_ab =abs(a-c);
			do_przelozenia_a = a;
			do_przelozenia_c = c;
		}
		if (abs(b-c) <najmniejsza_roznica_ab) {
			najmniejsza_roznica_ab =abs(a-b);
			do_przelozenia_a = a;
			do_przelozenia_b = b;
		}
		suma_a+=a;
		suma_b+=b;
		suma_c+=c;	*/
	}
	
	//cout<<"suma a = "<<suma_a<<"\n";
	//cout<<"suma a = "<<liczba_a_do_przeniesienia+liczba_b_do_przeniesienia+liczba_c_do_przeniesienia<<"\n";
	int suma = liczba_a_do_przeniesienia+liczba_b_do_przeniesienia+liczba_c_do_przeniesienia;
	/*cout<<"suma = "<<suma<<endl;
	cout<<"a = "<<liczba_z_najwiecej_a<<"  "<<najmniejsza_roznica_a<<endl;
	cout<<"b = "<<liczba_z_najwiecej_b<<"  "<<najmniejsza_roznica_b<<endl;
	cout<<"c = "<<liczba_z_najwiecej_c<<"  "<<najmniejsza_roznica_c<<endl;*/
	//if (liczba_z_najwiecej_a >0 and liczba_z_najwiecej_b>0 and  liczba_z_najwiecej_c>0)cout<<suma<<"\n";
	if(liczba_z_najwiecej_a==0 and liczba_a_do_przeniesienia> 0 )suma+= najmniejsza_roznica_a;
	if(liczba_z_najwiecej_b==0 and liczba_b_do_przeniesienia> 0 )suma+= najmniejsza_roznica_b;
	if(liczba_z_najwiecej_c==0 and liczba_c_do_przeniesienia> 0 )suma+= najmniejsza_roznica_c;
	//cout<<najmniejsza_roznica_a<<"\n";
	//cout<<najmniejsza_roznica_b<<"\n";
	//cout<<najmniejsza_roznica_c<<"\n";
	//cout<<suma<<"\n";
	cout<<suma;
	//system("pause");
	return 0;
}

