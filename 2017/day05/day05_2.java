import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class day05_2 {
    public static void main(String[] args) throws FileNotFoundException, IOException
     {
        File inputtxt = new File("2017\\day05\\input.txt");
        BufferedReader input = new BufferedReader(new FileReader(inputtxt));
        String text;
        ArrayList<String> labyrinth = new ArrayList<String>();
        int steps = 0;
        int idx = 0;
        while ((text = input.readLine()) != null){
            labyrinth.add(text);
        }
        
        try{
            for (int i=Integer.parseInt(labyrinth.get(idx)); i<labyrinth.size(); i=Integer.parseInt(labyrinth.get(idx))){
                steps += 1;
                if(Integer.parseInt(labyrinth.get(idx)) < 3){
                    labyrinth.set(idx, Integer.toString((Integer.parseInt(labyrinth.get(idx))+1)));
                }
                else {
                    labyrinth.set(idx, Integer.toString((Integer.parseInt(labyrinth.get(idx))-1)));
                }
                idx += i;
            }
        }
        catch (IndexOutOfBoundsException e){
            System.out.println(steps);
        }
    input.close();
    }
}
