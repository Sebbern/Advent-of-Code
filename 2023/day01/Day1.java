import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Day1 {
    public static void main(String[] args) throws IOException{
        Path path = Paths.get("2023//day01//input.txt");
        List<String> input = Files.readAllLines(path);
        int sum = 0;

        for (String i : input) {
            int v = 0, h = i.length()-1;
            String valueLeft = "", valueRight = "";
            while (true){
                if ((int)i.charAt(v) < 58 && 47 < (int)i.charAt(v) && valueLeft.length() == 0){
                    valueLeft = String.valueOf(i.charAt(v));
                }
                else {} v++;

                if ((int)i.charAt(h) < 58 && 47 < (int)i.charAt(h) && valueRight.length() == 0){
                    valueRight = String.valueOf(i.charAt(h));
                }
                else {} h--;

                if (valueLeft.length() != 0 && valueRight.length() != 0) {
                    String value = valueLeft+valueRight;
                    sum += Integer.parseInt(value);
                    break;
                }
            }
        }

        System.out.println(sum);
    }
}