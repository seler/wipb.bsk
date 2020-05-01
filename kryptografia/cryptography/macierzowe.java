# -*- coding: utf-8 -*-

__author__ = "Rafał Selewońko <rafal@selewonko.com>"


class MacierzoweA(object):
    private static String text;
    private static ArrayList<Integer> key         = new ArrayList<Integer>();
    private static ArrayList<Integer> sortedKey   = new ArrayList<Integer>();
    private static ArrayList<String>  stringArray = new ArrayList<String>();

    public static void getText(String in){ text = in; }
    public static void getKey(String in){
         key.clear();
         String nums[] = in.split("-");
         for(String n : nums) key.add(Integer.parseInt(n));
         sortedKey = (ArrayList)key.clone();
         Collections.sort(sortedKey);
    }
    private static void reverseKey(){ Collections.reverse(key); }
    public static void showKey(){
        System.out.println("\nKlucz: ");
        for(Integer i : key) System.out.print(i+" ");
        System.out.println("\nPosortowany Klucz: ");
        for(Integer i : sortedKey) System.out.print(i+" ");
        
        System.out.print("\nMax: " + maxKey());
        System.out.print("\nCiagla: " + czyCiagla() + "\n");
    } 
    private static boolean czyCiagla(){
        boolean ret = true;
        for(int i=1;i<maxKey();i++)
            if(!key.contains(i)) ret= false;
        return ret;
    }
    private static boolean sprawdzKlucz(){
        boolean ret   = czyCiagla();
        boolean start = true;
        Integer tmp;
        
        for(int i=0;i<sortedKey.size();i++){
            if(i==0){
                tmp=sortedKey.get(i);
            }
            if((i>0)&&(i<sortedKey.size()-1)){
                tmp=sortedKey.get(i);
                if(tmp == sortedKey.get(i+1)) ret=false;
            }
        }
        return ret;
    }
    private static Integer maxKey(){ return Collections.max(key); }
    private static Integer countRows(){
        int ret = (text.length() / maxKey());
        if( (text.length()%maxKey()) > 0 ) ret += 1;
        return ret;
    }
    private static void makeArray(){
        int i   = 1;
        int max = maxKey();
        while(stringArray.size()!=countRows()){
            int first  = i*max - max;
            int second = i*max;
            if(second > text.length()) second = text.length();
            stringArray.add( text.substring(first, second) );
            i++;
        }
    }
    public static void showArray(){
        makeArray();
        for(Integer i : sortedKey) System.out.print(i);
        System.out.println("\n------------");
        for(String s: stringArray) System.out.println(s);
    }
    public static String Encrypted(){
        makeArray();
        String ret = "";
        for(String s : stringArray){
            char[] arr = s.toCharArray();
            for(Integer i : key){
                 if(arr.length > i-1)
                     ret += arr[i-1];
            }
        }
        return ret;
    }
    public static String Decrypted(){
        makeArray();
        String ret = "";
        reverseKey();
        for(String s : stringArray){
            char[] arr = s.toCharArray();
                if(arr.length > maxKey()-1){
                    for(Integer i : key){
                        //if(arr.length > i-1)
                            ret += arr[i-1];
                    }
                }
                else
                { 
                    int licznik=0;
                    int m = arr.length;
                    for(Integer i : key){
                        if(licznik<m){
                            int j = i-1;
                            while(j >= m) j--;
                            ret += arr[j];
                            licznik++;
                        }
                    }
                }
        }
        return ret;
    }
    
    public static String Encrypt(){
        if(sprawdzKlucz()==false) return "Blad ! Klucz nie jest ciagly albo zawiera duplikaty.\n";
        else return Encrypted();
    }
    public static String Decrypt(){
        if(sprawdzKlucz()==false) return "Blad ! Klucz nie jest ciagly albo zawiera duplikaty.\n";
        else return Decrypted();
    }
    
    public static void clear(){
        text = new String();
        key = new ArrayList<Integer>();
        sortedKey = new ArrayList<Integer>();
        stringArray = new ArrayList<String>();
    }
}
