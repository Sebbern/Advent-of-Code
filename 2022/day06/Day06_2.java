import java.io.IOException;
import java.nio.file.*;
import java.util.*;

public class Day06_2 {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("2022//Day06//input.txt");
        List<String> input = Files.readAllLines(path);
        
        String[] split = input.get(0).split("");
        ArrayList<String> letterSet = new ArrayList<String>();
        int count = 0;
        
        while (true){
            if (!letterSet.contains(split[0].substring(0,1))){
                letterSet.add(split[0].substring(0,1));
                split = Arrays.copyOfRange(split, 1, split.length);
                count++;
                if (letterSet.size() == 14){
                    System.out.println(count);
                    break;
                }
            }
            else if (letterSet.contains(split[0].substring(0,1))){
                for (String i: letterSet){
                    if (i.equals(split[0].substring(0,1))){
                        letterSet.remove(0);
                        break;
                    }
                }
            }
        }
    }
}