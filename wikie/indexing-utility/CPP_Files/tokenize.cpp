#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctype.h>
#include <vector>
#include <map>

#include <thread>
#define BUFFER_SIZE 100
using namespace std;

static long long int count=0,ct=0,filecount=0;
fstream file[26];

char *lower_case(char *word){
  

      for (int i=0;i<strlen(word);i++){
          word[i]=tolower(word[i]);

      } 

      return word;

}

void tokens(char buffer[],int fc){
        
        char *token;    

        token = strtok(buffer, " .,;:\"\'=+!@#$%^&*()\n ");
       
       if (token && strlen(token)>=3 && isalpha(token[0])){
        

                token=lower_case(token);
               //cout<<token[0]-'a'<<endl; 
                if (token[0]-'a' >=0)            
                    file[token[0]-'a']<<token<<"  "<<fc<<endl;              
                ct++; 
        }


      while(token){
        token = strtok(NULL," .,;:\"\'=+!@#$%^&*()\n ");
        if(token && strlen(token)>=3 && isalpha(token[0])){
          

                token=lower_case(token);
                 //cout<<token[0]-'a'<<endl; 
                 if (token[0]-'a' >=0)
                    file[token[0]-'a']<<token<<"  "<<fc<<endl;               
             

          //printf("%s\n",token);
             ct++; 
          }

       
      }



}

void tokenize(char file[])
{
   
   char filename[200]="cleaned_data/";
   //strcpy(word,"neel/");
   strcat(filename,file);		
   cout<<(++count)<<" opening file "<<filename<<"............................................................................"<<endl;	
      
	 ifstream fin;
   fin.open(filename,ios::in);	
    //flush(filename)	;
  	filecount++;
    	
    while (!fin.eof())
    {
	
		char buffer[BUFFER_SIZE+1]={'\0'};		 
		//vector<char> buffer (10,0);      // create vector of 1024 chars with value 0   
 		fin.read(&buffer[0],BUFFER_SIZE );
		buffer[BUFFER_SIZE]='\0';
		//cout<<buffer<<endl<<endl;
    tokens(buffer,filecount);


    } 
   // cout<<"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ "<<ct<<endl;
 
	fin.close();
  
}




int main(){
	//tokenize("test.txt");
system("mkdir ab");
int i;
char al='A';
for (i=0;i<26;i++){
  char filename[200]="";
  char word[200]="";
  sprintf(word,"ab/%c.txt",al++);
  file[i].open(word,ios::out);
  
  
  }


//file[0]<<"hello world"<<endl;

//return 0;
DIR *dir;	
struct dirent *ent;
fstream fout;
fout.open("FileMap.txt",ios::out);
 
if ((dir = opendir ("cleaned_data/")) != NULL) {
  /* print all the files and directories within directory */
  while ((ent = readdir (dir)) != NULL) {
	if (!strcmp(ent->d_name,".")|| !strcmp(ent->d_name,".."))
		continue;
  
	tokenize(ent->d_name);
    //printf ("%s\n", ent->d_name);
  fout<<filecount<<"  "<<ent->d_name<<endl;
    	


  }
  closedir (dir);
  for (i=0;i<26;i++){
      file[i].close();


  }



} else {
  /* could not open directory */
  perror ("");
  return EXIT_FAILURE;
}
fout.close();
return 0;
}

