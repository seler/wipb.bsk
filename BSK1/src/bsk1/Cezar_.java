package bsk1;

public class Cezar_ {
    public static char[] alf;
        
        public Cezar_() {
            int i=0;
            alf = new char[28];
            for (char a = 'a'; a <='z'; a++) {
                 
                alf[i] = a;
                i++;
            }
            alf[i] = '_';
            alf[i + 1] = ' ';
        }
        
        public String szyfruj_a(String napis, int k) {
            int p=0;
            char[] c = napis.toCharArray();
            String wynik = "";
            for (int i = 0; i < napis.length(); i++) { 
                for(int j=0;j<alf.length;j++){if(c[i]==alf[j])p=j;}
                wynik += alf[(p + k) % alf.length];

                
            }
        
        return wynik;
        }
        public String deszyfruj_a(String napis, int k)
        {
            int p = 0;
            char[] c = napis.toCharArray();
            String wynik = "";
            for (int i = 0; i < napis.length(); i++)
            {
                for (int j = 0; j < alf.length; j++) { if (c[i] == alf[j])p = j; }
                wynik += alf[(p + alf.length-k) % alf.length];


            }

            return wynik;
        }
        public String szyfruj_b(String napis, int k1,int k2)
        {
            int p = 0;
            char[] c = napis.toCharArray();
            String wynik = "";
            for (int i = 0; i < napis.length(); i++)
            {
                for (int j = 0; j < alf.length; j++) { if (c[i] == alf[j])p = j; }
                wynik += alf[(p*k2 + k1) % alf.length];


            }

            return wynik;
        }
      
        public String deszyfruj_b(String napis, int k1,int k2)
        {
            int p = 0;
            char[] c = napis.toCharArray();
            String wynik = "";
            int kk=0;
            int k22 = 1;
            int k11=(alf.length - k1)%28;
            for (int i = 1; i < 12; i++) {

                k22 *= k2;
                k22 %= 28;
            }
                for (int i = 0; i < napis.length(); i++)
                {
                    for (int j = 0; j < alf.length; j++) { if (c[i] == alf[j])p = j; }
                    kk = (((p +k11 ) * k22)%28+28)%28;
                                       
                    wynik += alf[kk];


                }

            return wynik;
        }
}
