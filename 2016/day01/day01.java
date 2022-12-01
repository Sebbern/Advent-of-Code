import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class day01 {

    public static void main(String[] args) throws IOException{
        File inputTxt = new File("2016\\day01\\input.txt");
        BufferedReader input = new BufferedReader(new FileReader(inputTxt));
        String string;
        List<String> directions = new ArrayList<>();
        
        while ((string = input.readLine()) != null){
            directions = Arrays.asList(string.split(",\\s*"));
        }
        input.close();

        int direction = 0;
        int x = 0;
        int y = 0;
        char first;
        for (String i : directions){
            first = i.charAt(0);
            if (Character.toString(first).equals("L")){
                direction -= 1;
            }
            else if (Character.toString(first).equals("R")){
                direction += 1;
            }

            if (direction == (-1)){
                direction = 3;
            }
            else if (direction == 4){
                direction = 0;
            }

            i = i.substring(1);
            switch (direction){
                case 0: x += Integer.parseInt(i); break;
                case 1: y += Integer.parseInt(i); break;
                case 2: x -= Integer.parseInt(i); break;
                case 3: y -= Integer.parseInt(i); break;
            }
        }
        System.out.println(Math.abs(x)+Math.abs(y));
    }
}
