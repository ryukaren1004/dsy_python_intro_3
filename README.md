# Iteration

### Updating variables
Common pattern

    >>> x = 0
    >>> x = x + 1    ## Increment

### while statement
The flow of while statement

1. Evaluate the condition, yielding True or False
2. If the condiiton is false, exit the while statement and continue execution at the next statement
3. If the condiiton is true, execute the body and then go back to step 1 (loop back)

### Infinite loops

    n = 10
    while True:
        print(n, end='')
        n = n - 1
    print('Done!')

    while True:
        line = input('> ')
        if line == 'done':
            break
        print(line)
    print('Done!')

This way of writing while loops is common because you can check the condition anywhere in the loop (not just at the top) and you can express the stop condition affirmatively ("stop when this happens") rather than negatively ("keep going until that happens.").

### Finishing iterations with continue

    while True:
        line = input('> ')
        if line[0] == '#':
            continue
        if line == 'done':
            break
        print(line)
    print('Done!')

### Define loops using for

The <b>for</b> loop is looping through a known set of items so it runs through as many iterations as there are items in the set

### Loop patterns

#### Continuing and summing loops
len()
sum()

#### Maximum and minimum loops

    def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest


## [Exercises](./exercises_loop.md)

## [Glossary](./glossary_loop.md)

# [Week 5 Assignments](assignment.md)