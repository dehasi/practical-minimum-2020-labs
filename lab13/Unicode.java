package me;

public class Unicode {

    public static void main(String[] args) {
        System.out.println("𝄞" + " " + "𝄞".length());
        System.out.println("𐋄" + " " + "𐋄".length());
        System.out.println("⏰" + " " + "⏰".length());
        System.out.println("🏭" + " " + "🏭".length());
        System.out.println("🏖" + " " + "🏖".length());

        String life = "🏭" + "🏖";
        System.out.println(life);
        System.out.println(reverse(life));
        System.out.println(reverse(reverse(life)));
    }

    static String reverse(String string) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = string.length() - 1; i >= 0; i--) {
            stringBuilder.append(string.charAt(i));
        }
        return stringBuilder.toString();
    }
}
