
public abstract class OAHashTable implements IHashTable {
	
	public HashTableElement [] table;
	public int m;
	public HashTableElement delted = new HashTableElement(-1,-1);
	
	public OAHashTable(int m) {
		this.table = new HashTableElement[m];
		this.m=m;
	}
	
	
	@Override
	public HashTableElement Find(long key) {
		for(int i =0;i<m+1;i++) {
			if (i == m) {
				return null;
			}
			int t = Hash(key,i);
			if(table[t]==null){
				return null;
			}
			if(table[t].GetKey()==key){
				return table[t];
			}
		}

	   return null;
	}
	
	@Override
	public void Insert(HashTableElement hte) throws TableIsFullException,KeyAlreadyExistsException {
		long key1 = hte.GetKey();
		for(int i =0;i<m+1;i++){
			if(i==m){
				throw new TableIsFullException(hte);
			}
			int t = Hash(key1,i);
			if(table[t]==null){
				table[t]=hte;
				break;
			}
			if(table[t].GetKey()==key1){
				throw new KeyAlreadyExistsException(hte);
			}
			if(table[t]==delted){
				if(this.Find(hte.GetKey()) !=null){
					throw new KeyAlreadyExistsException(hte);
				}
				table[t]=hte;
				break;
			}
		}
	}
	
	@Override
	public void Delete(long key) throws KeyDoesntExistException {
		for (int i =0; i<m+1;i++){
			if(i==m){
				throw new KeyDoesntExistException(key);
			}
			int t = Hash(key,i);
			if (table[t]==null){
				throw new KeyDoesntExistException(key);
			}

			if(table[t].GetKey()==key){
				table[t]=delted;
				break;
			}
		}
	}
	
	/**
	 * 
	 * @param x - the key to hash
	 * @param i - the index in the probing sequence
	 * @return the index into the hash table to place the key x
	 */
	public abstract int Hash(long x, int i);
}
