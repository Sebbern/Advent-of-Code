import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Day3 {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("2021//day03//input.txt");
        List<String> input = Files.readAllLines(path);

        int count = 0, zeroBinary = 0, oneBinary = 0;
        StringBuilder gammaBinary = new StringBuilder();
        StringBuilder epsilonBinary = new StringBuilder();
        while (count < input.get(0).length()){
            for (String i : input) {
                if (i.charAt(count) == '0'){
                    zeroBinary += 1;
                }
                else if (i.charAt(count) == '1'){
                    oneBinary += 1;
                }
            }
            
            if (zeroBinary < oneBinary){
                gammaBinary.append(1);
                epsilonBinary.append(0);
            }
            else if (oneBinary < zeroBinary){
                gammaBinary.append(0);
                epsilonBinary.append(1);
            }
            zeroBinary = 0; oneBinary = 0;
            count++;
        }

        System.out.println(Integer.parseInt(gammaBinary.toString(), 2) * Integer.parseInt(epsilonBinary.toString(), 2));
    }
}
