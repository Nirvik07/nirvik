#include<stdio.h>
int main()
{
	int n,key;
	printf("Enter the value of n: ");
	scanf("%d",&n);
	int a[n],i,j,temp;
	printf("Enter the elements:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=1;i<n;i++)
	{
		key=a[i];
		j=i-1;
		while(j>=0&&a[j]>key)
		{
			a[j+1]=a[j];
			j=j-1;
		}
		a[j+1]=key;
	}
	for(i=0;i<n;i++)
	printf("%d ",a[i]);
}
	
