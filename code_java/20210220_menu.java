import java.util.*;

class Solution {

    List<Map<String, Integer>> FoodMaps = new ArrayList<>();
    int

    void comb(char[] arr, int pos, StringBuilder strBD){

        if(len()) {

            return;
        }

        comb(arr, pos+1, strBD.append(arr[0]));
        strBD.setLength(strBD.length()-1);
        comb(arr, pos+1, strBD);
    }

    public String[] solution(String[] orders, int[] course) {

        for (i=0; i<11; i++ ) {
            FoodMaps.add(new HashMap<String, Integer>());
        }

        for (String str : orders) {
            char[] arr = str.toCharArray();
            Arrays.sort(arr);
            comb
        }



        return answer;
    }
}