"""
Interactive Matrix Solver - A command-line interface for matrix operations.
"""

from matrix_solver import Matrix, create_identity, create_zero


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 60)
    print("MATRIX SOLVER - MAIN MENU")
    print("=" * 60)
    print("1. Create a new matrix")
    print("2. Display current matrix")
    print("3. Transpose")
    print("4. Calculate determinant")
    print("5. Calculate inverse")
    print("6. Calculate rank")
    print("7. Gaussian elimination (with steps)")
    print("8. Solve linear system Ax = b")
    print("9. Find dominant eigenvalue (power iteration)")
    print("10. Create identity matrix")
    print("0. Exit")
    print("=" * 60)


def get_matrix_from_user() -> Matrix:
    """Get matrix dimensions and values from user input."""
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            
            if rows <= 0 or cols <= 0:
                print("Dimensions must be positive integers.")
                continue
            
            print(f"\nEnter {rows}×{cols} matrix values row by row:")
            print("(Separate values with spaces)")
            
            data = []
            for i in range(rows):
                while True:
                    row_input = input(f"Row {i + 1}: ").strip()
                    values = [float(x) for x in row_input.split()]
                    
                    if len(values) != cols:
                        print(f"Error: Expected {cols} values, got {len(values)}")
                        continue
                    
                    data.append(values)
                    break
            
            return Matrix(data)
        
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue


def get_vector_from_user(size: int) -> list:
    """Get a vector from user input."""
    while True:
        try:
            print(f"Enter {size} values for vector b (separated by spaces):")
            values = [float(x) for x in input().strip().split()]
            
            if len(values) != size:
                print(f"Error: Expected {size} values, got {len(values)}")
                continue
            
            return values
        
        except ValueError as e:
            print(f"Invalid input: {e}")


def main():
    """Main interactive loop."""
    matrix = None
    
    print("\n🔢 Welcome to the Interactive Matrix Solver!")
    print("Perform matrix operations with step-by-step visualization.")
    
    while True:
        print_menu()
        
        if matrix:
            print(f"\nCurrent matrix: {matrix}")
        
        choice = input("\nEnter your choice (0-10): ").strip()
        
        if choice == "0":
            print("\nGoodbye! 👋\n")
            break
        
        elif choice == "1":
            matrix = get_matrix_from_user()
            print("\n✓ Matrix created successfully!")
        
        elif choice == "2":
            if not matrix:
                print("\n⚠ No matrix loaded. Please create one first.")
            else:
                print("\nCurrent Matrix:")
                print(matrix)
        
        elif choice == "3":
            if not matrix:
                print("\n⚠ No matrix loaded. Please create one first.")
            else:
                result = matrix.transpose()
                print("\nTranspose:")
                print(result)
        
        elif choice == "4":
            if not matrix:
                print("\n⚠ No matrix loaded. Please create one first.")
            elif matrix.rows != matrix.cols:
                print("\n⚠ Determinant requires a square matrix.")
            else:
                det = matrix.determinant()
                print(f"\nDeterminant: {det:.6f}")
        
        elif choice == "5":
            if not matrix:
                print("\n⚠ No matrix loaded. Please create one first.")
            elif matrix.rows != matrix.cols:
                print("\n⚠ Inverse requires a square matrix.")
            else:
                result = matrix.inverse()
                if result:
                    print("\nInverse Matrix:")
                    print(result)
                else:
                    print("\n⚠ Matrix is singular (no inverse exists).")
        
        elif choice == "6":
            if not matrix:
                print("\n⚠ No matrix loaded. Please create one first.")
            else:
                rank = matrix.rank()
                print(f"\nRank: {rank}")
        
        elif choice == "7":
            if not matrix:
                print("\n⚠ No matrix loaded. Please create one first.")
            else:
                result, steps = matrix.gaussian_elimination(verbose=True)
                print("\n--- Gaussian Elimination Steps ---")
                for step in steps:
                    print(step)
                print("\nRow Echelon Form:")
                print(result)
        
        elif choice == "8":
            if not matrix:
                print("\n⚠ No matrix loaded. Please create one first.")
            elif matrix.rows != matrix.cols:
                print("\n⚠ System requires a square coefficient matrix.")
            else:
                b = get_vector_from_user(matrix.rows)
                solution = matrix.solve(b)
                
                if solution:
                    print("\n✓ Solution found:")
                    for i, val in enumerate(solution):
                        print(f"  x[{i + 1}] = {val:.6f}")
                else:
                    print("\n⚠ No unique solution exists (system may be inconsistent or have infinite solutions).")
        
        elif choice == "9":
            if not matrix:
                print("\n⚠ No matrix loaded. Please create one first.")
            elif matrix.rows != matrix.cols:
                print("\n⚠ Eigenvalues require a square matrix.")
            else:
                result = matrix.eigenvalues_power_iteration()
                if result:
                    eigenvalue, eigenvector = result
                    print(f"\nDominant Eigenvalue: {eigenvalue:.6f}")
                    print("Corresponding Eigenvector:")
                    for i, val in enumerate(eigenvector):
                        print(f"  v[{i + 1}] = {val:.6f}")
                else:
                    print("\n⚠ Power iteration did not converge.")
        
        elif choice == "10":
            n = int(input("Enter size of identity matrix: "))
            matrix = create_identity(n)
            print(f"\n✓ {n}×{n} identity matrix created!")
            print(matrix)
        
        else:
            print("\n⚠ Invalid choice. Please enter a number between 0 and 10.")


if __name__ == "__main__":
    main()
