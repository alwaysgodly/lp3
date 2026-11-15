import java.util.Scanner;

public class EightQueens {
    private static final int N = 8;
    private static final int[] queenColumn = new int[N];

    // Checks whether a queen can be placed at (row, col).
    static boolean isSafe(int row, int col) {
        for (int previousRow = 0; previousRow < row; previousRow++) {
            int previousCol = queenColumn[previousRow];

            if (previousCol == col) return false; // Same column

            if (Math.abs(previousRow - row) == Math.abs(previousCol - col)) {
                return false; // Same diagonal
            }
        }
        return true;
    }

    // Places queens row by row using backtracking.
    static boolean solve(int row) {
        if (row == N) return true;

        for (int col = 0; col < N; col++) {
            if (isSafe(row, col)) {
                queenColumn[row] = col;

                if (solve(row + 1)) return true;

                queenColumn[row] = -1; // Backtrack
            }
        }
        return false;
    }

    static void printBoard() {
        System.out.println("\nSolution:");
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < N; col++) {
                System.out.print(queenColumn[row] == col ? "Q " : ". ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < N; i++) queenColumn[i] = -1;

        System.out.println("Enter the first queen's position (row and column, 1-8):");
        int firstRow = sc.nextInt() - 1;
        int firstCol = sc.nextInt() - 1;

        if (firstRow < 0 || firstRow >= N || firstCol < 0 || firstCol >= N) {
            System.out.println("Invalid position. Row and column must be from 1 to 8.");
            return;
        }

        // Fix the given queen and solve the remaining rows.
        queenColumn[firstRow] = firstCol;

        // Validate fixed queen against any earlier rows (none are fixed).
        boolean found = solveFromFixedRow(0, firstRow);

        if (found) {
            printBoard();
        } else {
            System.out.println("No solution exists for the given first queen position.");
        }
        sc.close();
    }

    static boolean solveFromFixedRow(int row, int fixedRow) {
        if (row == N) return true;

        if (row == fixedRow) {
            // The fixed queen must also be safe relative to queens in earlier rows.
            if (!isSafe(row, queenColumn[row])) return false;
            return solveFromFixedRow(row + 1, fixedRow);
        }

        for (int col = 0; col < N; col++) {
            if (isSafe(row, col)) {
                queenColumn[row] = col;
                if (solveFromFixedRow(row + 1, fixedRow)) return true;
                queenColumn[row] = -1;
            }
        }
        return false;
    }
}
