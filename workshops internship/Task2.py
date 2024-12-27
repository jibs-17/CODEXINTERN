import numpy as np

# Function to input a matrix
def input_matrix(name):  #a parameter for the function is name
    print(f"\nEnter details for {name}:")
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    print(f"Enter the elements for {name}, row by row (separate values with spaces):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Row does not match the number of columns!")
            return None
        matrix.append(row)
    return np.array(matrix)

# Menu options
def menu():
    print("\nMatrix Operations Menu:")
    print("1. If you want to Add Matrices")
    print("2. If you want to Subtract Matrices")
    print("3. If you want to Multiply Matrices")
    print("4. If you want to Transpose Matrix")
    print("5. If you want to  Determinant of Matrix")
    print("6. If you want to Exit")

# Main function
def main():
    print("Welcome to the Matrix Operations Tool!")
    while True:
        menu()
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':  # Addition
            print("\nMatrix Addition")
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A is not None and B is not None:
                if A.shape == B.shape:
                    print("Result of Addition:")
                    print(A + B)
                else:
                    print("Error: Matrices must be of the same dimensions!")
        
        elif choice == '2':  # Subtraction
            print("\nMatrix Subtraction")
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A is not None and B is not None:
                if A.shape == B.shape:
                    print("Result of Subtraction:")
                    print(A - B)
                else:
                    print("Error: Matrices must be of the same dimensions!")
        
        elif choice == '3':  # Multiplication
            print("\nMatrix Multiplication")
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A is not None and B is not None:
                if A.shape[1] == B.shape[0]:
                    print("Result of Multiplication:")
                    print(np.dot(A, B))
                else:
                    print("Error: Columns of A must match rows of B!")
        
        elif choice == '4':  # Transpose
            print("\nMatrix Transpose")
            A = input_matrix("Matrix")
            if A is not None:
                print("Transpose of the Matrix:")
                print(A.T)
        
        elif choice == '5':  # Determinant
            print("\nMatrix Determinant")
            A = input_matrix("Square matrix")
            if A is not None:
                if A.shape[0] == A.shape[1]:
                    print(f"Determinant of the Matrix: {np.linalg.det(A):.2f}")
                else:
                    print("Error: Determinant can only be calculated for square matrices!")
        
        elif choice == '6':  # Exit
            print("Goodbye!")
            break
        
        else:
            print("Invalid option! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
