namespace fibonacci
{
    public class fibonacci
    {
        static void Main()
        {
            List<int> nums = new List<int>();
            nums.Add(1);
            nums.Add(2);
            int num = 3;
            int sum = 2;
            int i;

            for (i = 0; num < 4000000; i++)
            {
                num = nums[i] + nums[i + 1];
                nums.Add(num);
                if (num % 2 == 0)
                {
                    sum += num;
                }
            }
            Console.WriteLine(sum);
        }
    }
}