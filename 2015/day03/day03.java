import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;

public class day03 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        File inputtxt = new File("2015\\day03\\input.txt");
        BufferedReader input = new BufferedReader(new FileReader(inputtxt));
        String string;
        ArrayList<String> coordinates = new ArrayList<String>();
        int x = 0;
        int y = 0;

        while ((string = input.readLine()) != null){
            char[] symbol = new char[string.length()];
            for (int i=0; i<string.length(); i++){
                symbol[i] = string.charAt(i);
                String symbolString = Character.toString(symbol[i]);

                if (symbolString.equals("<")){
                    x -= 1;
                }
                else if (symbolString.equals(">")){
                    x += 1;
                }
                else if (symbolString.equals("v")){
                    y -= 1;
                }
                else if (symbolString.equals("^")){
                    y += 1;
                }

                coordinates.add(x+","+y);
            }
            HashSet<String> uniqueCoordinates = new HashSet<String>(coordinates);
            System.out.println(uniqueCoordinates.size());
        }
        input.close();
    }
}