import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Day03_2 {
    private static char loop(char[] a, char[] b, char[] c){
        for (char i: a){
            for (char u: b){
                if (i == u){
                    for (char y: c){
                        if (u == y){
                            return y;
                        }
                    }
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) throws IOException{
        File inputTxt = new File("2022\\day03\\input.txt");
        BufferedReader input = new BufferedReader(new FileReader(inputTxt));
        String string;
        ArrayList<String> rucksackList = new ArrayList<>();

        while ((string = input.readLine()) != null){
            rucksackList.add(string);
        }
        input.close();

        String a, b, c;
        char[] chA, chB, chC;
        int prioritySum = 0; 
        int value;

        for (int i = 0, u = 1, y = 2; y<rucksackList.size(); i += 3, u += 3, y += 3){
            a = rucksackList.get(i);
            b = rucksackList.get(u);
            c = rucksackList.get(y);
            chA = a.toCharArray();
            chB = b.toCharArray();
            chC = c.toCharArray();

            value = loop(chA, chB, chC);
            if (65 <= value && value <= 90){
                value -= 38;
            }
            else if (97 <= value && value <= 122){
                value -= 96;
            }

            prioritySum += value;
        }
        System.out.println(prioritySum);
    }
}
