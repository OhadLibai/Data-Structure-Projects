import java.util.Random;

public class LPHashTable extends OAHashTable {
	ModHash modi;

	
	public LPHashTable(int m, long p) {
		super(m);
		this.modi =ModHash.GetFunc(m,p);

	}
	
	@Override
	public int Hash(long x, int i) {
		int r = modi.Hash(x);
		int tor = (r + i)%m;
		return tor;
	}
	
}
