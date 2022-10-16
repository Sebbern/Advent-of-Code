import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;

public class day03_2 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        File inputtxt = new File("2015\\day03\\input.txt");
        BufferedReader input = new BufferedReader(new FileReader(inputtxt));
        String string;
        ArrayList<String> coordinates = new ArrayList<String>();
        int x = 0;
        int y = 0;
        int roboX = 0;
        int roboY = 0;
        int turn = 0;

        while ((string = input.readLine()) != null){
            char[] symbol = new char[string.length()];
            for (int i=0; i<string.length(); i++){
                symbol[i] = string.charAt(i);
                String symbolString = Character.toString(symbol[i]);

                if (turn == 0){
                    switch (symbolString) {
                        case "<" -> x -= 1;
                        case ">" -> x += 1;
                        case "v" -> y -= 1;
                        case "^" -> y += 1;
                    }
                    coordinates.add(x+","+y);
                    turn += 1;
                }

                else if (turn == 1){
                    switch (symbolString) {
                        case "<" -> roboX -= 1;
                        case ">" -> roboX += 1;
                        case "v" -> roboY -= 1;
                        case "^" -> roboY += 1;
                    }
                    turn -= 1;
                    coordinates.add(roboX+","+roboY);
                }
            }
            HashSet<String> uniqueCoordinates = new HashSet<String>(coordinates);
            System.out.println(uniqueCoordinates.size());
        }
        input.close();
    }
}