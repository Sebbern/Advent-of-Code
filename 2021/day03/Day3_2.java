import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Day3_2 {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("2021//day03//input.txt");
        List<String> input = Files.readAllLines(path);

        int count = 0, zeroBinary = 0, oneBinary = 0,
        zeroBinaryO2 = 0, oneBinaryO2 = 0, zeroBinaryCO2 = 0, oneBinaryCO2 = 0;
        StringBuilder O2Binary = new StringBuilder();
        StringBuilder CO2Binary = new StringBuilder();
        boolean found = false, CO2 = false;

        while (count < input.get(0).length()){
            if (count == 0){
                for (String i : input) {
                    if (i.charAt(count) == '0'){
                        zeroBinary += 1;
                    }
                    else if (i.charAt(count) == '1'){
                        oneBinary += 1;
                    }
                }

                if (zeroBinary < oneBinary){
                    O2Binary.append(1);
                    CO2Binary.append(0);
                }
                else if (oneBinary < zeroBinary){
                    O2Binary.append(0);
                    CO2Binary.append(1);
                }
                    
            }
            else {
                for (String i : input) {
                    if (i.startsWith(O2Binary.toString())){
                        if (i.charAt(count) == '0'){
                            zeroBinaryO2 += 1;
                        }
                        else if (i.charAt(count) == '1'){
                            oneBinaryO2 += 1;
                        }
                    }
                    else if (i.startsWith(CO2Binary.toString()) && !CO2){
                        if (!found){
                            if (i.charAt(count) == '0'){
                                zeroBinaryCO2 += 1;
                            }
                            else if (i.charAt(count) == '1'){
                                oneBinaryCO2 += 1;
                            }
                        }
                        else {
                            CO2Binary.setLength(0);
                            CO2Binary.append(i);
                            CO2 = true;
                        }
                    }
                }

                if (zeroBinaryO2 < oneBinaryO2){
                    O2Binary.append(1);
                }
                else if (oneBinaryO2 < zeroBinaryO2){
                    O2Binary.append(0);
                }
                else if (oneBinaryO2 == zeroBinaryO2){
                    O2Binary.append(1);
                }

                if (!found){
                    if (zeroBinaryCO2 + oneBinaryCO2 != 1){
                        if (zeroBinaryCO2 < oneBinaryCO2){
                            CO2Binary.append(0);
                        }
                        else if (oneBinaryCO2 < zeroBinaryCO2){
                            CO2Binary.append(1);
                        }
                        else if (oneBinaryCO2 == zeroBinaryCO2){
                            CO2Binary.append(0);
                        }
                    }
                    else {
                        found = true;
                    }
        
                }
            }

            zeroBinaryO2 = 0; oneBinaryO2 = 0;
            if (!found){
                zeroBinaryCO2 = 0; oneBinaryCO2 = 0;
            }
            count++;
        }

        System.out.println(Integer.parseInt(O2Binary.toString(), 2) * Integer.parseInt(CO2Binary.toString(), 2));
    }
}
