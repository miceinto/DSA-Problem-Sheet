# Contributing to DSA Problem Sheet

Thank you for your interest in contributing to the DSA Problem Sheet! We appreciate all contributions, whether it's adding new problems, solving existing ones, or improving documentation.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Adding a New Problem](#adding-a-new-problem)
- [Solving an Existing Problem](#solving-an-existing-problem)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors

## How to Contribute

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/DSA-Problem-Sheet.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit your changes: `git commit -m 'Add: Brief description'`
7. Push to your branch: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Adding a New Problem

### Step 1: Choose a Topic
Select an appropriate category from the existing folders in `Problems/`. If a new category is needed, create it following the naming convention.

### Step 2: Create Problem Folder
Create a new folder for your problem under the appropriate topic:
```
Problems/
└── Arrays/
    └── Two-Sum/
```

### Step 3: Add Problem Description
Create a `README.md` file in the problem folder with:
- Problem title
- Difficulty level (Easy/Medium/Hard)
- Problem description
- Constraints
- Examples with input/output
- Hints (optional)

Example:
```markdown
# Two Sum

**Difficulty:** Easy

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Examples

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
```

### Step 4: Add Solution Files
Add solution files in your preferred programming language(s):
- `solution.py` for Python
- `solution.java` for Java
- `solution.cpp` for C++
- `solution.js` for JavaScript
- etc.

Include:
- Clear, well-commented code
- Time and space complexity analysis
- Explanation of the approach

## Solving an Existing Problem

1. Check if a solution already exists in your preferred language
2. If not, add a new solution file
3. Follow the same guidelines as for new problems
4. Include complexity analysis and explanation

## Pull Request Process

1. Ensure your PR description clearly describes the changes
2. Reference any related issues
3. Make sure all tests pass (if applicable)
4. Update documentation if needed
5. Wait for review and address any feedback

## Style Guidelines

### Code Style
- Use meaningful variable names
- Add comments explaining complex logic
- Follow language-specific best practices
- Include docstrings or comments for functions

### File Naming
- Use kebab-case for folder names: `two-sum`
- Use lowercase with underscores for file names: `solution.py`
- Use descriptive names that match the problem

### Commit Messages
Follow conventional commit format:
- `Add: New problem - Two Sum`
- `Solve: Two Sum in Java`
- `Fix: Correct solution for Binary Search`
- `Docs: Update contribution guidelines`

## Need Help?

If you have questions or need help, feel free to:
- Open an issue for discussion
- Ask in the comments of relevant problems
- Check existing issues for similar questions

Thank you for contributing to DSA Problem Sheet! 🎉
