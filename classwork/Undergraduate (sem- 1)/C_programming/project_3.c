#include <stdio.h>
void main(){
double sum, num_1, num_2;
printf("Enter value of first number: ");
scanf("%lf", &num_1);
printf("Enter valuse of second number: ");
scanf("%lf", &num_2);
sum = num_1 + num_2;
printf("\nsum of %lf and %lf is: %lf\n", num_1,num_2,sum);
}
