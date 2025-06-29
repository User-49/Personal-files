#include <stdio.h>
#include <math.h>
int main(){
int radius,x;
printf("enter the radius of circle: ");
scanf("%d",&radius);
for (int y=0;2*radius-x-y;y++){
	x=round(sqrt(radius*radius-y*y));
	for (int k=0;2*radius-x-k;k++){
		if (k<=radius-x) printf("_");
		else printf("*");
		}
	printf("\n");
	}
return 0;
}
