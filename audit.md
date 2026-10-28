Code Audit — Python & Technology Quiz

1. Project Information

* Project Name: Python & Technology Quiz
* Main File: main.py
* Programming Language: Python
* Application Type: Command-Line Quiz
* Dependencies: Python standard library only

2. Project Overview

The application presents three multiple-choice questions related to Python programming and technology.

Each question contains four options and a predefined correct answer. The user enters an answer, and the program determines whether it is correct.

At the end of the quiz, the program displays the total score and the percentage achieved.

3. Code Structure

QUESTIONS

The QUESTIONS variable is a list containing dictionaries.

Each dictionary stores:

* question: The question text.
* options: A list of four answer options.
* answer: The letter representing the correct answer.

Observation: This structure makes questions easy to read and modify.

run_quiz()

This function contains the main quiz logic.

Its responsibilities include:

* Initializing the score.
* Displaying the quiz title and instructions.
* Iterating through the questions using enumerate().
* Displaying each question and its options.
* Accepting the user’s answer.
* Checking whether the answer is correct.
* Displaying feedback.
* Calculating and displaying the final score and percentage.

Main Guard

The following statement ensures that the quiz runs when the file is executed directly:

if __name__ == "__main__":

The application then calls run_quiz().

This is a standard Python practice that also allows the module to be imported without automatically starting the quiz.

4. Positive Findings

The code demonstrates several good practices:

* Uses a clear and readable structure.
* Separates quiz data from the quiz logic.
* Uses descriptive variable names.
* Uses a function to organize the main application.
* Converts answers to uppercase and removes surrounding whitespace.
* Provides immediate feedback after each answer.
* Calculates the final score and percentage.
* Uses enumerate() to number questions.
* Uses an f-string for formatted output.
* Includes a main guard.
* Requires no external packages.

5. Issues Identified

Issue 1: Invalid Answers Are Marked Incorrect

Severity: Low

The program accepts any input. If a user enters an invalid character or word, it is treated as an incorrect answer.

For example, entering X produces the same result as choosing an incorrect option.

Recommendation: Validate that the answer is one of A, B, C, or D. If it is invalid, ask the user to enter a valid option.

Issue 2: No Retry for Incorrect Answers

Severity: Low

Once an answer is submitted, the program moves to the next question, even if the user entered an invalid response.

Recommendation: Add an input-validation loop so the user can correct invalid input before proceeding.

Issue 3: Limited Number of Questions

Severity: Low

The current quiz contains only three questions.

Recommendation: Expand the question bank to include additional Python, programming, and AI-related topics.

Issue 4: No Randomization

Severity: Low

Questions always appear in the same order.

Recommendation: Consider using Python’s random module to shuffle the questions.

Issue 5: No Persistent Score History

Severity: Low

The score is displayed at the end but is not saved after the program exits.

Recommendation: Add an optional feature to save quiz results to a file.

Issue 6: Potential Division by Zero if the Question List Is Empty

Severity: Low

The percentage calculation divides the score by the total number of questions.

If QUESTIONS becomes empty, the calculation will cause a ZeroDivisionError.

Recommendation: Check whether the question list contains at least one question before running the quiz or calculating the percentage.

6. Security Review

* The application does not connect to external services.
* The application does not request passwords or credentials.
* The code uses Python’s built-in functionality.
* No external packages are required.
* User input is compared against predefined answer strings.

Assessment: No obvious security concerns are apparent for this small, local quiz application.

7. Performance Review

The application is lightweight and suitable for a small quiz.

Its execution time increases approximately linearly with the number of questions because each question is processed once.

For a quiz containing only three questions, performance is not a concern.

8. Testing Recommendations

The following cases should be tested:

Test Case	Expected Result
Enter the correct answer	Display “Correct!” and increase the score.
Enter an incorrect answer	Display the correct answer without increasing the score.
Enter a lowercase answer	Accept it as equivalent to the uppercase answer.
Enter an answer with surrounding spaces	Remove the spaces before checking the answer.
Answer all questions correctly	Display 3/3 and 100%.
Answer all questions incorrectly	Display 0/3 and 0%.
Enter an invalid option	Currently treated as incorrect; input validation is recommended.
Remove all questions	Currently risks division by zero; add a guard.

9. Recommended Improvements

Priority improvements include:

1. Validate answers before checking correctness.
2. Prevent division by zero if no questions are available.
3. Expand the question bank.
4. Add randomized question order.
5. Save results for future reference.
6. Add automated tests for scoring and input handling.

10. Conclusion

The Python & Technology Quiz is a beginner-friendly project demonstrating lists, dictionaries, functions, loops, conditional statements, user input, string manipulation, and arithmetic operations.

The implementation is simple and readable, and it fulfils its primary purpose of conducting a basic multiple-choice quiz.

The main areas for improvement are input validation, handling an empty question list, expanding the question bank, and adding optional score tracking.

Audit Status: Static code review completed. Recommended improvements have been documented but have not necessarily been implemented or tested.
