# README 
This README file summarizes the results of a model developed to determine whether a given question reflects a specific practice or not. 

## Result Summary 
Accuracy: 0.6222222222222222

Confusion Matrix:

|       | Predicted Positive | Predicted Negative |
| ----- | ------------------ | ------------------ |
| True  | 43                 | 7                  |
| False | 27                 | 13                 |

## Prompt Construction
Imagine yourself as an education worker, you are developing a series of after-class exercise for high school students. You have determined a several practices you want to achieve by designing those questions. The name of the practice you need to pay attention to is `Algorithm Practices`, the practice is defined as a question that prompts students to engage in one or more of the subpractices. Modifying or designing an algorithm might involve pseudo-code only but can also include implementing it in a computational language (e.g. text or block based code). 

Below is an example input and output (no need to follow):
```
Determine whether the following 10 questions reflect the given practice or not
(Do not try to answer the questions):

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

## Model Usage
The model used in this test is **text-davinci-003**

## Next Step

1. GPT-4?
2. Revise Question Coding
3. Provide examples
4. Google Palm