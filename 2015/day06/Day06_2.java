import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.HashMap;

public class Day06_2 {
    public static void main(String[] args) throws IOException{
        Path path = Paths.get("2015//day06//input.txt");
        List<String> input = Files.readAllLines(path);

        HashMap<Integer, Integer> grid = new HashMap<Integer, Integer>();

        Integer xStart, yStart;
        Integer xEnd, yEnd;
        String[] xySplit;

        for (Integer i = 0; i<(1000*1000); i++){
            grid.put(i,0);
        }

        for (String i : input) {
            String[] inputSplit = i.split(" ");

            if (inputSplit[0].equals("turn")){
                xySplit = inputSplit[2].split(",");
                xStart = Integer.parseInt(xySplit[0]); yStart = Integer.parseInt(xySplit[1]);
                xySplit = inputSplit[4].split(",");
                xEnd = Integer.parseInt(xySplit[0]); yEnd = Integer.parseInt(xySplit[1]);

                for (int y = yStart; y<=yEnd; y++){
                    for (int x = xStart; x<=xEnd; x++){
                        if (inputSplit[1].equals("on")){
                            grid.put(x+(y*1000),grid.get(x+(y*1000))+1);
                        }
                        else {
                            if (grid.get(x+(y*1000)) != 0){
                                grid.put(x+(y*1000),grid.get(x+(y*1000))-1);
                            }
                        }
                    }
                }
            }
            else {
                xySplit = inputSplit[1].split(",");
                xStart = Integer.parseInt(xySplit[0]); yStart = Integer.parseInt(xySplit[1]);
                xySplit = inputSplit[3].split(",");
                xEnd = Integer.parseInt(xySplit[0]); yEnd = Integer.parseInt(xySplit[1]);

                for (int y = yStart; y<=yEnd; y++){
                    for (int x = xStart; x<=xEnd; x++){
                        grid.put(x+(y*1000),grid.get(x+(y*1000))+2);
                    }
                }
            }
        }

        int count = 0;
        for (int i = 0; i<grid.size(); i++){
            count += grid.get(i);
        }

        System.out.println(count);
    }
}