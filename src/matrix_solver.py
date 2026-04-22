"""
Matrix Solver - A comprehensive Python module for matrix operations.
Supports: Transpose, Determinant, Inverse, Rank, Gaussian Elimination, Eigenvalues
"""

import copy
from typing import List, Tuple, Optional


class Matrix:
    """A class representing a mathematical matrix with various operations."""
    
    def __init__(self, data: List[List[float]]):
        """Initialize matrix with 2D list data."""
        if not data or not data[0]:
            raise ValueError("Matrix cannot be empty")
        
        self.rows = len(data)
        self.cols = len(data[0])
        
        # Validate all rows have same length
        if any(len(row) != self.cols for row in data):
            raise ValueError("All rows must have the same number of columns")
        
        self.data = [[float(val) for val in row] for row in data]
    
    def __repr__(self):
        return f"Matrix({self.rows}x{self.cols})"
    
    def __str__(self):
        """Pretty print the matrix with brackets."""
        result = []
        for i, row in enumerate(self.data):
            if i == 0:
                prefix = "⎡"
            elif i == self.rows - 1:
                prefix = "⎣"
            else:
                prefix = "⎢"
            
            if i == 0:
                suffix = "⎤"
            elif i == self.rows - 1:
                suffix = "⎦"
            else:
                suffix = "⎥"
            
            row_str = " ".join(f"{val:8.4f}" for val in row)
            result.append(f"{prefix} {row_str} {suffix}")
        
        return "\n".join(result)
    
    def get(self, row: int, col: int) -> float:
        """Get element at position (row, col)."""
        return self.data[row][col]
    
    def set(self, row: int, col: int, value: float):
        """Set element at position (row, col)."""
        self.data[row][col] = value
    
    def copy(self) -> 'Matrix':
        """Create a deep copy of this matrix."""
        return Matrix(copy.deepcopy(self.data))
    
    def transpose(self) -> 'Matrix':
        """Return the transpose of this matrix."""
        transposed = [[self.data[j][i] for j in range(self.rows)] 
                      for i in range(self.cols)]
        return Matrix(transposed)
    
    def determinant(self) -> float:
        """Calculate the determinant using LU decomposition."""
        if self.rows != self.cols:
            raise ValueError("Determinant only defined for square matrices")
        
        n = self.rows
        if n == 1:
            return self.data[0][0]
        
        if n == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        
        # Use LU decomposition with partial pivoting
        lu, piv = self._lu_decompose()
        
        det = 1.0
        for i in range(n):
            det *= lu.data[i][i]
            if piv[i] != i:
                det *= -1
        
        return det
    
    def _lu_decompose(self) -> Tuple['Matrix', List[int]]:
        """Perform LU decomposition with partial pivoting."""
        n = self.rows
        lu = self.copy()
        piv = list(range(n))
        
        for k in range(n):
            # Find pivot
            max_val = abs(lu.data[k][k])
            max_row = k
            for i in range(k + 1, n):
                if abs(lu.data[i][k]) > max_val:
                    max_val = abs(lu.data[i][k])
                    max_row = i
            
            # Swap rows
            if max_row != k:
                lu.data[k], lu.data[max_row] = lu.data[max_row], lu.data[k]
                piv[k], piv[max_row] = piv[max_row], piv[k]
            
            # Eliminate
            for i in range(k + 1, n):
                if lu.data[k][k] != 0:
                    factor = lu.data[i][k] / lu.data[k][k]
                    for j in range(k, n):
                        lu.data[i][j] -= factor * lu.data[k][j]
                    lu.data[i][k] = factor
        
        return lu, piv
    
    def inverse(self) -> Optional['Matrix']:
        """Calculate the inverse using Gauss-Jordan elimination."""
        if self.rows != self.cols:
            raise ValueError("Inverse only defined for square matrices")
        
        n = self.rows
        
        # Create augmented matrix [A|I]
        augmented = []
        for i in range(n):
            row = self.data[i][:] + [1.0 if j == i else 0.0 for j in range(n)]
            augmented.append(row)
        
        # Gauss-Jordan elimination
        for col in range(n):
            # Find pivot
            max_row = col
            for row in range(col + 1, n):
                if abs(augmented[row][col]) > abs(augmented[max_row][col]):
                    max_row = row
            
            augmented[col], augmented[max_row] = augmented[max_row], augmented[col]
            
            if abs(augmented[col][col]) < 1e-10:
                return None  # Singular matrix
            
            # Scale pivot row
            pivot = augmented[col][col]
            for j in range(2 * n):
                augmented[col][j] /= pivot
            
            # Eliminate column
            for row in range(n):
                if row != col:
                    factor = augmented[row][col]
                    for j in range(2 * n):
                        augmented[row][j] -= factor * augmented[col][j]
        
        # Extract inverse
        inverse_data = [row[n:] for row in augmented]
        return Matrix(inverse_data)
    
    def rank(self) -> int:
        """Calculate the rank using row echelon form."""
        matrix = self.copy()
        m, n = matrix.rows, matrix.cols
        
        rank = 0
        row = 0
        
        for col in range(n):
            if row >= m:
                break
            
            # Find pivot
            pivot_row = row
            for i in range(row + 1, m):
                if abs(matrix.data[i][col]) > abs(matrix.data[pivot_row][col]):
                    pivot_row = i
            
            if abs(matrix.data[pivot_row][col]) < 1e-10:
                continue
            
            # Swap rows
            matrix.data[row], matrix.data[pivot_row] = matrix.data[pivot_row], matrix.data[row]
            
            # Eliminate
            pivot = matrix.data[row][col]
            for i in range(row + 1, m):
                factor = matrix.data[i][col] / pivot
                for j in range(col, n):
                    matrix.data[i][j] -= factor * matrix.data[row][j]
            
            rank += 1
            row += 1
        
        return rank
    
    def gaussian_elimination(self, verbose: bool = False) -> Tuple['Matrix', List[str]]:
        """
        Perform Gaussian elimination to get row echelon form.
        Returns the resulting matrix and a log of steps performed.
        """
        matrix = self.copy()
        steps = []
        m, n = matrix.rows, matrix.cols
        
        row = 0
        for col in range(n):
            if row >= m:
                break
            
            # Find pivot
            pivot_row = row
            for i in range(row + 1, m):
                if abs(matrix.data[i][col]) > abs(matrix.data[pivot_row][col]):
                    pivot_row = i
            
            if abs(matrix.data[pivot_row][col]) < 1e-10:
                continue
            
            # Swap rows if needed
            if pivot_row != row:
                matrix.data[row], matrix.data[pivot_row] = matrix.data[pivot_row], matrix.data[row]
                if verbose:
                    steps.append(f"Step: Swap row {row + 1} with row {pivot_row + 1}")
            
            # Scale pivot row
            pivot = matrix.data[row][col]
            if abs(pivot - 1.0) > 1e-10:
                if verbose:
                    steps.append(f"Step: Divide row {row + 1} by {pivot:.4f}")
                for j in range(n):
                    matrix.data[row][j] /= pivot
            
            # Eliminate below
            for i in range(row + 1, m):
                factor = matrix.data[i][col]
                if abs(factor) > 1e-10:
                    if verbose:
                        steps.append(f"Step: R{i + 1} = R{i + 1} - ({factor:.4f}) × R{row + 1}")
                    for j in range(col, n):
                        matrix.data[i][j] -= factor * matrix.data[row][j]
            
            row += 1
        
        if verbose:
            steps.append("Gaussian elimination complete - Row Echelon Form achieved")
        
        return matrix, steps
    
    def solve(self, b: List[float]) -> Optional[List[float]]:
        """
        Solve the system Ax = b using Gaussian elimination.
        Returns the solution vector x, or None if no unique solution exists.
        """
        if self.rows != self.cols:
            raise ValueError("System must have square coefficient matrix")
        
        if len(b) != self.rows:
            raise ValueError("Vector b must have same length as matrix rows")
        
        n = self.rows
        
        # Create augmented matrix [A|b]
        augmented = [self.data[i][:] + [b[i]] for i in range(n)]
        
        # Forward elimination
        for col in range(n):
            # Find pivot
            max_row = col
            for row in range(col + 1, n):
                if abs(augmented[row][col]) > abs(augmented[max_row][col]):
                    max_row = row
            
            augmented[col], augmented[max_row] = augmented[max_row], augmented[col]
            
            if abs(augmented[col][col]) < 1e-10:
                return None  # No unique solution
            
            # Eliminate below
            for row in range(col + 1, n):
                factor = augmented[row][col] / augmented[col][col]
                for j in range(col, n + 1):
                    augmented[row][j] -= factor * augmented[col][j]
        
        # Back substitution
        x = [0.0] * n
        for i in range(n - 1, -1, -1):
            x[i] = augmented[i][n]
            for j in range(i + 1, n):
                x[i] -= augmented[i][j] * x[j]
            x[i] /= augmented[i][i]
        
        return x
    
    def eigenvalues_power_iteration(self, max_iterations: int = 1000, tolerance: float = 1e-6) -> Optional[Tuple[float, List[float]]]:
        """
        Find the dominant eigenvalue and eigenvector using power iteration.
        Returns (eigenvalue, eigenvector) or None if convergence fails.
        """
        if self.rows != self.cols:
            raise ValueError("Eigenvalues only defined for square matrices")
        
        n = self.rows
        # Start with random vector
        v = [1.0] * n
        
        for _ in range(max_iterations):
            # Multiply A * v
            Av = [sum(self.data[i][j] * v[j] for j in range(n)) for i in range(n)]
            
            # Find eigenvalue estimate (Rayleigh quotient)
            eigenvalue = sum(Av[i] * v[i] for i in range(n)) / sum(v[i] * v[i] for i in range(n))
            
            # Normalize
            norm = sum(x * x for x in Av) ** 0.5
            if norm < 1e-10:
                return None
            v_new = [x / norm for x in Av]
            
            # Check convergence
            diff = sum((v_new[i] - v[i]) ** 2 for i in range(n)) ** 0.5
            if diff < tolerance:
                return eigenvalue, v_new
            
            v = v_new
        
        return None  # Did not converge


