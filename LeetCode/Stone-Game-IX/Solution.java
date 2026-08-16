1class Solution {
2    public boolean stoneGameIX(int[] stones) {
3        int[] count=new int[3];
4for(int stone:stones)count[stone%3]++;
5if(count[0]%2==0)return count[1]>0&&count[2]>0;
6return Math.abs(count[1]-count[2])>2;
7    }
8}