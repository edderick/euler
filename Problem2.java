import java.util.ArrayList;

public class Problem2 {
	public static int sumEvenFibonacci() {

		ArrayList<Integer> fib = new ArrayList<Integer>();

		fib.add(1);
		fib.add(1);

		int i = 2;

		
		while (fib.get(fib.size() - 1) < 4000000) {
			fib.add(fib.get(i - 1) + fib.get(i - 2));
			i++;
		}

		fib.remove(fib.size() - 1);

		int sum = 0;
		for (Integer x : fib) {
			if (x % 2 == 0) {
				sum += x;
			}
		}

		return sum;
	}

	public static void main(String[] args) {
		System.out.println(sumEvenFibonacci());
	}

}
