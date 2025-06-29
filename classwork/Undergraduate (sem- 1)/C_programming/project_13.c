#include <stdio.h>

int bin(int num);

int bin(int num){
if (!num) return (0);
else{ return bin(num/2)*10+(num%2);
}}

void main(){
int num;
printf("enter the number: ");
scanf("%d",&num);
printf("binary num is: %d\n",bin(num));
}
