# Homework
- Name: Addison Schleigh
## Question 1) Define the following unit, integration, regression tests and when you would use each?
- Unit test: Unit tests are used to see if a function does the function it needs to do, valid or not valid. In this homework, I used parametrize on a couple tests which can be used to test different scenarios and the results easily.
- Integration test: Integration tests are used to test if a function that utilizes another function works as intended. This typically happens after you create another function that uses a previous function within it, hence integration.
- Regression test: Regression tests are used after making additions and changes to a program, for which regression tests are previous tests to see if new additions don't bring back previous errors, otherwise known as the code regressing.
## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.
Pytest works by looking setting up a pytest.ini, where in it you say where the root of the directory is and pytest works within the scope of that directory. From there it searches for python files that have test within them. Going into those files, it runs any files that have test within them, and if no errors are found, says if they pass those tests or not. A pytest fixture essentially acts as a parameter for a test, which is used to set up and tear down a program that is to be tested such that it is easier to manage and visually see as well as reusable for different tests
