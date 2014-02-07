import java.util.List;
import java.util.ArrayList;
import java.math.BigInteger;

public class Problem3 {

static BigInteger val = new BigInteger("600851475143");
static BigInteger root_val = new BigInteger("775147");
static BigInteger zero = new BigInteger("0");


static BigInteger nextPrime(List<BigInteger> primes) {
	if (primes.size() == 0) return new BigInteger("2");

	BigInteger i = primes.get(primes.size() - 1);
	i = i.add(new BigInteger("1"));


	boolean found = false;

	while (!found) {
		boolean prime = true;
		for (BigInteger p : primes) {
			if (i.mod(p).equals(zero)) {
				prime = false;
			}
		}	
		if (prime) found = true;
		if (!found) i = i.add(new BigInteger("1")); 
	}

	return i;
}

static BigInteger largestPrimeFactor() {
	List<BigInteger> primes = new ArrayList<BigInteger>();

	BigInteger largestSeen = zero;
	BigInteger p = zero;
	while (p.compareTo(root_val) < 0) {
		p = nextPrime(primes);
		if (val.mod(p).equals(zero)) largestSeen = p;
		primes.add(p);
	}	
	return largestSeen;
}

public static void main(String[] args) {
	System.out.println(largestPrimeFactor());
}
}
