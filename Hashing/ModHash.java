import java.util.concurrent.ThreadLocalRandom;


public class ModHash {
	public long p;
	public long a;
	public long b;
	public int m;

	public ModHash(long p , int m, long a,long b){
		this.a =a;
		this.b=b;
		this.m=m;
		this.p=p;

	}
	
	public static ModHash GetFunc(int m, long p){
		if(p>1) {
			long a = ThreadLocalRandom.current().nextLong(1, p);
			long b = ThreadLocalRandom.current().nextLong(0, p);
			ModHash modi = new ModHash(p, m, a, b);

			return modi;
		}
		return null;
	}
	
	public int Hash(long key) {
		long tt = ((a*key + b)%p)%m;
		int k = (int)tt;
		return k;
	}
}
