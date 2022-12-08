import java.io.IOException;
import java.nio.file.*;
import java.util.*;

public class Day08 {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("2022//Day08//input.txt");
        List<String> input = Files.readAllLines(path);
        String[] split;
        String[] split2;
        int up = 0;
        int down = 0;
        int left = 0;
        int right = 0;
        int center = 0;
        int visible = 0;

        for (int x = 0; x<input.size(); x++){
            split = input.get(x).split("");
            if (x == 0 || x == input.size()-1){
                visible += split.length;
            }
            else{
                for (int y = 0; y<split.length; y++){
                    if (y == 0 || y == split.length-1){
                        visible += 1;
                    }
                    
                    else {
                        up = 0;
                        down = 0;
                        left = 0;
                        right = 0;

                        center = Integer.parseInt(split[y]);

                        for (int count = x-1; count>=0; count--){
                            split2 = input.get(count).split("");
                            if (up < Integer.parseInt(split2[y])){
                                up = Integer.parseInt(split2[y]);
                            }
                        }

                        for (int count = x+1; count<input.size(); count++){
                            split2 = input.get(count).split("");
                            if (down < Integer.parseInt(split2[y])){
                                down = Integer.parseInt(split2[y]);
                            }
                        }

                        for (int count = 0; count<split.length; count++){
                            if (count < y){
                                if (left < Integer.parseInt(split[count])){
                                    left = Integer.parseInt(split[count]);
                                }
                            }

                            else if (count > y){
                                if (right < Integer.parseInt(split[count])){
                                    right = Integer.parseInt(split[count]);
                                }
                            }
                        }

                        if (center > up || center > down || center > left || center > right){
                            visible += 1;
                        }
                    }
                }
            }
        }
        System.out.println(visible);
    }
}