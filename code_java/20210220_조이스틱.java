import java.util.*;

class Solution {
    public int solution(String name) {
        int answer = 0;
        int first = 0;
        int last = 0;
        int index = 0;

        for (int i=0; i<name.length(); i++){

            if(name.charAt(i)-'A' > 'Z'-name.charAt(i)+1) {
                answer+='Z'-name.charAt(i)+1;
            }else{
                answer+=name.charAt(i)-'A';
            }

        }
        
        int length = name.length();
        int min = name.length();
        for(int i=0;i<name.length();i++){
            int next=i+1;
            while(next<length && name.charAt(next)=='A'){
                next++;
            }
            min=Math.min(min,i+length-next+Math.min(i,length-next));
        }

        return answer+min;
    }
}