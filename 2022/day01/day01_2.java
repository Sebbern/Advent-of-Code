import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class day01_2 {
    public static void main(String[] args) throws IOException, FileNotFoundException{
        File inputTxt = new File("2022\\day01\\input.txt");
        BufferedReader input = new BufferedReader(new FileReader(inputTxt));
        String string;
        int caloriesFirst = 0, caloriesSecond = 0, caloriesThird = 0;
        ArrayList<Integer> caloriesList = new ArrayList<>();

        while ((string = input.readLine()) != null){
            if (string.isEmpty()){
                caloriesList.add(caloriesFirst);
                caloriesFirst = 0;
            }
            else {
                caloriesFirst += Integer.parseInt(string);
            }
        }
        input.close();

        for (int i = 0; i<caloriesList.size(); i++){
            if (caloriesFirst < caloriesList.get(i)){
                caloriesThird = caloriesSecond;
                caloriesSecond = caloriesFirst;
                caloriesFirst = caloriesList.get(i);
            }
            else if (caloriesFirst > caloriesList.get(i) && caloriesSecond < caloriesList.get(i)){
                caloriesThird = caloriesSecond;
                caloriesSecond = caloriesList.get(i);
            }
            else if (caloriesFirst > caloriesList.get(i) && caloriesSecond > caloriesList.get(i) && caloriesThird < caloriesList.get(i))
            {
                caloriesThird = caloriesList.get(i);
            }

        }


        System.out.println(caloriesFirst+caloriesSecond+caloriesThird);
    }
}
