import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class day10_2 {
    private static String test(int cycle, int x){
        if (cycle-1 == x || cycle-1 == x-1 || cycle-1 == x+1){
            return "#";
        }
        else{
            return ".";
        }
    }

    public static void main(String[] args) throws IOException{
        Path path = Paths.get("2022//Day10//input.txt");
        List<String> input = Files.readAllLines(path);

        int x = 1;
        int cycle = 0;
        int loop = 0;
        ArrayList<String> symbol = new ArrayList<>();

        for (String i: input){
            String[] split = i.split(" ");
            if (i.equals("noop")){
                cycle += 1;
                if (cycle%40==0){
                    loop++;
                }
                symbol.add(test(cycle-(40*loop),x));
            }
            else {
                cycle += 1;
                if (cycle%40==0){
                    loop++;
                }
                symbol.add(test(cycle-(40*loop),x));
                cycle += 1;
                if (cycle%40==0){
                    loop++;
                }
                symbol.add(test(cycle-(40*loop),x));
                int addX = Integer.parseInt(split[1]);
                x += addX;
            }
        }
        for (int i = 0; i<symbol.size(); i++){
            if ((i+1)%40!=0){
                System.out.print(symbol.get(i));                
            }
            else {
                System.out.print(symbol.get(i)+"\n");
            }
        }
    }
}