int i;
int k;
int ans = 0;
List<int> divcheck = new List<int> {11,12,13,14,15,16,17,18,19};
List<bool> boolcheck = new List<bool> { };

for (i = 20; ans == 0; i+=20)
{
    boolcheck = new List<bool> { };

    for (k = 0; k < divcheck.Count(); k++)
    {
        if (i % divcheck[k] == 0)
        {
            boolcheck.Add(true);
        }
        else
        {
            boolcheck.Add(false);
            break;
        }
    }

    if (!boolcheck.Contains(false))
    {
        ans = i;
        Console.WriteLine(ans);
    }
}