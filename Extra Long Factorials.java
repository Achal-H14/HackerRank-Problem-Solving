// https://www.hackerrank.com/challenges/extra-long-factorials/problem

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'extraLongFactorials' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

    public static void extraLongFactorials(int n) {
    // Write your code here
        if(n > 2){
            BigInteger res = new BigInteger("1"); 
        
            for(int i=n; i>1; i--){
                res = res.multiply(BigInteger.valueOf(i));
            }
                
            System.out.println(res);
        }
        else{
            System.out.println(n);
        }
        
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        Result.extraLongFactorials(n);

        bufferedReader.close();
    }
}
