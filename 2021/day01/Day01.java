import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Day01{
    public static void main(String[] args) throws IOException{
        Path path = Paths.get("2021//day01//input.txt");
        List<String> input = Files.readAllLines(path);

        int increase = 0;

        for (int i = 0; i < input.size()-1; i++) {
            if (Integer.parseInt(input.get(i)) < Integer.parseInt(input.get(i+1))) {
                increase += 1;
            }   
        }
        System.out.println(increase);
    }
}