#include <stdio.h>
void main(){
int num,temp1=0;
printf("enter number: ");
scanf("%d",&num);
for (int temp2=num,k;temp2;temp2/=10){
	k=temp2%10;
	temp1 = temp1+k*k*k;
	}
if (temp1==num) printf("armstrong number\n");
else printf("not armstrong number\n");
}
