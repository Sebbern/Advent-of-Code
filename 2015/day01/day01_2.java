import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class day01_2 {
    public static void main(String[] args) throws Exception {
        File inputtxt = new File("C:\\Users\\sebas\\Advent-of-Code\\2015\\day01\\input.txt");
        BufferedReader input  = new BufferedReader(new FileReader(inputtxt));
        String string;
        int floor = 0;

        while ((string = input.readLine()) != null){
            char[] symbol = new char[string.length()];
            for (int i=0; i<string.length(); i++){
                symbol[i] = string.charAt(i);
                String test = Character.toString(symbol[i]);
                if (test.equals("(")){
                    floor += 1;
                }
                else {
                    floor -= 1;
                }

                if (floor == -1){
                    System.out.println(i+1);
                    break;
                }
            }
        }
    }
}
