
# Building lists on the fly
As we've previously seen, for-loops and lists are often used together to either build a new list, access multiple elements of a list, or finding elements in a list that satisfy certain criteria. An example of this could be the following exercise from the chapter "Iteration over values":

```python
result = []
fruit = 'banana'
for character in fruit:
    if character == 'a':
        result.append(character)
```

Going through this line by line:
1) First create a variable that contains an empty list
2) Define the string we want to iterate over
3) Create a for loop that iterates over 'fruit'
4) Create a conditional that triggers when the letter 'a' is found in the string
5) Append the letter 'a' to the 'result' list

While it is relatively easy to follow the logic through these five lines of code, it can quickly take up a lot of space in our code if we have to do these types of actions multiple times through our program. Python, however, has a solution for this!

## List comprehensions {-}

List comprehensions offer a clever way of combining lists with for-loops, in a way that takes up much less space than what we saw in the banana-example.
Try to write an run the following line of code, and compare the output to that of the example above:

```python
fruit = 'banana'
result = [character for character in fruit if character == 'a']
print(result)
```

This should give you the same output as the more traditional for-loop, but we managed to do steps 1, 3, 4, and 5 from the previous example in a single line!
What we're doing here is asking Python to do the following:

1) Loop over each character in the string 'fruit' (`for character in fruit`)
2) Check if the character is 'a' (`if character == 'a'`)
3) If it is, add it to the list (`[character ...]`)

So, the list comprehension takes care of both the loop and the condition in a concise way. The output is exactly the same as before, but it only takes one line instead of five.

### General structure {-}
The syntax / structure of a list comprehension might look unfamiliar at first, but it's actually relatively straightforward once you break it down

```python
new_list = [expression for variable in iterable]
```

- **expression**: the value or transformation you want in the new list. It can be as simple as appending the variable (like `character`), or you can apply string-methods in case of iterating over a string (`character.upper()`)
- **variable**: represents each item in the original sequence (e.g., each character in a string)
- **iterable**: the collection you're iterating over, such as a list, string, range, tuple, ...
- **condition** (optional): filters the items; only items for which this condition is `True` are included in the new list

Let's go over a few examples to reinforce the concept. Write out the following examples, think about what you expect the results to be, then run the code.

```python
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)
```

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
```

## Advantages of list comprehensions
Utilizing your new skills in making list comprehensions can make your code more concise by turning several lines of code into one, and additionally, once you get familiar with the syntax, they often make the intention of your code much clearer!

## Things to watch out for
While you may want to flex you knowledge by turning every for-loop of your code into a list comprehension, it's important to show a bit of constraint. Complex for-loops quickly become incredibly difficult to break down if they're turned into list comprehensions, so keep a couple of things in mind:
- **Keep it simple**: Avoid complex expressions or multiple conditions in a single comprehension
- **Use for readability**: If you or others find the comprehension hard to understand at first glance, consider breaking it down into a regular for-loop instead

[//]: # (Comment)
[//]: # (Not sure if the following should be included, might be too complex)

An example of a list comprehension that probably should be expanded to a regular for-loop:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_even_squares = [x**2 for row in matrix for x in row if x % 2 == 0 and x > 4]
```

Instead this could be refactored to:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_even_squares = []
for row in matrix:
    for x in row:
        if x % 2 == 0 and x > 4:
            flattened_even_squares.append(x**2)
```

#### Exercise
Given a list of numbers, create a new list that contains the square of each **even** number from the original list, using a list comprehension

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [# List comprehension here!]
print('Expected output: [4, 16, 36, 64, 100]')
print(f'Your result: {even_squares}')
```

#### Exercise
Given a string, use a list comprehension to create a list of all the vowels in the string

```python
text = 'List comprehensions are awesome!'
vowels = [# List comprehension here]
print('Expected output: ["i", "o", "e", "e", "i", "o", "a", "e", "a", "e", "o", "e"]')
print(f'Your result: {vowels}')
```

#### Exercise
Given a list of numbers, create a new list where each number is squared if it’s even, and cubed if it’s odd

**Hint**: The condition has to be applied to the *expression* in this exercise; it is not used as a filter as in the example shown earlier. Therefore, the syntax is as follows:

```python
new_list = [expression if condition for variable in iterable]
```

```python
numbers = [1, 2, 3, 4, 5]
transformed = [# List comprehension here!]
print('Expected output: [1, 4, 27, 16, 125]')
print(f'Your result: {transformed}')
```

## Example from translation project {-}


