#include <stdio.h>


#define SIZE 9

// Function to print the Sudoku grid
void printGrid(int grid[SIZE][SIZE]) {
    printf("\n      1 2 3   4 5 6   7 8 9\n");
    printf("    -------------------------\n");
    for (int row = 0; row < SIZE; row++) {
        if (row > 0 && row % 3 == 0) {
            printf("    |-------+-------+-------|\n");
        }
        printf(" %d  | ", row + 1);
        for (int col = 0; col < SIZE; col++) {
            if (col > 0 && col % 3 == 0) {
                printf("| ");
            }
            if (grid[row][col] == 0) {
                printf(". ");
            } else {
                printf("%d ", grid[row][col]);
            }
        }
        printf("|\n");
    }
    printf("    -------------------------\n");
}

// Function to check if it's safe to place a number in a given position
int isSafe(int grid[SIZE][SIZE], int row, int col, int num) {
    // Check row
    for (int x = 0; x < SIZE; x++) {
        if (grid[row][x] == num) return 0; // false
    }

    // Check column
    for (int x = 0; x < SIZE; x++) {
        if (grid[x][col] == num) return 0; // false
    }

    // Check 3x3 box
    int startRow = row - row % 3;
    int startCol = col - col % 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (grid[i + startRow][j + startCol] == num) return 0; // false
        }
    }

    return 1; // true
}

// Function to check if the grid is completely filled
int isFull(int grid[SIZE][SIZE]) {
    for (int row = 0; row < SIZE; row++) {
        for (int col = 0; col < SIZE; col++) {
            if (grid[row][col] == 0) return 0; // false
        }
    }
    return 1; // true
}

int main() {
    // Initial Sudoku puzzle (0 represents empty cells)
    int grid[SIZE][SIZE] = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}
    };

    // To keep track of initial numbers (so they can't be changed)
    int initial[SIZE][SIZE];
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            initial[i][j] = (grid[i][j] != 0);
        }
    }

    int row, col, num;
    printf("--- Welcome to Sudoku! ---\n");
    printf("Enter coordinates (row col) and value (1-9) to play.\n");
    printf("Example: '1 3 4' to put 4 in row 1, column 3.\n");
    printf("Enter '0 0 0' to exit.\n");

    while (!isFull(grid)) {
        printGrid(grid);
        printf("\nEnter row col val: ");
        if (scanf("%d %d %d", &row, &col, &num) != 3) {
            printf("Invalid input format. Try again.\n");
            while (getchar() != '\n'); // Clear buffer
            continue;
        }

        if (row == 0 && col == 0 && num == 0) break;

        // Adjust for 0-indexing
        row--; col--;

        if (row < 0 || row >= SIZE || col < 0 || col >= SIZE || num < 0 || num > 9) {
            printf("Invalid input! Row/Col should be 1-9 and Value 0-9.\n");
            continue;
        }

        if (initial[row][col]) {
            printf("Cannot change initial values!\n");
            continue;
        }

        if (num == 0) {
            grid[row][col] = 0;
            printf("Cell cleared.\n");
            continue;
        }

        if (isSafe(grid, row, col, num)) {
            grid[row][col] = num;
            printf("Move accepted.\n");
        } else {
            printf("Invalid move! Rule violation (row, col, or box).\n");
        }
    }

    if (isFull(grid)) {
        printGrid(grid);
        printf("\nCongratulations! You solved the Sudoku!\n");
    } else {
        printf("\nGame exited. Goodbye!\n");
    }

    return 0;
}
