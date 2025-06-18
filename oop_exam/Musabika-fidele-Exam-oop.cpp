#include <iostream>
using namespace std;

class MatrixOpBase {
public:
    virtual int** run(int** A, int** B, int r1, int c1, int r2, int c2) = 0;
    virtual ~MatrixOpBase() {}
};



class AddMatrixOp : public MatrixOpBase {
public:
    int** run(int** A, int** B, int r1, int c1, int r2, int c2) override {
        if (r1 != r2 || c1 != c2) {
            cout << "Addition requires matrices of same dimensions.\n";
            return nullptr;
        }
        int** result = new int*[r1];
        for (int i = 0; i < r1; ++i) {
            result[i] = new int[c1];
            for (int j = 0; j < c1; ++j)
                *(*(result + i) + j) = *(*(A + i) + j) + *(*(B + i) + j); 
        }
        return result;
    }
};

class MulMatrixOp : public MatrixOpBase {
public:
    int** run(int** A, int** B, int r1, int c1, int r2, int c2) override {
        if (c1 != r2) {
            cout << "Multiplication requires columns of A to match rows of B.\n";
            return nullptr;
        }
        int** result = new int*[r1];
        for (int i = 0; i < r1; ++i) {
            result[i] = new int[c2];
            for (int j = 0; j < c2; ++j) {
                *(*(result + i) + j) = 0;
                for (int k = 0; k < c1; ++k)
                    *(*(result + i) + j) += *(*(A + i) + k) * *(*(B + k) + j); 
            }
        }
        return result;
    }
};
class TransposeMatrixOp : public MatrixOpBase {
public:
    int** run(int** A, int**, int r1, int c1, int, int) override {
        int** result = new int*[c1];
        for (int i = 0; i < c1; ++i) {
            result[i] = new int[r1];
            for (int j = 0; j < r1; ++j)
                *(*(result + i) + j) = *(*(A + j) + i); 
        }
        return result;
    }
};

int** allocateMatrix(int rows, int cols) {
    int** matrix = new int*[rows];
    for (int i = 0; i < rows; ++i)
        matrix[i] = new int[cols];
    return matrix;
}

void inputMatrix(int** matrix, int rows, int cols, char name) {
    cout << "Enter elements for matrix " << name << " (" << rows << "x" << cols << "):\n";
    for (int i = 0; i < rows; ++i)
        for (int j = 0; j < cols; ++j)
            cin >> *(*(matrix + i) + j);
}

void printMatrix(int** matrix, int rows, int cols, const string& name) {
    cout << name << ":\n";
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j)
            cout << *(*(matrix + i) + j) << " ";
        cout << "\n";
    }
}

int main() {
    int r1, c1, r2, c2;
    cout << "Enter rows and columns for Matrix A: ";
    cin >> r1 >> c1;
    cout << "Enter rows and columns for Matrix B: ";
    cin >> r2 >> c2;

    int** A = allocateMatrix(r1, c1);
    int** B = allocateMatrix(r2, c2);
    inputMatrix(A, r1, c1, 'A');
    inputMatrix(B, r2, c2, 'B');
    

    MatrixOpBase** ops = new MatrixOpBase*[3];
    ops[0] = new AddMatrixOp();
    ops[1] = new MulMatrixOp();
    ops[2] = new TransposeMatrixOp();

    int** sum = ops[0]->run(A, B, r1, c1, r2, c2);
    if (sum) printMatrix(sum, r1, c1, "Sum");

    int** mul = ops[1]->run(A, B, r1, c1, r2, c2);
    if (mul) printMatrix(mul, r1, c2, "Product");

    int** trans = ops[2]->run(A, nullptr, r1, c1, 0, 0);
    printMatrix(trans, c1, r1, "Transpose of A");

    for (int i = 0; i < r1; ++i) delete[] A[i];
    for (int i = 0; i < r2; ++i) delete[] B[i];
    delete[] A; delete[] B;

    for (int i = 0; i < 3; ++i) delete ops[i];
    delete[] ops;

    return 0;
}
