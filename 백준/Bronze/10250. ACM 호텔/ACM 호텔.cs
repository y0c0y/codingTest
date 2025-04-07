int n = int.Parse(Console.ReadLine());

            for (int i = 1; i <= n; i++)
            {
                string[] input = Console.ReadLine().Split(' ');
                
                int H = int.Parse(input[0]);
                int W = int.Parse(input[1]);
                int N = int.Parse(input[2]);
    
                int X = N / H;
                int Y = N % H;
                if (Y == 0) 
                    {Y = H;}
                else {X++;}
    
                int room = Y * 100 + X;
                
                Console.WriteLine(room);
             }