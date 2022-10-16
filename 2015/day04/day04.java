import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class day04 {
    public static void main(String[] args) throws UnsupportedEncodingException, NoSuchAlgorithmException {
        String input = "yzbqklnj";
        StringBuilder hexa;
        String editedInput;
        int count = 0;
        
        while (true){
            editedInput = (input+count);
            byte[] bytesInput = editedInput.getBytes(StandardCharsets.UTF_8);
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] mdArray = md.digest(bytesInput);
            hexa = new StringBuilder();

            for (byte i : mdArray){
                hexa.append(String.format("%02x", i));
                if (!hexa.toString().startsWith("0")){
                    break;
                }
            }

            // Task 1: (hexa.toString().startsWith("00000")
            // Task 2: (hexa.toString().startsWith("000000")
            if (hexa.toString().startsWith("00000")){
                System.out.println(editedInput);
                System.out.println(hexa);
                System.out.println(count);
                System.exit(0);
            }
            count += 1;
        }
    }
}
