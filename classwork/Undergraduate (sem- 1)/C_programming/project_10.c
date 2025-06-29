#include <stdio.h>
void main(){
int num, k, i, rev=1;
printf("enter number: ");
scanf("%d",&num);
start:
for (int i=0;(i!=-1);i+=rev){
	for (k=0;k!=(num/2-i);k++)
		printf(" ");
	for (k=0;k!=i+1;k++)
		printf("* ");
	printf("\n");
	if (i==num/2) rev=-1;
	}
}
