package bsk1;

import java.util.ArrayList;

public class RailFence {
    
    public static String Encrypt(String plainText, int rail) {
        ArrayList<String> railFence = new ArrayList<String>();
        for (int i = 0; i < rail; i++) railFence.add("");
 
        int number = 0;
        int increment = 1;
        char[] arr = plainText.toCharArray();
    
        for(char c : arr)
        {
            if (number + increment == rail) increment = -1;
            else if (number + increment == -1) increment = 1;

            railFence.set(number, railFence.get(number)+c);
            number += increment;
        }
 
        String buffer = "";
        for(String s : railFence) buffer += s;
        return buffer;
    }

    public static String Decrypt(String cipherText, int rail) {
        int cipherLength = cipherText.length();
        ArrayList< ArrayList<Integer> > railFence = new ArrayList< ArrayList<Integer> >();
        for (int i = 0; i < rail; i++) 
            railFence.add(new ArrayList<Integer>());
 
        int number = 0;
        int increment = 1;
        for (int i = 0; i < cipherLength; i++)
        {
            if (number + increment == rail) increment = -1;
            else if (number + increment == -1) increment = 1;
            railFence.get(number).add(i);
            number += increment;
        }
 
        int counter = 0;
        char[] buffer = new char[cipherLength];
        for (int i = 0; i < rail; i++)
        {
            for (int j = 0; j < railFence.get(i).size(); j++)
            {
                buffer[ railFence.get(i).get(j) ] = cipherText.toCharArray()[counter];
                counter++;
            }
        }
 
        return new String(buffer);
    }
    
}
