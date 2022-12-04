import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Day04 {
    private static int check(String x, String y){
        int elfOneLow,elfOneHigh,elfTwoLow,elfTwoHigh;
        String[] xSplit, ySplit;
        xSplit = x.split("-");
        ySplit = y.split("-");
        elfOneLow = Integer.parseInt(xSplit[0]);
        elfOneHigh = Integer.parseInt(xSplit[1]);
        elfTwoLow = Integer.parseInt(ySplit[0]);
        elfTwoHigh = Integer.parseInt(ySplit[1]);

        if (((elfTwoLow <= elfOneLow) && (elfOneHigh <= elfTwoHigh)) || ((elfOneLow <= elfTwoLow) && (elfTwoHigh <= elfOneHigh))){
            return 1;
        }
        else{
            return 0;
        }
        
    }

    public static void main(String[] args) throws IOException{
        File inputTxt = new File("2022\\day04\\input.txt");
        BufferedReader input = new BufferedReader(new FileReader(inputTxt));
        String string, x, y;
        ArrayList<String> assignmentList = new ArrayList<>();
        String[] split;

        while ((string = input.readLine()) != null){
            assignmentList.add(string);
        }
        input.close();
        int pairs = 0;

        for (String i: assignmentList){
            split = i.split(",");
            x = split[0];
            y = split[1];

            pairs += check(x,y);
        }
        System.out.println(pairs);
    }
}
