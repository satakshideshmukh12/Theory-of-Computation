#include<iostream>
using namespace std;

int main()
{
	string s;
	cin>>s;
	int l = s.length();
	bool count=false;
	if(s[0]=='1' && s[l]=='1')
	{
		for(int i=1;i<l-1;i++)
		{
			if(s[i]=='0')
			{
				count = true;
			}
			else
			{
				count = false;
			}
		}
	}
	else
	{
		count = false;
	}
	if(count==true)
	{
		cout<<"String is correct"<<endl;
	}
	else
	{
		cout<<"String is wrong"<<endl;
	}
}
