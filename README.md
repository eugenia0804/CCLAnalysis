# CCLAnalysis
Analysis on CT-STEM practice questions using LLM \
Intern Project at Northwestern's Center for Connected Learning and Computer-Based Modeling (CCL) (March 2023 - June 2023) \ 
Using GPT-3.5 to categorize questions based on the skills being tested

## Code Structure
```plaintext
.
├── code
│   ├── codebook_info.py                 # Util function to read subpractices and explanation in the guidebook
│   ├── quesion_info.py                  # Util function to read questions from the guidebook
│   └── util.py                          # Low level utility functions
├── dataset
│   ├── BioUnitDataCoding                # Codebook Original Data File 
│   └── Questionset-TaxonomyMath         # Practice Questions
├── images                               # Confusion Matrix from each iteration
├── results
│   └── iteration-1
│       ├── final.json                    # Combined final result
│       ├── prompts.txt                   # Prompts for each call
│       ├── raw_results.txt               # Direct LLM output for each call
│       └── results.json                  # Structured results for each call
│   └── iteration-2 ...
├── llm.py                                # LLM model informations
├── main.py                               # Main file for each iteration
├── prompts.py                            # Prompts open to modified 
├── analysis.py                           # Result analyzer - Confusion Matrix Generator
├── support.py                            # Combine results from individual calls
├── LICENSE                              
└── README.md                            
```
## How to rerun a specific iteration 
Make sure to change index (Selected Practice) & iteration (Selected set of prompts)
```
bash rerun.sh
```

