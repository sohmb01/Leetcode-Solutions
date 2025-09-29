// Problem ID: 802
// Title: K-th Smallest Prime Fraction
// Runtime: 334 ms

class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        
        PriorityQueue<int[]> pq = new PriorityQueue<> ((a,b) -> {
            double x = (double)b[0] / b[1];
            double y = (double)a[0] / a[1];
            if (x > y){
                return 1;
            }
            return -1;
        });

        for (int i = 0; i<arr.length;i++){
            for (int j = i+1; j<arr.length;j++){
                pq.offer(new int[] {arr[i],arr[j]});
                while (pq.size()>k){
                    pq.poll();
                }
            }
        }
        return pq.poll();
    }
}