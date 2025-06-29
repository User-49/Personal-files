#include <stdio.h>
void main(){
int num;
char a=' ';
printf("enter number: ");
scanf("%d",&num);
for (int i=0;i<=num-1;i++){
	for (int k=num-i;k;k--)
		printf(" ");
	printf("*");
	for (int k=i-1;k>=1;k--)
		printf(" %c",a);
	if (i) printf(" *");
	if (i==num-2) a='*';
	printf("\n");
}
}
