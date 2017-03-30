import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int NumberOfElements = in.nextInt(); 
        long sum = 0L; // make it a long number! 

        for (int i = 0; i < NumberOfElements; i++) { 
        	sum += in.nextLong(); 

        }
        in.close(); 
        System.out.println(sum); 
    }
}