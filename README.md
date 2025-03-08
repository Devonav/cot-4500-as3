# Numerical Methods for Solving Differential Equations

## Description
This project implements numerical methods to solve differential equations, specifically:
- **Euler's Method**
- **Runge-Kutta Method (4th Order)**

The differential equation solved is:
\[ \frac{dy}{dt} = t - y^2 \]
with initial condition \( f(0) = 1 \) over the range \( 0 < t < 2 \) using 10 iterations.

## Repository Structure
```
cot-4500-as3/
├── src/
│   ├── main/
│   │   ├── __init__.py
│   │   ├── assignment_3.py
│   ├── test/
│   │   ├── __init__.py
│   │   ├── test_assignment_3.py
├── requirements.txt
├── README.md
```

## Installation & Requirements
This project only requires Python and NumPy. Install dependencies with:
```sh
pip install -r requirements.txt
```

## Running the Program
To execute the main script:
```sh
python src/main/assignment_3.py
```
Expected output:
```
1.2446380979332121
1.251316587879806
```

## Running Unit Tests
To verify the implementation, run:
```sh
python -m unittest discover -s src/test
```
OR
```sh
python src/test/test_assignment_3.py
```

## Notes
- No external libraries beyond **NumPy** are used.
- The project follows a structured format for clarity and maintainability.
- Ensure Python 3.x is installed before running the scripts.

## Author
Devon Villalona

