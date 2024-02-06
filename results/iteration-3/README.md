### Topline Findings
Accuracy: 62.2%

Confusion Matrix
|       | Predicted Positive | Predicted Negative |
| ----- | ------------------ | ------------------ |
| True  | 13                 | 27                 |
| False | 7                  | 43                 |

### Difference from Last Iteration
Change the 'template' part in prompt into a relatively non-restrictive instruction, intended to fully utilize the power of reasoning before making decision.


### Example Prompt
Imagine yourself as an education worker, you are developing a series of after-class exercises for high school students. You have determined several practices you want to achieve by designing these questions. Your task is to determine whether the following questions reflect that specific practice or not.

The name of the practice you need to pay attention to is `Algorithm Practices`. The practice is defined as a question that prompts students to engage in one or more of the subpractices. Modifying or designing an algorithm might involve pseudo-code only but can also include implementing it in a computational language (e.g. text or block-based code).

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
            "Reasons": "Analysis of steps required for students to solve the question and why it does/does not reflect the given practice.",
            "Answer": "Yes/No"
        }
    <continue...>
}
```

Use ` `` ` if you want to quote some phrases.

### Example Output
```JSON
"15": {
        "Question": "Suppose an administrator is claiming that the true Mean score of the population is 3.2. Do you have convincing evidence to refute their claim? Explain.",
        "Reasons": "This question does not reflect the given practice of Algorithm Practices as it does not involve modifying or designing an algorithm. The question requires students to understand the concept of sampling distribution and use the statistical model to explain why their claim is wrong.",
        "Answer": "No",
        "Correct Answer": "Yes"
    },
    "16": {
        "Question": "First, we'll create the same sampling distribution that we created yesterday. Use the model above to create the sampling distribution for the mean scores of samples of 2 students (n=2) taken from a population of 48 students (N=48).\n\n1) Set the slider and click `setup` and `collect samples.` The sampling will happen faster if you pull the `model speed` slider all the way to the right.\n\n2) Click the...",
        "Reasons": "This question reflects the given practice of Algorithm Practices as it involves modifying or designing an algorithm. The question requires students to understand the concept of sampling distribution and use the model to create the sampling distribution for the mean scores of samples of 2 students.",
        "Answer": "Yes",
        "Correct Answer": "Yes"
```


### Model Step
The model used in this test is **text-davinci-003**

### Next Step

1. GPT-4?
2. Revise Question Coding
3. Provide examples
4. Google Palm
