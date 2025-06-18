# Matrix Operation Library - C++

## 👤 Author
Fidele Musabika

## 📘 Description
This project implements basic matrix operations — addition, multiplication, and transpose — using C++ object-oriented programming principles such as inheritance and polymorphism. All matrices are dynamically allocated and manipulated using pointer arithmetic.

## ✅ Features
- Dynamic matrix allocation (`int**`)
- Abstract base class `MatrixOpBase`
- Derived classes:
  - `AddMatrixOp`
  - `MulMatrixOp`
  - `TransposeMatrixOp`
- Operation dispatcher via `MatrixOpBase** ops`
- Pointer arithmetic used for all matrix manipulations
- Screenshots of sample inputs and outputs included

## 🛠 How It Works
1. **User Input:** Matrix sizes and elements.
2. **Operation Dispatch:** Calls `run()` from corresponding class.
3. **Result Display:** Printed output on console.
4. **Memory Cleanup:** All dynamic allocations are properly deleted.

## 📌 Screenshot
![Matrix Output Screenshot](screenshot.png)

## 💻 How to Run
```bash
g++ main.cpp -o matrix_ops
./matrix_ops
