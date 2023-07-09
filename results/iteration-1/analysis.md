### Topline Findings
Accuracy: 64.5%

Confusion Matrix
|       | Predicted Positive | Predicted Negative |
| ----- | ------------------ | ------------------ |
| True  | 43                 | 7                  |
| False | 25                 | 15                 |

### Difference from Last Iteration
Shorten the prompt to make it more efficient & clear. Specific changes include remove the subpractices list & reduce the number of samples in the template.


### Example Prompt
Imagine yourself as an education worker, you are developing a series of after-class exercises for high school students. You have determined several practices you want to achieve by designing these questions. Your task is to determine whether the following questions reflect that specific practice or not.

The name of the practice you need to pay attention to is `Algorithm Practices`, which is consisted of subpractices includes 
`Using an algorithm to solve a problem`,
`Selecting an appropriate algorithm to solve a problem`,
`Assessing the efficiency, correctness, and clarity of an algorithm`,
`Modifying an algorithm to better address a problem`,
`Designing and constructing algorithms`.
The practice is defined as a question that prompts students to engage in one or more of the subpractices. Modifying or designing an algorithm might involve pseudo-code only but can also include implementing it in a computational language (e.g. text or block-based code).

Determine whether the following 10 questions reflect the given practice or not (Do not try to answer the questions):

```C
1: What is the parameter of interest? What symbol is used to represent this value?
2: What is the statistic obtained from the sample? What symbol is used to represent this value?
3: How many samples of size 2 can be taken from this population?
4: What is the parameter of interest for this situation?
5: What statistic are we using to estimate the parameter of interest for this situation?
6: Do you think taking a sample this size from this population effectively estimates the mean score of the population?
7: Calculate the sample mean for all possible samples of size 2 from this population.
8: Create a dotplot of your results from question #2. Create your sketch below.
9: In most real-life situations, we cannot create the dotplot of all possible samples of size n from the entire population (size N). Why not?
10: Click `setup` and then `collect sample`. What did the model do?
```

Return the answer for all 10 questions in an easily dumped JSON format like this:

```JSON
 {
            "Question_number listed in prompt(eg. "1")":
                {
                    "Question": "Original text of question 1",
                    "Reasons": "The question is intended for students to perform the work of ..., which does/does not reflect the `practice name`.",
                    "Answer": "Yes/No"
                }
            
             "Question_number listed in prompt(eg. "12")":
                {
                    "Question": "Original text of question 1",
                    "Reasons": "The question is intended for students to perform the work of ..., which does/does not reflect the `practice name`.",
                    "Answer": "Yes/No"
                }
            <continue...>
        }
```

Use ` `` ` if you want to quote some phrases.

### Example Output
```JSON
    "34": {
        "Question": "Set the population proportion slider to match your answer in the previous question. When you click `setup` button and then the \u201ctake sample\u201d button the model will take an SRS of 5 traffic stops and report the proportion of drivers who identify as black. Take a few samples. Do you get proportions close to the actual value? Explain why you do or do not.",
        "Reasons": "The question reflects the `Algorithm Practices` as it involves the subpractices of `Using an algorithm to solve a problem`, `Selecting an appropriate algorithm to solve a problem`, `Assessing the efficiency, correctness, and clarity of an algorithm`.",
        "Answer": "Yes",
        "Correct Answer": "Yes"
    },
    "35": {
        "Question": "On the next page you're going to do some work with sampling distributions. Define the term `sampling distribution` in one sentence.",
        "Reasons": "The question does not reflect the `Algorithm Practices` as it does not involve any of the subpractices.",
        "Answer": "No",
        "Correct Answer": "No"
```


### Model Step
The model used in this test is **text-davinci-003**

### Next Step

1. Try simplified prompt 
2. Consider GPT-4?
3. Revise Question Coding
4. Provide examples
5. Explore Google PaLM2
