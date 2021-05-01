// https://leetcode.com/problems/unique-paths-ii/

class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int dp[][] = new int[obstacleGrid.length][obstacleGrid[0].length];
        // base cases along first row and column

        // First column
        for (int i = 0; i < obstacleGrid.length; i++) {
            if (obstacleGrid[i][0] == 1) {
                for (int k = i; k < obstacleGrid.length; k++) {
                    dp[k][0] = 0;
                }
                break;
            }
            else {
                dp[i][0] = 1;
            }
        }

        // First row
        for (int j = 0; j < obstacleGrid[0].length; j++) {
            if (obstacleGrid[0][j] == 1) {
                for (int k = j; k < obstacleGrid[0].length; k++) {
                    dp[0][k] = 0;
                }
                break;
            }
            else {
                dp[0][j] = 1;
            }
        }

        // DP general case
        for (int i = 1; i < obstacleGrid.length; i++) {
            for (int j = 1; j < obstacleGrid[0].length; j++) {
                if (obstacleGrid[i][j] == 0) dp[i][j] = dp[i-1][j] + dp[i][j-1]; // Pascal's triangle
                else dp[i][j] = 0;
            }
        }
        return dp[obstacleGrid.length - 1][obstacleGrid[0].length - 1];
    }
}