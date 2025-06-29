#include <stdio.h>
void main(){
int num,sum=0;
printf("enter number: ");
scanf("%d",&num);
for (;num;num--) sum+=num;
printf("sum of natural numbers till n: %d\n",sum);
}
