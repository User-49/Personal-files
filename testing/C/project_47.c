#include <stdio.h>

int abs(int x){
	if (x<0)
		return -x;
	return x;
}

void main(){
	int n,r,c;
	printf("\nEnter the number: ");
	scanf(" %d", &n);

	for( int i=0; i<2*n-1; i++){
		for (int j=0; j<2*n-1; j++){
			r = abs(j-n+1)+1;
			c = abs(i-n+1)+1;
			printf("%d ",(r>=c)?r:c);
	}
	printf("\n");
	}

}
