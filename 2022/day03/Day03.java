import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Day03 {
    private static char loop(char[] a, char[] b){
        for (char u: a){
            for (char y: b){
                if (u == y){
                    return u;
                }
            }
        }
        return 0;
    }

    private static String[] mid(String i){
        final int mid = i.length()/2;
        String[] split = {i.substring(0, mid), i.substring(mid)};
        return split;
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

        String a, b;
        String[] split;
        char[] chA, chB;
        int prioritySum = 0; 
        int value;

        for (String i: rucksackList){
            split = mid(i);
            a = split[0];
            b = split[1];
            chA = a.toCharArray();
            chB = b.toCharArray();

            value = loop(chA, chB);
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
