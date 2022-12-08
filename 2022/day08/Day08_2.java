import java.io.IOException;
import java.nio.file.*;
import java.util.*;

public class Day08_2 {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("2022//Day08//input.txt");
        List<String> input = Files.readAllLines(path);
        String[] split;
        String[] split2;
        int center = 0;

        int scenicSum = 0;
        int scenicUp = 0;
        int scenicDown = 0;
        int scenicLeft = 0;
        int scenicRight = 0;

        for (int x = 0; x<input.size(); x++){
            split = input.get(x).split("");

            if (!(x == 0 || x == input.size()-1)){
                for (int y = 0; y<split.length; y++){
                    if (!(y == 0 || y == split.length-1)){
                        scenicUp = 0;
                        scenicDown = 0;
                        scenicLeft = 0;
                        scenicRight = 0;

                        center = Integer.parseInt(split[y]);

                        for (int count = x-1; count>=0; count--){
                            split2 = input.get(count).split("");
                            if (center <= Integer.parseInt(split2[y])){
                                scenicUp += 1;
                                break;
                            }
                            else {
                                scenicUp += 1;
                            }
                        }

                        for (int count = x+1; count<input.size(); count++){
                            split2 = input.get(count).split("");
                            if (center <= Integer.parseInt(split2[y])){
                                scenicDown += 1;
                                break;
                            }
                            else {
                                scenicDown += 1;
                            }
                        }

                        for (int count = y-1; count>=0; count--){
                            if (center <= Integer.parseInt(split[count])){
                                scenicLeft += 1;
                                break;
                            }
                            else {
                                scenicLeft += 1;
                            }
                        }

                        for (int count = y+1; count<split.length; count++){
                            if (center <= Integer.parseInt(split[count])){
                                scenicRight += 1;
                                break;
                            }
                            else {
                                scenicRight += 1;
                            }
                        }
                        
                        if (scenicSum < (scenicUp*scenicDown*scenicLeft*scenicRight)){
                            scenicSum = scenicUp*scenicDown*scenicLeft*scenicRight;
                        }
                    }
                }
            }
        }
        System.out.println(scenicSum);
    }
}