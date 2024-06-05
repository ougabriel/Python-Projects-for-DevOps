## Automate  Pull Request on a GitHub Project using Python

**Objective**
This project is aimed at automating the following
- Get the names of users who did a Pull Request
- Get the number of Pull Requests made by each user

**Algorithm used**

1. Use Request Module
2. API URL to access Github 
3. Convert information recieved from JSON to Dictionary
4. Print the Pull Request information

**Briefs**
This project uses the popular Kubernetes repo as sample to test this script.


**Output Result**
!output for pullrequest.py](image.png)



**Personal Notes**

- We import the requests library to make HTTP requests.
- We send a GET request to the specified URL using requests.get('https://api.github.com/repos/kubernetes/kubernetes/pulls') and store the response in the response variable.
- We parse the JSON data from the response using response.json() and store it in the user_details variable.
- We check if the request was successful by checking if the status_code is 200 (OK).
- If the request was successful, we loop through each element of the user_details list using a for loop and the range function.
- Inside the loop, we print the 'login' and 'id' values from the 'user' dictionary for each element in the list.
- If the request failed, we print an error message with the status code.
- The output of this code will be a list of tuples, where each tuple contains the 'login' and 'id' values for each pull request in the list.

Note:  have the requests library installed before running this code. If not, you can install it using pip install requests.

@ougabriel
@OkomUGabriel
@GabrielOkom