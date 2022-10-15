import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;


public class day02_2 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        File inputtxt = new File("2015\\day02\\input.txt");
        BufferedReader input = new BufferedReader(new FileReader(inputtxt));
        String string;
        int sum = 0;

        while ((string = input.readLine()) != null){
            String[] box = string.split("x");
            int x = Integer.parseInt(box[0]);
            int y = Integer.parseInt(box[1]);
            int z = Integer.parseInt(box[2]);
            sum += ((x*y*z)+Math.min(Math.min((x+x+y+y), (y+y+z+z)), (x+x+z+z)));
        }
        System.out.println(sum);
        input.close();
    }
}
