import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/spiral-matrix/

class Solution {

    // Simulate going through a spiral in the matrix
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ret = new ArrayList<Integer>();
        // Keep track of which squares have been visited
        boolean[][] visited = new boolean[matrix.length][matrix[0].length];
        int i = 0;
        int j = 0;
        int hDiff = 1;
        int vDiff = 0;
        int counter = matrix.length * matrix[0].length;
        for (int k = counter - 1; k >= 0; k--) {
            visited[i][j] = true;
            ret.add(matrix[i][j]);

            // going to the right and hitting either a visited space or a rightmost space
            if (hDiff == 1 && (j == matrix[0].length - 1 || visited[i][j+1])) {
                hDiff = 0;
                vDiff = 1;
            }
            // going to the left and hitting either a visited space or a leftmost space
            if (hDiff == -1 && (j == 0  || visited[i][j-1])) {
                hDiff = 0;
                vDiff = -1;
            }
            // going up and hitting either a visited space or a top space
            if (vDiff == 1 && (i == matrix.length - 1 || visited[i+1][j])) {
                hDiff = -1;
                vDiff = 0;
            }
            // going down and hitting either a visited space or a bottom space
            if (vDiff == -1 && (i == 0 || visited[i-1][j])) {
                hDiff = 1;
                vDiff = 0;
            }
            i += vDiff;
            j += hDiff;

        }
        return ret;
    }
}