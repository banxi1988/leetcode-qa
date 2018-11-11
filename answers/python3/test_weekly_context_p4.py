def test_wc110_p4():
    pass


"""
参考答案 from uwi
class Solution {
	    public int distinctSubseqII(String S) {
	        return distinctSubsequence(S.toCharArray(), 1000000007);
	    }

		public int distinctSubsequence(char[] a, int mod)
		{
			int n = a.length;
			int[] bucket = new int[26];
			Arrays.fill(bucket, -1);
			
			int cum = 0;
			for(int i = 0;i < n;i++){
				int v = cum;
				int ind = a[i]-'a';
				if(bucket[ind] == -1){
					v++;
				}else{
					v += mod - bucket[ind];
				}
				if(v >= mod)v -= mod;
				bucket[ind] = cum;
				cum += v;
				if(cum >= mod)cum -= mod;
			}
			return cum;
		}	}	

"""
