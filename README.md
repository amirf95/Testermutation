# Mutation Testing Project

This project implements a basic mutation testing framework for Python, focusing on a simple function (`is_even`) and a minimal test suite to evaluate its robustness. The framework introduces small, deliberate errors (mutants) in the code and checks if the tests can catch them.

## Project Structure

- **example.py**: Contains the target function `is_even`.
- **test_example.py**: Defines the unit tests for `is_even`.
- **mutations.py**: Lists possible code mutations.
- **mutant_tester.py**: The main script that runs the mutation testing process.
- **backup.py**: A backup of the original implementation, used to restore the original code after testing.

## How It Works

1. The original implementation is backed up.
2. Each defined mutation is applied to the original code to create a mutant.
3. The test suite is executed against each mutant:
   - If the tests fail, the mutant is considered "killed" (good).
   - If the tests still pass, the mutant has "survived" (indicating potential test suite weakness).
4. The mutation testing engine reports a mutation score.

## Usage

To run the mutation testing framework:

```bash
python mutant_tester.py
The script will:

Backup the original code.

Apply each mutation and run the tests.

Output which mutants were killed or survived.

Calculate and display the final mutation score.

Restore the original implementation.

Example
The project tests the is_even function:

python
Copier
Modifier
def is_even(n):
    return n % 2 == 0
The corresponding tests:

python
Copier
Modifier
from example import is_even

def test_even():
    assert is_even(2)
    assert not is_even(3)
Mutation Definitions
Common mutations include:

== → !=

!= → ==

> → <

< → >

+ → -

- → +

True → False

False → True

These mutations simulate typical errors in the code.

Results
In the current implementation, only one mutation (== → !=) is applicable to the is_even function, and the test suite successfully detects it, resulting in a 100% mutation score.

Limitations and Potential Improvements
The framework currently applies only simple string-based mutations.

Only one mutation is applied at a time.

No integration with code coverage tools.

Limited to basic operator and boolean mutations.

Future Enhancements:

✅ Use AST-based mutations for more precise code alterations.
✅ Combine with coverage tools to identify untested code.
✅ Add parameter-based and boundary condition mutations.
✅ Provide a GUI or web interface for easier analysis.
✅ Suggest additional test cases for surviving mutants.

Conclusion
This project demonstrates the core concept of mutation testing. It can serve as a foundation for developing more advanced testing frameworks and improving the quality of your test suites.

Authors:

Tahir Ozasik (SW developer)

Ekrem Sumeraka (Powerpoint)

Emre Yalcin (Report manager)

Ugurcan Tekdemir (Group manager)

Emir Fenina (SW developer)
