import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

class Exercise13_8 {
    public static List<Integer> getRandomSubset(List<Integer> list) {
        Random rand = new Random();
        List<Integer> sublist = new ArrayList<>();
        list.forEach(i -> {
            if (rand.nextInt(2) > 0) {
                sublist.add(i);
            }
        });
        return sublist;
    }

    public static void main(String[] args) {
        Integer[] integerArray = new Integer[] { 3, 1, 4, 1, 5, 9, 2, 6 };
        List<Integer> list = Arrays.asList(integerArray);
        for (int i = 0; i < 10; i++) {
            List<Integer> sublist = getRandomSubset(list);
            System.out.println(sublist);
        }
    }
}
