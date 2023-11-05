#include <stdio.h>
 
 
int main()
{
	int age;
	printf("Enter age : ");
	scanf("%d", &age);
	
	if(age >=21){
		printf("The person is an Adult \n");
		printf("The person can Vote \n");
		printf("The person can Drive \n");
		printf("The person can Drink aswell \n");
	}
	
	else if(age >=18 <21 ){
			printf("The person is an Adult \n");
		printf("The person can Vote \n");
		printf("The person can Drive \n");
	}
	
	else{
		printf("The person is not an Adult \n");
	}
	
	printf("THANK YOU");
	
	return 0;
	
	
}
