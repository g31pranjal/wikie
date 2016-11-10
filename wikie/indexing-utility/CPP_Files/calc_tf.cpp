#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>

using namespace std;
int main(int argc,char *argv[]){
	char filename[100];	
	sprintf(filename,"temp/tf/calc/%s",argv[1]);
	if (!strcmp(argv[1],"final"))
		return 0;
	cout<<"opening	"<<filename<<".............................."<<endl;
	fstream fin(filename,ios::in);
	char file[100];
	sprintf(file,"temp/tf/calc/final/TF%s",argv[1]);
	


	string prev_term;
	int prev_docid;
	int prev_freq;
	fin>>prev_term>>prev_docid>>prev_freq;	
	
	fstream fout(file,ios::out);
	while (!fin.eof()){
		string term;
		int docid;
		int freq;
		fin>>term>>docid>>freq;
		if (!(prev_term==term && prev_docid==docid)){
			fout<<prev_term<<"	"<<prev_docid<<"	"<<prev_freq<<endl;
			prev_term=term;
			prev_docid=docid;
			prev_freq=freq;		
			continue;
		}
		prev_freq+=freq;

			
		//cout<<term<<"*"<<docid<<"*"<<freq<<endl;
		


	}
	fin.close();
	fout.close();
	return 0;
}
