public class Fibonacci {
	public static void main(String[] args) {
		long a=1, b=1, c=a+b;
		System.out.println(a);
		System.out.println(b);
		while(c < 1e9){
			System.out.println(c);
			a = b;
			b = c;
			c = a + b;
		}
	}
}
