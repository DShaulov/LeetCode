import java.util.HashMap;
public class TwoSumDict {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
           int checkKey = target - nums[i];
           if (map.containsKey(checkKey)) {
               if (map.get(checkKey) == i) {
                   continue;
               }
               int[] solution = new int[2];
               solution[0] = i;
               solution[1] = map.get(checkKey);
               return solution;
           }
        }
        return null;
    }
}
