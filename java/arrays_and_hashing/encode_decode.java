import java.util.ArrayList;
import java.util.List;

public class encode_decode {

    // Encodes a list of strings to a single string.
   public String encode(List<String> strs) {
       StringBuilder encoded = new StringBuilder();
       for (String s : strs) {
           encoded.append(s.length()).append("-").append(s);
       }
       return encoded.toString();
   }

   // Decodes a single string to a list of strings.
   public List<String> decode(String s) {
       List<String> decoded = new ArrayList<>();
       int start = 0;

       while (start < s.length()) {
           int dashIndex = s.indexOf("-", start);
           int size = Integer.parseInt(s.substring(start, dashIndex));
           decoded.add(s.substring(dashIndex + 1, dashIndex + 1 + size));
           start = dashIndex + 1 + size;
       }

       return decoded;
   }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));