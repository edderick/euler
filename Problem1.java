public class Problem1 {
	static int sumThreeOrFive() {
		int sum =0;

		for (int i = 0; i < 1000; i++) {
			if ((i % 5 == 0) || (i % 3 == 0)) {
				sum += i;
			}  
		}
		return sum;
	}

	public static void main(String[] args) {

		System.out.println(sumThreeOrFive());

	}

}
