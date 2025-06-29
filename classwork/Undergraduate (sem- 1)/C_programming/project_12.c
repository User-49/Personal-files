#include <stdio.h>
void main(){
int num, flag=0,x,y;
printf("enter number: ");
scanf("%d",&num);
for (int i=1;i<=num;i++){
  if (flag == 0){x=i;y=num-i;}
  else {x=num-i;y=i;}
  
  for (int k=x;k;k--) printf("*");
  for (int k=y;k;k--) printf("  ");
  for (int k=x;k;k--) printf("*");
  printf("\n");
  
  if ((i==num)&&(flag==0)) {i=0;flag=1;}
  }
}
