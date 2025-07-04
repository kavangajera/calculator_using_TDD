# 🧮 String Calculator – TDD Kata in Python - Using CI/CD pipeline

This is a **Test-Driven Development (TDD)** implementation of the classic [String Calculator Kata](https://osherove.com/tdd-kata-1) using **Python 3**, `unittest`, and **GitHub Actions for CI/CD**.  
It includes 21+ unit tests and a **fully working pipeline to ensure clean, tested code is pushed into the main branch**.

---

## 🚀 Features Implemented

✅ Add method supports:
- Empty string → returns `0`  
- One or more numbers separated by `,` or `\n`  
- Custom delimiters: `//[delimiter]\n[numbers...]`  
- Delimiters of **any length** (`[***]`)  
- **Multiple delimiters** (`[;][%%]`)  
- **Negative number handling** — raises `ValueError`  
- Ignores numbers **> 1000**  
- Tracks how many times `add()` was called  
- Event system: triggers `subscribe()` callback after `add()` is called  

---

## 🧪 Tests

Includes **21+ unit tests** using Python's built-in `unittest` framework:
- Tests basic addition, custom delimiters, edge cases
- Verifies exception for negative numbers
- Checks delimiter parsing logic
- Tests event system and call count tracking

### ✅ Run all tests locally:
```bash
python -m unittest tests.test_for_string_calculator -v
