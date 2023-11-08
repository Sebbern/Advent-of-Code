import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Day01_2{
    public static void main(String[] args) throws IOException{
        Path path = Paths.get("2021//day01//input.txt");
        List<String> input = Files.readAllLines(path);

        int increase = 0;
        int temp = Integer.parseInt(input.get(0)) + Integer.parseInt(input.get(1)) + Integer.parseInt(input.get(2));

        for (int i = 1; i < input.size()-2; i++) {
            if (temp < (Integer.parseInt(input.get(i)) + Integer.parseInt(input.get(i+1)) + Integer.parseInt(input.get(i+2)))) {
                increase += 1;
            }

            temp = Integer.parseInt(input.get(i)) + Integer.parseInt(input.get(i+1)) + Integer.parseInt(input.get(i+2));
        }
        System.out.println(increase);
    }
}