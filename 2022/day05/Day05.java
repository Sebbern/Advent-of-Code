import java.io.IOException;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

public class Day05 {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("2022//Day05//input.txt");
        List<String> input = Files.readAllLines(path);     
        int resume = 0;
        ArrayList<String> boxList = new ArrayList<>();
        ArrayList<Integer> idxList = new ArrayList<>();
        ArrayList<String> arrangedList = new ArrayList<>();

        for (int i = 0; i<input.size(); i++){
            if (input.get(i).equals("")){
                resume = i;
                break;
            }
        
            boxList.add(input.get(i));
        }

        for (int i = boxList.size()-1; i>=0; i--){
            if (i == boxList.size()-1){
                for (int idx = 0; idx<boxList.get(i).length(); idx++){
                    if((int)boxList.get(i).charAt(idx) >= 49 && (int)boxList.get(i).charAt(idx) <= 57){
                        idxList.add(idx);
                        arrangedList.add("");
                    }
                }
            }

            for (int u = 0; u<idxList.size(); u++){
                if(boxList.get(i).charAt(idxList.get(u)) != ' '){
                    arrangedList.set(u, arrangedList.get(u)+boxList.get(i).charAt(idxList.get(u)));
                }
            }
        }

        String[] split;
        String letters;
        int move, from, to;

        for (int i = resume+1; i<input.size(); i++){
            split = input.get(i).replaceAll("[^\\d.]", " ").strip().split("\\W+");
            move = Integer.parseInt(split[0]);
            from = Integer.parseInt(split[1]);
            to = Integer.parseInt(split[2]);
            letters = arrangedList.get(from-1);
            letters = letters.substring(letters.length()-move);
            
            StringBuffer reverse = new StringBuffer(letters);
            reverse.reverse();

            arrangedList.set(from-1, arrangedList.get(from-1).substring(0, arrangedList.get(from-1).length()-move));
            arrangedList.set(to-1, arrangedList.get(to-1)+reverse);
        }

        String result = "";
        
        for (int i = 0; i<arrangedList.size(); i++){
            result = result+arrangedList.get(i).substring(arrangedList.get(i).length()-1);
        }

        System.out.println(result);
    }
}
