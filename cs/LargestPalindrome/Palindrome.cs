int high = 0;
char[] arr;
int i;
int k;

for (i = 999; i > 99; i--)
{
    for (k = 999; k > 99; k--)
    {
        if ((i * k) > high)
        {
            arr = (((i * k).ToString()).ToCharArray());
            if (arr.ToString() == arr.Reverse().ToString())
            {
                high = i * k;
            }
        }
    }
}
Console.WriteLine(high);

//In progress