# Result Summary
The accuracy score of the model is 0.6444444444444445
The confusion matrix is as follows:
[[43  7]
 [25 15]]

## Prompt Construction
Imagine yourself as a education worker, developing a series of after-class exercises for high school students. You have determined a practice you want to achieve by designing these questions - **Algorithm Practices**.
The practice is defined as "A question that prompts students to engage in one or more of the following subpractices:
* Using an algorithm to solve a problem
* Selecting an appropriate algorithm to solve a problem
* Assessing the efficiency, correctness, and clarity of an algorithm
* Modifying an algorithm to better address a problem
* Designing and constructing algorithms

An example input and output is included below: 

Determine whether the following 10 questions reflect the given practice or not (do not try to answer the questions): 
* 41: Test your hypothesis by changing the sample size. How does the sampling distribution change? 
* 42: Which values for n and p will make the sampling distribution look the most normal? Perform some experiments using the model and report your findings here.
* 43: The Evanstonian is concerned about the effect of vaping and e-cigarettes at ETHS. The Evanstonian staff poll a simple random sample of 150 ETHS students and ask, “Yes or No? Do you think that vaping (and/or e-cigarettes) are a problem at ETHS?” Is the 10% condition satisfied? Why or why not? If so, calculate the standard deviation of the sampling distribution of p^.
* 44: Suppose that 30% of all ETHS students respond “Yes” to this question. Let p^ be the sample proportion of ETHS students who respond “Yes” to this question. What is the mean of the sampling distribution of p^?
* 45: What is the shape of the sampling distribution of p^? Explain your reasoning and show work.
* 46: What is the probability that, in a random sample of 150 ETHS students, less than 25% will respond `Yes`. 
* 47: In a congressional district, 55% of registered voters are Democrats. Suppose we take a random sample of 100 voters from this congressional district. What is the probability of getting less than 50% Democrats in a random sample of size 100?
* 48: The Chicago Tribune asked a random sample of 750 Chicago residents. `Do you wear a face covering in public?` Based on a previous study by the IDPH, we know that 50% of ALL Chicago residents actually wear a face covering in public. Let p^ be the sample proportion who say that they wear a face covering in public. What is the probability that, in a random sample of 750, more than 75% will respond `Yes`?
* 49: If the claim is true what could that suggest about racial bias in EPD?
* 50: The idea that Police aren't always fair in carrying out their duties can bring up a lot of feelings and experiences. Do you have any personal thoughts or experiences about this topic that you'd like to share?

The model will return the answer in a easily dumped JSON format: 

```
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

## Model Usage
The model used is `text-davinci-003`. 

## Next Steps
1. Try simplified prompt 
2. Consider GPT-4?
3. Revise Question Coding
4. Provide examples
5. Explore Google PaLM2