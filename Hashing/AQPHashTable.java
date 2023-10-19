import java.util.Random;
public class AQPHashTable extends OAHashTable {
	ModHash modi;

	public AQPHashTable(int m, long p) {
		super(m);
		this.modi =ModHash.GetFunc(m,p);
	}
	
	@Override
	public int Hash(long x, int i) {
		int r = modi.Hash(x);
		int yy = (int) Math.pow(i,2);
		int toret =0;
		if(i%2==0){
		return ((r+yy)% m);
		}
		else {
			if ((r - yy)%m < 0) {
				toret = ((r - yy) % m) + m;
			} else {
				toret = (r - yy) % m;
			}
		}

		return toret;
	}
}
