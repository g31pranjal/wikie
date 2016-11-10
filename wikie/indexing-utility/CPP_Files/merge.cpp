#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctype.h>
#include <vector>
#include <string>
#include <map>
#include <vector>
#include <queue>


#define BUFFER_SIZE 100

using namespace std;
int filecount=0;
void conv(string str,char word[]){
	int i;
	for (i=0;i<str.size();i++){
		word[i]=str[i];

	}
	word[i]='\0';
}
string merge(string file1,string file2){
	fstream fin1,fin2,fout;
	const char *s3=file1.c_str();
	const char *s4=file2.c_str();
	char tempfile1[100]="temp/tf/";
	strcat(tempfile1,s3);
	char tempfile2[100]="temp/tf/";
	strcat(tempfile2,s4);

	fin1.open(tempfile1,ios::in);
	fin2.open(tempfile2,ios::in);

	if (!fin1 && !fin2)
		return "";

			
	char word[100];
	sprintf(word,"%d.txt",filecount++);
	string str(word);
	char outfile[100];
	strcpy(outfile,"temp/tf/");
	strcat(outfile,word);
	fout.open(outfile,ios::out);

	cout<<"Joining "<<file1<<"	and	 "<<file2<<"	into 	"<<str<<endl;
	
	/*Merger CoDe HeRe*/
	string term1;
	string term2;
	string docid1;
	string docid2;
	long int tf1;
	long int tf2;

	
	//cout<<"hello";
	int flag=0;

	while (!fin1.eof() && !fin2.eof()){
		if (flag==0 || flag==-1){
		char line[100];

		 fin1.getline(line,199);
		 string term1(line);
		}
		
		
		if (flag==0 || flag==1){
		char line[100];

		 fin1.getline(line,199);
		 string str(line);
		}


		if (term1>term2){
				if (term2!="")
				fout<<term2<<endl;
				flag=1;
		

		}	
		else if (term1<term2){
				if (term1!="")
				fout<<term1<<endl;
				flag=-1;
		

		}
		else{
				if (term1!="")
				fout<<term2<<endl;
				flag=0;			
		}
		




	}


	while (!fin1.eof()){
		char line[100];

		 fin1.getline(line,199);
		 string term1(line);
		if (term1!="")	
		 fout<<term1<<endl;		
	}
	while (!fin2.eof()){
		char line[100];

		 fin2.getline(line,199);
		 string term2(line);
		if (term2!="")	
		 fout<<term2<<endl;		
	}



	fin1.close();
	fin2.close();
	fout.close();
	char word1[100];
	string temp="rm temp/tf/";
	temp+=file1;
	const char *s1=temp.c_str();
	


	
	string temp1="rm temp/tf/";
	temp1+=file2;
	const char *s2=temp1.c_str();
	
	
	system(s1);
	system(s2);

	return str;
}


int main(){

	
	DIR *dir;	
struct dirent *ent;

queue <string>q;

 
if ((dir = opendir ("temp/tf/")) != NULL) {
  /* print all the files and directories within directory */
  while ((ent = readdir (dir)) != NULL) {
	if (!strcmp(ent->d_name,".")|| !strcmp(ent->d_name,".."))
		continue;
  if (!strcmp(ent->d_name,"tf"))
  	continue;
  string str(ent->d_name); 		
  //cout<<str<<endl;
  q.push(str);  	

  }
  closedir (dir);
  
  



} else {
  /* could not open directory */
  perror ("");
  return EXIT_FAILURE;
}

while (!q.empty()){
	

	string file1=q.front();
	q.pop();

	if (q.empty()){

		break;
	}
	string file2=q.front();
	q.pop();
	
	string newfile=merge(file1,file2);
	q.push(newfile);

}


return 0;
}
