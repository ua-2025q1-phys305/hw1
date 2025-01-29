# PHYS305 Homework Set #1

Welcome to the repository for **Homework Set #1** in PHYS305.
This homework set is worth **10 points** and is designed to test your
understanding of topics that we covered in the first five classes.
The submission cutoff time is at **Thursday Feb 6th, 11:59pm** Arizona
time.


## Structure and Grading

This homework set consists of **five assignments**, each contributing
equally to your overall grade.
The grading breakdown is as follows:

1. **Automated Evaluation (50%)**:
   * Each assignment will be graded using `pytest`, an automated
     testing framework.
   * The correctness of your solutions accounts for 1 point per
     assignment (5 points in total).
   * You can run `pytest` in GitHub Codespaces or your local
     development environment to verify your solutions before
     submission.

2. **Documentation and Coding Practices (50%)**:
   * The remaining 1 point per assignment (5 points total) will be
     based on documentation and coding practices.
   * Clear and concise **documentation** of your code, including
     meaningful comments.
   * Adherence to good **coding practices**, such as proper variable
     naming, modular design, and code readability.

By following the interface and prototypes provided in each assignment
template, you can ensure compatibility with the autograding system and
maximize your score.


## Assignments

### **Assignment 1**: Setup Python Package (2 points)

* **Objective**:
  Learn how to set up and organize a pip-installable python package.
* **Details**:
  * Following the guest lecture, add multiple metadata files including
    "pyproject.toml" and "LICENSE" to this package and turn it into a
    pip-installable python package.
  * Properly organize source code, tests, and documentations.

### **Assignment 2**: Integer Negation and Subtraction Using NAND Gates (2 points)

* **Objective**:
  Implement a function that performs integer negation using only NAND
  gates and use it to implement subtraction.
* **Details**:
  * You are tasked with simulating the behavior of NAND gates to
    achieve these operations at the logical level.
  * The description of the assignment and the solution template can be
    found in `phys305_hw1/a2.py`.

### **Assignment 3**: Rewriting the Coupled Harmonic Oscillator (2 points)

* **Objective**:
  Take the coupled harmonic oscillator problem we solved in the lab
  and rewrite it using a well-structured Python class.
* **Details**:
  * Your implementation should encapsulate the behavior and parameters
    of the system in an object*oriented design.
  * Ensure your class includes methods to compute the system's
    dynamics.
  * The description of the assignment and the solution template can be
    found in `phys305_hw1/a3.py`.

### **Assignment 4**: Solving the Heat Equation and Visualizing Results (2 points)

* **Objective**:
  Solve the 1D heat equation semi-analytically and create a
  visualization of the solution.
* **Details**:
  * You should put the solver in a class, which can be based on the
    assignment 2.
  * Given an arbitrary initial temperature profile, your solver should
    return a semi-analytical solution of the temperature at arbitrary
    time.
  * The description of the assignment and the solution template are
    available in `phys305_hw1/a4.py`.

### **Assignment 5**: Providing Project Ideas (2 points)

* **Objective**: Provide draft project ideas to form teams.
* **Details**:
  * This assignment ensures student start putting time to brainstorm their
    mid-term projects.
  * Your submission should include three project ideas based on the
    topics that are covered in the first half of this course:
    * Data Representation and Errors
    * Numerical Linear Algebra
    * Fourier Transform and Spectral Analysis
    * Interpolation and Extrapolation
    * Numerical and Automatic Derivatives
    * Numerical Integration of Functions
    * Root Finding
    * Optimization
    * Data Modeling and Machine Learning
  * You submission will be a well formatted YAML file
    `phys305_hw1/a5.yaml`.


## Submission Guidelines

1. Create a new repostiory based on this template by using the GitHub
   Classroom Link https://classroom.github.com/a/xpW8Mw2V and work on
   the assignments in GitHub Codespaces or locally.

2. Use `pytest` to test your solutions before submission.
   Ensure that all test cases pass to maximize your automated
   evaluation score.

3. **Submit your completed assignments by pushing your changes to the
   repository before the deadline.**

**Note**:
**The submission deadline is a strict cutoff.
No submission will be accepted after the deadline.**g
Be sure to manage your time effectively and plan ahead to ensure your
work is submitted on time.
Frequent and incremental `git commit` and `git push` are recommended
to ensure your latest work are seen.


## Additional Notes

* **Collaboration**:
  You are encouraged to discuss ideas with your peers, but your
  submission must reflect your own work.
* **Help and Resources**:
  If you encounter any difficulties, please refer to the course
  materials, consult your instructor, or seek help during office
  hours.
* **Deadlines**:
  Be mindful of the submission deadline, as late submissions will not
  be accepted.

Good luck, and enjoy working on the assignments!
