import java.util.Random;

public class QPHashTable extends OAHashTable {
	ModHash modi;

	public QPHashTable(int m, long p) {
		super(m);
		this.modi =ModHash.GetFunc(m,p);
	}
	
	@Override
	public int Hash(long x, int i) {
		int r = modi.Hash(x);
		int tor = (r + (i*i))%m;
		return tor;

	}
}
