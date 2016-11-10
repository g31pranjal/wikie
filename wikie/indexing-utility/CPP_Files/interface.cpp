#include <string.h>
#include <stdio.h>
#include <dirent.h>
#include <stdlib.h>
#include <ctype.h>
#include <string>
#define BLOCK_SIZE 50000
#define BUFFER_SIZE 100

using namespace std;


int main(){


	DIR *dir;	
struct dirent *ent;
 
if ((dir = opendir ("temp/tf/")) != NULL) {
 
  while ((ent = readdir (dir)) != NULL) {
	if (!strcmp(ent->d_name,".")|| !strcmp(ent->d_name,".."))
		continue;
  
	if (ent->d_type==DT_DIR)
			continue;

	char filename[100];
	strcpy(filename,ent->d_name);	
	string str(filename);
	if (str.size()<2)
			continue;
	char ch=str[2];
	char dir[100];
	sprintf(dir,"%c/",toupper(ch));
	char cmd[100];
	sprintf(cmd,"mv temp/tf/%s temp/tf/%s",ent->d_name,dir);
	system(cmd);



  }
  closedir (dir);
 


} else {
  //could not open directory 
  perror ("");
  return EXIT_FAILURE;
}



	return 0;
}