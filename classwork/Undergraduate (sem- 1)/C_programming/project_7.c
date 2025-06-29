#include <stdio.h>
void main(){
float a,b;
char oprtr;
printf("eter a simple expression(a [operator] b): ");
scanf("%f %c %f",&a,&oprtr,&b);
switch (oprtr){
case '+':printf("%f\n",(a+b)); break;
case '-':printf("%f\n",(a-b)); break;
case '*':printf("%f\n",(a*b)); break;
case '/':if (b==0){printf("zero division error\n");return;}
	 printf("%f\n",(a/b)); break;
default: printf("invalid operation\n");
}}
/*

#include <stdio.h>
void main(){
float a,b;
int opr;
char choice;
do{
printf("\nenter first number: ");
scanf("%f",&a);
printf("enter second number: ");
scanf("%f",&b);
printf("enter type of operation:\n1-Add\n2-Sub\n3-Mul\n4-Div\n> ");
scanf("%d",&opr);
switch (opr){
case 1: printf("%f + %f = %f\n",a,b,a+b); break;
case 2: printf("%f - %f = %f\n",a,b,a-b); break;
case 3: printf("%f * %f = %f\n",a,b,a*b); break;
case 4: if (b==0) {printf("zero division error\n"); break;}
	printf("%f / %f = %f\n",a,b,a/b); break;
default: printf("invalid operation\n");
}
printf("do you widh to continue(y/n): ");
scanf(" %c",&choice);
} while (choice!='n');
}*/
