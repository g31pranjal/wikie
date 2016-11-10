#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <vector>
#include <string.h>
#include <stdio.h>
#include <dirent.h>
#include <stdlib.h>
#define BLOCK_SIZE 650000
#define BUFFER_SIZE 100
using namespace std;
char ch='A';

void create_blocks(char filename[]){

	fstream fin;
	fin.open(filename,ios::in);
	int count=0;
	char newfilename[200]="";
	int ct=0;
	sprintf(newfilename,"temp/%c%d.txt",ch,ct++);
	cout<<"creating "<<newfilename<<"................................................"<<endl;
	fstream fout;
	fout.open(newfilename,ios::out);
	while (!fin.eof())
    {
		char line[100];

		 fin.getline(line,199);
		 string str(line);
		 fout<<str<<endl;
		 if (str=="")
		 	continue;	
		 count++;
		 if(count>=BLOCK_SIZE){
		 		count=0;
		 		sprintf(newfilename,"temp/%c%d.txt",ch,ct++);

	cout<<"creating "<<newfilename<<"................................................"<<endl;
		 		fout.close();
				fout.open(newfilename,ios::out);
		 		

		 }		
	}	

	fout.close();
}

void sort_file(char filename[]){


	
  	char file[100];
	sprintf(file,"temp/%s",filename);
	cout<<"sorting file "<<filename<<"............................................................................"<<endl;	
  	
	fstream fin;
	fin.open(file,ios::in);

	vector <string>a;

	while (!fin.eof())
    {
		char line[100];

		 fin.getline(line,199);
		 string str(line);
		 if (str=="")
		 	continue;	
		a.push_back(str);

	}

	sort(a.begin(),a.end());
	int i;
	fstream fout;
	strcpy(file,"");
	sprintf(file,"temp/s%s",filename);
	fout.open(file,ios::out);


	for (i=0;i<a.size();i++){
		fout<<a[i]<<endl;


	}
	fin.close();
	fout.close();
	char cmd[100];
	
	sprintf(cmd,"rm temp/%s",filename);
	system(cmd);




}
int main(){
	//fstream fin;
    char al='A';
    int i;
    for (i=0;i<26;i++){
    	char file[200];
    	sprintf(file,"ab/%c.txt",al++);
		cout<<"Breaking down "<<file<<" into blocks"<<endl;
		create_blocks(file);
		ch++;
		//cout<<file<<endl;	
	}


/*	DIR *dir;	
struct dirent *ent;

 
if ((dir = opendir ("temp/")) != NULL) {
  // print all the files and directories within directory 
  while ((ent = readdir (dir)) != NULL) {
	if (!strcmp(ent->d_name,".")|| !strcmp(ent->d_name,".."))
		continue;
  
	//tokenize(ent->d_name); Replac with file action
    //printf ("%s\n", ent->d_name);
	sort_file(ent->d_name);

	


  }
  closedir (dir);
 


} else {
  //could not open directory 
  perror ("");
  return EXIT_FAILURE;
}
*/
	return 0;
}