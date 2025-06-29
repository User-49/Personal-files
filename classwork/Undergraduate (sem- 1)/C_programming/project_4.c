#include <stdio.h>
void main(){
char name[25];
int age;
printf("Enter your age and name: ");
scanf("%d, %s",&age, name);
printf("\nYou have entered:\nname: %s\nage: %d\n",name,age);
}
