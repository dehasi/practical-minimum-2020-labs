package me;

public class Ascii {
    public static void main(String[] args) {

        System.out.printf("%c\n", 'a' - ' ');
        System.out.printf("%c\n", 'A' ^ ' ');
        System.out.printf("%c\n", 'a' ^ ' ');
        char c = '9';
        System.out.printf("%d: %d", (int)c, c - '0');

//        System.out.println("\n\u0401");
//        System.out.println("\n\u0415 \u0308");
//
//        System.out.println("\u00e9"); // => é
//        System.out.println("\u0065 \u0301"); // => é
//        System.out.println("\u00e9".equals("\u0065\u0301")); // => false
//        System.out.println("\u00e9".length()); // => 1
//        System.out.println("\u0065\u0301".length()); // => 2
    }
}
