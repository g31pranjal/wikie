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
int main(int argc,char *argv[]){
/*	fstream fin;

	char filename[]="ab/A.txt";
	create_blocks(filename);
*/
sort_file(argv[1]);

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