import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Day2_2 {
    public static void main(String[] args) throws IOException{
        Path path = Paths.get("2021//day02//input.txt");
        List<String> input = Files.readAllLines(path);

        int pos = 0;
        int depth = 0;
        int aim = 0;

        for (String i : input) {
            String[] splitStrings = i.split("\\s");
            String direction = splitStrings[0]; int amount = Integer.parseInt(splitStrings[1]);

            if (direction.equals("forward")){
                pos += amount;
                depth += aim*amount;
            }
            else if (direction.equals("down")){
                aim += amount;
            }
            else if (direction.equals("up")){
                aim -= amount;
            }
        }

        System.out.println(pos * depth);
    }
}
