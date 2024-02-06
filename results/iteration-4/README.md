### Topline Findings
Accuracy: 53.3%

Confusion Matrix
|       | Predicted Positive | Predicted Negative |
| ----- | ------------------ | ------------------ |
| True  | 33                 | 7                  |
| False | 35                 | 15                 |

### Difference from Last Iteration
Change from completion model to chat model (gpt-turbo-3.5-16k), split up system prompt and user prompt, further reduce restriction in reasoning template. The porpotion of false negative has been greatly increased.


### Example Prompt
#### System Prompt
Imagine yourself as an education worker, you are developing a series of after-class exercises for high school students. You have determined several practices you want to achieve by designing these questions. Your task is to determine whether the following questions reflect that specific practice or not.

The name of the practice you need to pay attention to is `Algorithm Practices`. The practice is defined as a question that prompts students to engage in one or more of the subpractices. Modifying or designing an algorithm might involve pseudo-code only but can also include implementing it in a computational language (e.g. text or block-based code).

Return the answer for all 10 questions in an easily dumped JSON format like this:

```JSON
{
    "Question_number listed in prompt(eg. "1")":
        {
            "Question": "Original text of question 1",
            "Reasons": "Analysis of steps required for students to solve the question.",
            "Answer": "Yes/No"
        }
    <continue...>
}
```

Use ` `` ` if you want to quote some phrases.

#### User Prompt

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

### Example Output
```JSON
    "1": {
        "Question": "What is the parameter of interest? What symbol is used to represent this value?",
        "Reasons": "This question prompts students to identify the parameter of interest and its representation symbol.",
        "Answer": "Yes",
        "Correct Answer": "No"
    },
    "2": {
        "Question": "What is the statistic obtained from the sample? What symbol is used to represent this value?",
        "Reasons": "This question prompts students to identify the statistic obtained from a sample and its representation symbol.",
        "Answer": "Yes",
        "Correct Answer": "No"
```


### Model Step
The model used in this test is **gpt-turbo-3.5-16k**

### Next Step

1. Revise reasoning part
2. Provide examples
3. Google Palm
