#include <stdio.h>
void main(){
float marks;
int grade;
printf("enter marks: ");
scanf("%f",&marks);
if (marks>90) grade=1;
else if (marks>80) grade=2;
else if (marks>70) grade=3;
else if (marks>60) grade=4;
else if (marks>50) grade=5;
switch (grade){
case 1: printf("A grade\n"); break;
case 2: printf("B grade\n"); break;
case 3: printf("C grade\n"); break;
case 4: printf("D grade\n"); break;
case 5: printf("E grade\n"); break;
default: printf("FAIL\n"); 
}}
