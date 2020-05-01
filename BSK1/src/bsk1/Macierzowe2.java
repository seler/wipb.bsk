package bsk1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class Macierzowe2 {
    private static String text;
    private static String keytext;
    private static ArrayList<Integer> key         = new ArrayList<Integer>();
    private static ArrayList<Integer> sortedKey   = new ArrayList<Integer>();
    private static ArrayList<String>  stringArray = new ArrayList<String>();

    public static void getText(String in){ text = in.replace(" ",""); }
    public static void getKey(String in){
        key.clear();
            int y = 1;
            char[] kl = new char[in.length()];
            in = in.replace(" ","");
            keytext = in;
            kl = in.toCharArray();
            int[] kk = new int[in.length()];
            for (char i = 'A'; i < 'z'; i++) {
                for (int j = 0; j < in.length(); j++) {
                    if (kl[j] == i) { kk[j] = y; y++; }
                }
            }
         for(int i : kk){ key.add(i); }
         sortedKey = (ArrayList)key.clone();
         Collections.sort(sortedKey);
    }
    public static void showKey(){
        for(int i : key) System.out.print(i + " - ");
    }
    private static void makeArray_toEncode(){
        for(int i=0; i<key.size();i++) stringArray.add("");
        
        int licznik = 0;
        while(licznik < text.length()){
            for(int i : key){
                if(licznik < text.length()) stringArray.set(i-1, stringArray.get(i-1)+text.charAt(licznik));
                licznik++;
            }
        }
    }
    private static void makeArray_toDecode(){
        for(int i=0; i<key.size();i++) stringArray.add("");
        String textCopy = text.substring(0, text.length());
        
        int reszta     = (text.length()%key.size());
        int stdrozmiar = text.length()/key.size();

        for(int i : sortedKey){
            int rozmiar = stdrozmiar;
            if(reszta>0){ rozmiar++; reszta--; }
            stringArray.set(i-1, textCopy.substring(0, rozmiar)  );
            textCopy = textCopy.replace( textCopy.substring(0,rozmiar), "");
        }
    }
    public static void showArray(){
        System.out.println("\n");
        for(String s : stringArray) System.out.println("|"+s);
    }
    private static Boolean sprawdzKlucz(String klucz){
        Boolean ret = true;
        for(char c : klucz.toCharArray()){
            if( (c<65) || ((c>90)&&(c<97)) || (c>122) ) ret=false;
        }
        return ret;
    }
    private static String Encoded(){
        String ret = "";
        for(int i : sortedKey){
            ret += stringArray.get(i-1);
        }
        return ret;
    }
    private static String Decoded(){
        String ret = "";
        int reszta     = (text.length()%key.size());
        int stdrozmiar = text.length()/key.size();
        
        int end = stdrozmiar;
        if(reszta>0) end++;
        int rlicznik= 0;
        int licznik = 0;
            while(licznik < end){
                for(int i : key){
                    if(licznik < stdrozmiar) ret += stringArray.get(i-1).charAt(licznik);
                    else{
                        if(rlicznik<reszta){ ret += stringArray.get(i-1).charAt(licznik); rlicznik++; }
                    }
                }
                licznik++;
            }
        
        return ret;
    }
    public static String Encrypt(){
        makeArray_toEncode();
        return Encoded();
    }
    public static String Decrypt(){
        makeArray_toDecode();
        return Decoded();
    }
    
    public static void clear(){
        text = new String();
        key = new ArrayList<Integer>();
        sortedKey = new ArrayList<Integer>();
        stringArray = new ArrayList<String>();
    }
}