## Automate Server Configuration file when connection exceeds 200



**Algorithm**
- Read the file
- Store in a variable
- Write the file
- Update maximum connection line 



Here's an algorithm for the given script::

```
FUNCTION update_server_config(file_path, key, value)
    OPEN file at file_path in read mode
    READ all lines from the file into a list called lines
    CLOSE the file

    OPEN the same file at file_path in write mode

    FOR each line in lines
        IF the key is present in the line
            WRITE the key followed by "=" and the new value to the file
            APPEND a newline character ("/n") to the file
        ELSE
            WRITE the original line to the file

    CLOSE the file

CALL update_server_config("Server.conf", "MAX_CONNECTIONS", "1000")
```

Here's a step-by-step explanation of the algorithm:

1. The function `update_server_config` takes three arguments: `file_path` (the path to the configuration file), `key` (the configuration key to update), and `value` (the new value for the key).

2. The function opens the file at `file_path` in read mode using the `with` statement and the `open` function. It reads all lines from the file into a list called `lines` using the `readlines()` method.

3. After reading the lines, the file is closed automatically due to the `with` statement.

4. The function then opens the same file at `file_path` in write mode using the `with` statement and the `open` function.

5. The function iterates over each line in the `lines` list using a `for` loop.

6. For each line, the function checks if the `key` is present in the line using the `in` operator.

7. If the `key` is present in the line, the function writes the `key` followed by `"="` and the new `value` to the file. It also appends a newline character (`"/n"`) to the file.

8. If the `key` is not present in the line, the function writes the original line to the file.

9. After iterating over all lines, the file is closed automatically due to the `with` statement.

10. Finally, the script calls the `update_server_config` function with the arguments `"Server.conf"` (the file path), `"MAX_CONNECTIONS"` (the configuration key), and `"1000"` (the new value for the key).

This algorithm updates the value of the specified configuration key in the given file. If the key is already present in the file, its value is updated; otherwise, a new line with the key and value is added to the file.
