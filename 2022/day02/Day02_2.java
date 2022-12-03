import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Day02_2 {
    public static void main(String[] args) throws IOException {
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
                case "X": 
                    points += 0;
                    switch (x){
                        case "A": points += 3; break;
                        case "B": points += 1; break;
                        case "C": points += 2; break;
                    }
                    break;
                case "Y": 
                    points += 3; 
                    switch (x){
                        case "A": points += 1; break;
                        case "B": points += 2; break;
                        case "C": points += 3; break;
                    }
                    break;
                case "Z": 
                    points += 6;
                    switch (x){
                        case "A": points += 2; break;
                        case "B": points += 3; break;
                        case "C": points += 1; break;
                    }
                    break;
            }
        }
        System.out.println(points);
    }
}
