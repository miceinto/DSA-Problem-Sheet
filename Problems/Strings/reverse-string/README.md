# Reverse String

**Difficulty:** Easy

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with O(1) extra memory.

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ascii character.

## Examples

**Example 1:**

Input: s = ["h","e","l","l","o"]

Output: ["o","l","l","e","h"]

**Example 2:**

Input: s = ["H","a","n","n","a","h"]

Output: ["h","a","n","n","a","H"]

## Hints

- Use two pointers, one at the start and one at the end.

- Swap the characters and move the pointers towards each other.
