int[] mult = new int[] {3, 5};
List<int> current = new List<int> { };

for (int i = 0; i < 1000; i++)
{
    for (int k = 0; k < mult.Length; k++)
    {
        if (i % mult[k] == 0)
        {
            current.Add(i);
            break;
        }
    }
}
Console.WriteLine(current.Sum());