def create_identity(n: int) -> Matrix:
    """Create an n×n identity matrix."""
    data = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    return Matrix(data)


def create_zero(rows: int, cols: int) -> Matrix:
    """Create a rows×cols zero matrix."""
    return Matrix([[0.0] * cols for _ in range(rows)])


if __name__ == "__main__":
    # Demo usage
    print("=" * 60)
    print("MATRIX SOLVER DEMO")
    print("=" * 60)
    
    # Create a sample matrix
    A = Matrix([
        [4, 2, 1],
        [1, 3, 2],
        [2, 1, 4]
    ])
    
    print("\nOriginal Matrix A:")
    print(A)
    
    print("\n--- Transpose ---")
    print(A.transpose())
    
    print(f"\n--- Determinant ---")
    print(f"det(A) = {A.determinant():.4f}")
    
    print("\n--- Inverse ---")
    A_inv = A.inverse()
    if A_inv:
        print(A_inv)
    else:
        print("Matrix is singular (no inverse)")
    
    print(f"\n--- Rank ---")
    print(f"rank(A) = {A.rank()}")
    
    print("\n--- Gaussian Elimination Steps ---")
    ref, steps = A.gaussian_elimination(verbose=True)
    for step in steps:
        print(step)
    print("\nRow Echelon Form:")
    print(ref)
    
    print("\n--- Solve Linear System ---")
    b = [7, 8, 9]
    print(f"Solving Ax = b where b = {b}")
    x = A.solve(b)
    if x:
        print(f"Solution: x = {[f'{xi:.4f}' for xi in x]}")
    else:
        print("No unique solution exists")
