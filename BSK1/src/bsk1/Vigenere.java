package bsk1;

import java.util.ArrayList;

public class Vigenere {
    public static ArrayList<String> Tabela = new ArrayList<String>();

    public static void initTab(){
        Tabela.add("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        Tabela.add("BCDEFGHIJKLMNOPQRSTUVWXYZA");
        Tabela.add("CDEFGHIJKLMNOPQRSTUVWXYZAB");
        Tabela.add("DEFGHIJKLMNOPQRSTUVWXYZABC");
        Tabela.add("EFGHIJKLMNOPQRSTUVWXYZABCD");
        Tabela.add("FGHIJKLMNOPQRSTUVWXYZABCDE");
        Tabela.add("GHIJKLMNOPQRSTUVWXYZABCDEF");
        Tabela.add("HIJKLMNOPQRSTUVWXYZABCDEFG");
        Tabela.add("IJKLMNOPQRSTUVWXYZABCDEFGH");
        Tabela.add("JKLMNOPQRSTUVWXYZABCDEFGHI");
        Tabela.add("KLMNOPQRSTUVWXYZABCDEFGHIJ");
        Tabela.add("LMNOPQRSTUVWXYZABCDEFGHLJK");
        Tabela.add("MNOPQRSTUVWXYZABCDEFGHIJKL");
        Tabela.add("NOPQRSTUVWXYZABCDEFGHIJKLM");
        Tabela.add("OPQRSTUVWXYZABCDEFGHIJKLMN");
        Tabela.add("PQRSTUVWXYZABCDEFGHIJKLMNO");
        Tabela.add("QRSTUVWXYZABCDEFGHIJKLMNOP");
        Tabela.add("RSTUVWXYZABCDEFGHIJKLMNOPQ");
        Tabela.add("STUVWXYZABCDEFGHIJKLMNOPQR");
        Tabela.add("TUVWXYZABCDEFGHIJKLMNOPQRS");
        Tabela.add("UVWXYZABCDEFGHIJKLMNOPQRST");
        Tabela.add("VWXYZABCDEFGHIJKLMNOPQRSTU");
        Tabela.add("WXYZABCDEFGHIJKLMNOPQRSTUV");
        Tabela.add("XYZABCDEFGHIJKLMNOPQRSTUVW");
        Tabela.add("YZABCDEFGHIJKLMNOPQRSTUVWX");
        Tabela.add("ZABCDEFGHIJKLMNOPQRSTUVWXY");
    }
    
    private static Boolean checkLetters(String s){
        Boolean ret = false;
        char[] a = s.toCharArray();
        for(char c : a){
            if(Character.isLetter(c)) ret = true;
            else ret = false;
        }
        return ret;
    }
    
    public static Boolean isOK(String m, String k){
        Boolean ret = false;
        
        if ( (m.length()==k.length())&&(checkLetters(m))&&(checkLetters(k)) ) ret=true;
        else ret=false;
        
        return ret;
    }
    
    public static int toKey(char c){ return c - 65; }
    public static char toChar(int i){ return (char)(i + 65); }

    public static String Encode(String m, String k){
        String ret = "";
            m = m.toUpperCase();
            k = k.toUpperCase();
            
            if(k.length()<m.length()){
                int i = 0;
                int f = k.length()-1;
                
                while(k.length()<m.length()){
                    k += k.charAt(i);
                    i++;
                    if(i>f) i=0;
                }
            }
            
            for(int i=0; i<m.length(); i++){
                int iM = toKey(m.charAt(i));
                int iK = toKey(k.charAt(i));
                char c  = Tabela.get(iM).charAt(iK);
                ret += c;
            }
                    
        return ret;
    }

    public static String Decode(String m, String k){
        String ret = "";
            m = m.toUpperCase();
            k = k.toUpperCase();

            if(k.length()<m.length()){
                int i = 0;
                int f = k.length()-1;
                
                while(k.length()<m.length()){
                    k += k.charAt(i);
                    i++;
                    if(i>f) i=0;
                }
            }
            
            for(int i=0; i<m.length(); i++){
                int iM = toKey(m.charAt(i));
                int iK = toKey(k.charAt(i));
                
                char c  = toChar( Tabela.get(iK).indexOf(m.charAt(i)) );
                ret += c;
            }
        return ret;
    }
}