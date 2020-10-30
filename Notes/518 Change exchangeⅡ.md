## 518 Change exchangeⅡ

显然是动态规划

但是好像会出现重叠问题

1：1

2：1+1，2

3：1+1+1，1+2（2又有两种）

### 美妙代码

```java
class Solution {
    public int change(int amount, int[] arr) {
        // 动态规划
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : arr) {
            for (int i = 0; i+coin <= amount; i++) {
                dp[i+coin] += dp[i];
            }
        }
        return dp[amount];
    }
}
```

