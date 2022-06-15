//Bartosz Jardzioch 2020/21
#include<iostream>
using namespace std;
int Tab[9][9] = {0, 6, 0, 4, 0, 0, 0, 7, 0, 
				 0, 8, 0, 0, 0, 0, 0, 2, 9,
				 0, 7, 0, 0, 2, 0, 5, 0, 0,
				 0, 0, 5, 6, 0, 0, 0, 0, 4,
				 9, 0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 5, 0, 0, 0, 0, 3,
				 0, 0, 4, 1, 0, 0, 0, 0, 0,
			 	 8, 0, 0, 0, 9, 0, 0, 0, 0,
				 0, 0, 0, 0, 8, 0, 1, 0, 6};
int Tab_zerowa[9][9] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 
				 0, 0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 0, 0, 0, 0, 0, 0};
int Tab_nierozwiazana[9][9] = {0, 0, 0, 0, 6, 0, 0, 0, 0, 
				 7, 0, 0, 4, 0, 3, 0, 0, 2,
				 0, 0, 9, 2, 0, 1, 8, 0, 0,
				 9, 0, 7, 0, 0, 0, 3, 0, 4,
				 0, 0, 0, 1, 0, 2, 0, 0, 0,
				 8, 0, 3, 0, 0, 0, 1, 0, 5,
				 0, 0, 6, 7, 0, 4, 2, 0, 0,
				 3, 0, 0, 8, 0, 6, 0, 0, 1,
				 0, 0, 0, 0, 9, 5, 0, 0, 0};
