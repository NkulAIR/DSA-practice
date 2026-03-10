import java.util.ArrayList;

public class Nkuli {
    public static void main(String[] args) {
        String greeting = "Hello Nkululeko - Welcome to Java\n";
        System.out.println(greeting);

        // Making an array - fixed size iterable / data structure
        // ArrayList<Integer> numbers = new ArrayList<>();
        // int len = numbers.length; 
        int[] numbers = {1,2,3,4,5};
        System.out.println(even(numbers));

    }
    public static int even(int[] numbers) {
        for (int i = 0; i < numbers.length ;i++) {
            if (i % 2 == 0) {
                System.out.println(numbers[i]);
            }
            return numbers.length;

        }

    }
    public static int add(int a, int b) {
        return a + b;
    }

}