import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Day02 {
    public static void main(String[] args) throws IOException{
        File inputTxt = new File("2022\\day02\\input.txt");
        BufferedReader input = new BufferedReader(new FileReader(inputTxt));
        String string;
        String x, y;
        String[] split;

        ArrayList<String> xyzList = new ArrayList<>();

        while ((string = input.readLine()) != null){
            xyzList.add(string);
        }
        input.close();

        int points = 0;

        for (String i: xyzList){
            split = i.split(" ");
            x = split[0];
            y = split[1];

            switch (y){
                case "X": points += 1; break;
                case "Y": points += 2; break;
                case "Z": points += 3; break;
            }

            switch (y){
                case "X": y = "A"; break;
                case "Y": y = "B"; break;
                case "Z": y = "C"; break;
            }

            if (x.equals(y)){
                points += 3;
            }

            else if ((x.equals("A") && y.equals("B")) || (x.equals("B") && y.equals("C")) || (x.equals("C") && y.equals("A"))){
                points += 6;
            }

            else if ((x.equals("A") && y.equals("C")) || (x.equals("B") && y.equals("A")) || (x.equals("C") && y.equals("B"))){
                points += 0;
            }
        }
        System.out.println(points);
    }    
}
