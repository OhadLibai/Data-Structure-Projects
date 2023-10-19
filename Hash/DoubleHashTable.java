import java.util.Random;

public class DoubleHashTable extends OAHashTable {
	ModHash modi;
	ModHash modiaa;
	
	public DoubleHashTable(int m, long p) {
		super(m);
		this.modi =ModHash.GetFunc(m,p);
		this.modiaa =ModHash.GetFunc(m-1,p);
	}
	
	@Override
	public int Hash(long x, int i) {
		int r = modi.Hash(x);
		long rr =r;
		int l = modiaa.Hash(x)+1;
		long ll =l;
		long ii =i;
		long tor = (rr + (ii*ll))%m;
		int kk = (int)tor;
		return kk;
	}
	
}
