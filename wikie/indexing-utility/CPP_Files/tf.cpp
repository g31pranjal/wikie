#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <vector>
#include <string.h>
#include <stdio.h>
#include <dirent.h>
#include <stdlib.h>
#define BLOCK_SIZE 688888
#define BUFFER_SIZE 100
using namespace std;
void create_blocks(char filename[]){
	system("mkdir temp");
	fstream fin;
	fin.open(filename,ios::in);
	int count=0;
	char newfilename[200]="";
	int ct=0;
	sprintf(newfilename,"temp/%d.txt",ct++);
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
		 		sprintf(newfilename,"temp/%d.txt",ct++);

	cout<<"creating "<<newfilename<<"................................................"<<endl;
		 		fout.close();
				fout.open(newfilename,ios::out);
		 		

		 }		
	}	

	fout.close();
}

void calc_tf(char filename[]){


	
  	char file[100];
	sprintf(file,"temp/%s",filename);
	cout<<"Generating frequencies for "<<filename<<"............................................................................"<<endl;	
  	
	fstream fin;
	fstream fout;

	char output[200];
	sprintf(output,"temp/tf/t%s",filename);
	fin.open(file,ios::in);
	fout.open(output,ios::out);
	if (!fin)
		{cout<<"unable to open!!!!"<<endl;
		return ;}	
	string prev="";
	string curr="";
	char line[100];
	fin.getline(line,199);
	string str(line);
	prev=str;	 
	int count=0;
	while (!fin.eof())
    {
		char line[100];

		 fin.getline(line,199);
		 string str(line);
		 if (str=="")
		 	continue;	
		 curr=str;
		 count++;
		 if (curr != prev){
		 	//print prev count	
		 	fout<<prev<<" "<<count<<endl;
		 	count=0;	
		 }
		prev=curr;
	}
	count++;
			fout<<prev<<" "<<count<<endl;
	fin.close();
	fout.close();

	
}
int main(){
	

	//char filename[]="ab/A.txt";
//	create_blocks(filename);

system("mkdir temp/tf");

	DIR *dir;	
struct dirent *ent;

 
if ((dir = opendir ("temp/")) != NULL) {
  /* print all the files and directories within directory */
  while ((ent = readdir (dir)) != NULL) {
	if (!strcmp(ent->d_name,".")|| !strcmp(ent->d_name,".."))
		continue;
  
	//tokenize(ent->d_name); Replac with file action
    //printf ("%s\n", ent->d_name);
	//sort_file(ent->d_name);
	if (!strcmp(ent->d_name,"tf"))
		continue;
	calc_tf(ent->d_name);
	


  }
  closedir (dir);
 


} else {
  /* could not open directory */
  perror ("");
  return EXIT_FAILURE;
}

	return 0;
}