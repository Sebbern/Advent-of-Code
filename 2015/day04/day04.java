import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class day04 {
    public static void main(String[] args) throws UnsupportedEncodingException, NoSuchAlgorithmException {
        String input = "yzbqklnj";
        String hexa;
        String editedInput;
        int count = 0;
        
        while (true){
            editedInput = (input+count);
            byte[] bytesInput = editedInput.getBytes("UTF-8");
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] mdArray = md.digest(bytesInput);
            hexa = "";

            for (byte i : mdArray){
                hexa += String.format("%02x", i);
                if (!hexa.startsWith("0")){
                    break;
                }
            }
            
            // Task 1: (hexa.startsWith("00000")
            // Task 2: (hexa.startsWith("000000")
            if (hexa.startsWith("000000")){
                System.out.println(editedInput);
                System.out.println(hexa);
                System.out.println(count);
                System.exit(0);
            }
            count += 1;
        }
    }
}
