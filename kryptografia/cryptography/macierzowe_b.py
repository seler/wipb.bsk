

class MacierzoweB(object):
    text = ''
    key = []
    sortedKey = []
    stringArray = []

    def __init__(self):
        pass

    def setText(self, s):
        self.text = s.replace(" ", "")

    def setKey(self, s):
        self.key = []
        y = 1
        s = s.replace(" ", "")
        keytext = s[:]
        kk = [None for i in range(len(s))]
        i = ord('A')
        while i < ord('z'):
            for j in range(len(s)):
                if s[j] == chr(i):
                    kk[j] = y
                    y += 1
            i += 1
        for i in kk:
            self.key = kk
        self.sortedKey = self.key[:]
        self.sortedKey.sort()

    def makeArray_toEncode(self):
        for i in range(len(self.key)):
            self.stringArray.append("")

        licznik = 0
        while licznik < len(self.text):
            for i in self.key:
                if licznik < len(self.text):
                    self.stringArray[i - 1] += self.text[licznik]
                    licznik += 1

    def reverseKey(self):
        self.key.reverse()

    def czyCiagla(self):
        ret = True
        for i in range(self.maxKey()):
            if i + 1 not in self.key:
                ret = False
        return ret

    def sprawdzKlucz(self):
        ret = self.czyCiagla()

        for i in range(len(self.sortedKey)):
            if i == 0:
                tmp = self.sortedKey[i]
            if i > 0 and i < len(self.sortedKey) - 1:
                tmp = self.sortedKey[i]
                if tmp == self.sortedKey[i + 1]:
                    ret = False
        return ret

    def maxKey(self):
        return max(self.key)

    def countRows(self):
        ret = len(self.text) / self.maxKey()
        if len(self.text) % self.maxKey() > 0:
            ret += 1
        return ret

    def makeArray(self):
        i = 1
        max = self.maxKey()
        while len(self.stringArray) != self.countRows():
            first = i * max - max
            second = i * max
            if second > len(self.text):
                second = len(self.text)
            self.stringArray.append(self.text[first:second])
            i += 1

    def encrypted(self):
        ret = ""
        import ipdb; ipdb.set_trace()
        for i in self.sortedKey:
            ret += self.stringArray[i-1]
        return ret

    def decrypted(self):
        self.makeArray()
        ret = ''

        self.reverseKey()
        for s in self.stringArray:
            licznik = 0
            m = len(s)
            for i in self.key:
                if licznik < m:
                    j = i - 1
                    while (j >= m):
                        j -= 1
                    ret += s[j]
                    licznik += 1
        return ret

    def encrypt(self, string, key):
        self.clear()
        self.setText(string)
        self.setKey(key)
        self.makeArray_toEncode()
        return self.encrypted()

    def decrypt(self, string, key):
        self.clear()
        self.setText(string)
        self.setKey(key)
        return self.decrypted()

    def clear(self):
        self.text = ""
        self.key = []
        self.sortedKey = []
        self.stringArray = []

"""
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
"""
