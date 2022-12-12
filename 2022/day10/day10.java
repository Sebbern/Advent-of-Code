import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class day10 {
    private static int test(int cycle, int x){
        switch (cycle) {
            case 20, 60, 100, 140, 180, 220: return cycle*x;
        }
        return 0;
    }

    public static void main(String[] args) throws IOException{
        Path path = Paths.get("2022//Day10//input.txt");
        List<String> input = Files.readAllLines(path);

        int x = 1;
        int cycle = 0;
        int sum = 0;

        for (String i: input){
            String[] split = i.split(" ");
            if (i.equals("noop")){
                cycle += 1;
                sum += test(cycle,x);
            }
            else {
                cycle += 1;
                sum += test(cycle,x);
                cycle += 1;
                sum += test(cycle,x);
                int addX = Integer.parseInt(split[1]);
                x += addX;
            }
        }
        System.out.println(sum);
    }
}
