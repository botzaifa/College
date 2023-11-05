#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	int length, k;
	char str[100];
	printf ("Enter a String : ");
	gets(str);
	length = strlen(str);
	length = length - 1;
	k=0; 
	while (length > k)
	{
	 if (str[length] != str[k])
	 {
	 	printf("%s is not a Palindrome", str);
	 	exit (0);
	 }
	  length --;
	  k++;	
	}
	
	printf("%s is a Palindrome", str);
	return 0;
		
	
	
}
