import java.util.Scanner;
class OrganicChemistry{
    public boolean lewisAcid(boolean a, boolean b){
        if(a==true && b==true){
            return true;
        }
        else{
            return false;
        }
    }
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        System.out.println("is the compound electron-deficient?");        
        boolean a=sc.nextBoolean();
        System.out.println("does the compound have tendency to accept electron?");
        boolean b=sc.nextBoolean();

        OrganicChemistry obj=new OrganicChemistry();
        if(obj.lewisAcid(a, b)==true){
            System.out.println("Compound is lewis acid");
        }
        else{
            System.out.println("Compond is not a lewis acid");
        }
        
    }
}