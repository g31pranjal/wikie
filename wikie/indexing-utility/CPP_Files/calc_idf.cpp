#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc,char *argv[]){
	char filename[100];	
	sprintf(filename,"temp/tf/calc/final/%s",argv[1]);
	if (!strcmp(argv[1],"idf")||!strcmp(argv[1],"tf")||!strcmp(argv[1],"posting"))
		return 0;
	cout<<"opening	"<<filename<<".............................."<<endl;
	fstream fin(filename,ios::in);
	char file[100];
	sprintf(file,"temp/tf/calc/final/posting/%s",argv[1]);
	

	vector <int>id;
	id.clear();
	
	string prev_term;
	int prev_docid;
	int prev_freq;
	fin>>prev_term>>prev_docid>>prev_freq;
	//id.push_back(prev_docid);
	fstream fout(file,ios::out);
	fout<<prev_term<<"	";
	fout<<prev_docid<<",";	
	int count=1;
	
	while (!fin.eof()){
		
			
		string term;
		int docid;
		int freq;
		fin>>term>>docid>>freq;
		if (!(prev_term==term)){
			prev_term=term;
			prev_docid=docid;
			prev_freq=freq;
			
			fout<<endl;
			if (prev_term=="")
				continue;	
			fout<<prev_term<<"	";
			fout<<prev_docid<<",";
			count=1;	
			continue;
		}
		fout<<docid<<",";
			
		


	}
	fin.close();
	fout.close();
	return 0;
}
