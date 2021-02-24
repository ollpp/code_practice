import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;

        Arrays.sort(citations);
        for (int i=citations.length-1; i>=0; i--){
            if (citations[i] > answer){
                answer += 1;
            }else {
                break;
            }
        }


        return answer;
    }
}