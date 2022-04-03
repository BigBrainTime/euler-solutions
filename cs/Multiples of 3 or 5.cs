using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cs
{
    public class Class1
    {
        static void Main()
        {
            int[] mult = new int[] {3, 5};
            List<int> current = new List<int> { };

            int i;
            int k;

            for (i = 0; i == 1000; i++)
            {
                for (k = 0; k == mult.Length; k++)
                {
                    if (i%mult[k] == 0)
                    {
                        current.Add(i);
                        break;
                    }
                }
            }
            Console.WriteLine(current.Sum(x => Convert.ToInt32(x)));
        }
    }
}
