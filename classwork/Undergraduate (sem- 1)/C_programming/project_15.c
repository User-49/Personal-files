#include<stdio.h>
void main(){
FILE *fp;
char ch;
fp=fopen("project_14.c","r");
while (1){
	ch = fgetc(fp);
	if (ch==EOF)
		break;
	printf("%c",ch);
}
printf("\n");
fclose(fp);
}
