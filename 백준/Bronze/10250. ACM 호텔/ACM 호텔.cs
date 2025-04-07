 int n = int.Parse(Console.ReadLine());

        for (int i = 1; i <= n; i++)
        {
            string[] input = Console.ReadLine().Split(' ');
            
            int H = int.Parse(input[0]);
            int W = int.Parse(input[1]);
            int N = int.Parse(input[2]);

            int x = 1;
            int y = 1;
            while(true)
            {
                N--;
                if(N == 0) break;
                if(y == H)
                {
                    y = 1;
                    x++;
                }
                else{
                    y++;
                }
                
            }
            Console.WriteLine(y*100+x);
        }