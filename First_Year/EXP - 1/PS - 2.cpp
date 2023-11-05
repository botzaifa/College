#include <Stdio.h>

int main(){
	
	float a, b, c;
	printf("Enter the value of Basic salary : ");
	scanf("%f", &a);
	
	printf("Enter the value of HRA : ");
	scanf("%f", &b);
	
	printf("Enter the value of DA : ");
	scanf("%f", &c);
	
 
	printf("Gross Salary of Employee is : %f", a + b + c);
	
	return 0;
}
