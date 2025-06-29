#include <stdio.h>
void main(){
int num,rev=0,temp;
printf("enter number: ");
scanf("%d",&num);
for (;num;num/=10)
	rev = rev*10+num%10;
printf("reversed number is: %d\n",rev);
}