bool Tab_Moz[9][9][9];
void render(){
	for (int i = 0; i<9;i++){
		for (int j = 0;j<9;j++){
			cout<<Tab[i][j]<<"  ";
		}
		cout<<"\n";
	}
}
bool only_one_true(int i, int j){
	int y=0;
	for (int k = 0;k<9;k++){
//		cout<<"\nTO TU  "<<Tab_Moz[i][j][k]<<"\n";
		if(Tab_Moz[i][j][k]){
		y++;
		}
	}
//	cout<<"\nY  "<<y<<"  \n";
	if (y>1)return false;
	else return true;
	
}
int only_one_number_possible_in_row_collumn(int i,int  j){
	for (int n=0;n<9;n++){
		int count = 0;
		for (int a = 0;a<9;a++){
			if(Tab_Moz[a][j][n]==true)count++;
		}
		
//		if(n==0)cout<<"\n\ntu jest blad count  =  "<<count<<"  i = "<<i<<"  j  =  "<<j<<"  n  =  "<<n<<"\n\n";
		if(count==1)return n+1;
		count = 0;
		for (int a = 0;a<9;a++){
			if(Tab_Moz[i][a][n]==true)count++;
		}
		if(count==1)return n+1;
		count = 0;
		if(i<3 and j<3){
			for (int a = 0;a<3;a++){
				for (int b = 0;b<3;b++){
					if(Tab_Moz[a][b][n]==true)count++;
				}
			}
		}else if(i<6 and j<3){
			for (int a = 3;a<6;a++){
				for (int b = 0;b<3;b++){
					if(Tab_Moz[a][b][n]==true)count++;
				}
			}
		}else if(i<9 and j<3){
			for (int a = 6;a<9;a++){
				for (int b = 0;b<3;b++){
					if(Tab_Moz[a][b][n]==true)count++;
				}
			}
		}else if(i<3 and j<6){
			for (int a = 0;a<3;a++){
				for (int b = 3;b<6;b++){
					if(Tab_Moz[a][b][n]==true)count++;
				}
			}
		}else if(i<3 and j<9){
			for (int a = 0;a<3;a++){
				for (int b = 6;b<9;b++){
					if(Tab_Moz[a][b][n]==true)count++;
				}
			}
		}else if(i<6 and j<6){
			for (int a = 3;a<6;a++){
				for (int b = 3;b<6;b++){
					if(Tab_Moz[a][b][n]==true)count++;
				}
			}
		}else if(i<9 and j<6){
			for (int a = 6;a<9;a++){
				for (int b = 3;b<6;b++){
					if(Tab_Moz[a][b][n]==true)count++;
				}
			}
		}else if(i<6 and j<9){
			for (int a = 3;a<6;a++){
				for (int b = 6;b<9;b++){
					if(Tab_Moz[a][b][n]==true)count++;
				}
			}
		}else if(i<9 and j<9){
	//		cout<<"jestem\n";
			for (int a = 6;a<9;a++){
				for (int b = 6;b<9;b++){
					if(Tab_Moz[a][b][n]==true)count++;
				}
			}
		}
		if(count==1)return n+1;
	}
	return 0;
}
void exclude_from_square(int i, int j, int n){
	if(i<3 and j<3){
		for (int a = 0;a<3;a++){
			for (int b = 0;b<3;b++){
				Tab_Moz[a][b][n]=false;
			}
		}
	}else if(i<6 and j<3){
		for (int a = 3;a<6;a++){
			for (int b = 0;b<3;b++){
				Tab_Moz[a][b][n]=false;
			}
		}
	}else if(i<9 and j<3){
		for (int a = 6;a<9;a++){
			for (int b = 0;b<3;b++){
				Tab_Moz[a][b][n]=false;
			}
		}
	}else if(i<3 and j<6){
		for (int a = 0;a<3;a++){
			for (int b = 3;b<6;b++){
				Tab_Moz[a][b][n]=false;
			}
		}
	}else if(i<3 and j<9){
		for (int a = 0;a<3;a++){
			for (int b = 6;b<9;b++){
				Tab_Moz[a][b][n]=false;
			}
		}
	}else if(i<6 and j<6){
		for (int a = 3;a<6;a++){
			for (int b = 3;b<6;b++){
				Tab_Moz[a][b][n]=false;
			}
		}
	}else if(i<9 and j<6){
		for (int a = 6;a<9;a++){
			for (int b = 3;b<6;b++){
				Tab_Moz[a][b][n]=false;
			}
		}
	}else if(i<6 and j<9){
		for (int a = 3;a<6;a++){
			for (int b = 6;b<9;b++){
				Tab_Moz[a][b][n]=false;
			}
		}
	}else if(i<9 and j<9){
//		cout<<"jestem\n";
		for (int a = 6;a<9;a++){
			for (int b = 6;b<9;b++){
				Tab_Moz[a][b][n]=false;
			}
		}
	}
}
int main(){
	render();
	for (int i = 0; i<9;i++){
		for (int j = 0;j<9;j++){
			for(int k = 0;k<9;k++){
				Tab_Moz[i][j][k]=true;	
			}
		}
	}
	
	for (int b = 0;b<15;b++){
	for (int i = 0; i<9;i++){
		for (int j = 0;j<9;j++){
			if(Tab[i][j]!=0){
				exclude_from_square(i, j, Tab[i][j]-1);
//				cout<<"2";
				for (int a = 0; a<9;a++){
					Tab_Moz[i][j][a]=false;
					Tab_Moz[a][j][Tab[i][j]-1]=false;
					Tab_Moz[i][a][Tab[i][j]-1]=false;
				}
			}
		}
	}
	for (int i = 0; i<9;i++){
		for (int j = 0;j<9;j++){
				if(only_one_true(i, j)){
//					cout<<"3";
					for (int a = 0; a<9;a++){
						if (Tab_Moz[i][j][a]==true){
//							cout<<"4";
							Tab[i][j] = a+1;
//							cout<<"znalazlem  w b =   "<<b<<"  i, j =  "<<i<<"  "<<j<<"  "<<a+1<<"\n";
						}
					}
				}
				int n = only_one_number_possible_in_row_collumn(i, j)-1;
//				if(i==0 and j ==7)cout<<"\n\ntu jest blad   i = "<<i<<"  j  =  "<<j<<"  n  =  "<<n<<"Tab_Moz[i][j][n] = "<<Tab_Moz[i][j][n]<<"\n\n";
				if (n!=-1 and Tab_Moz[i][j][n]==true){
					Tab[i][j] = n+1;	
//					cout<<"znalazlem  w b =   "<<b<<"  i, j =  "<<i<<"  "<<j<<"  "<<n+1<<"\n";
				}
		}
	}
	}
	cout<<"\n";
	render();
	for (int i = 0; i<9;i++){
		for (int j = 0;j<9;j++){
			for(int k = 0;k<9;k++){
//				cout<<Tab_Moz[i][j][k]<<" ";	
			}
//			cout<<"\n";
		}
	}
	system("pause");
	return 0;
}

