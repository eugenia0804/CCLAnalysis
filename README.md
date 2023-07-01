# CCLAnalysis
Analysis on CT-STEM practice questions using LLM

## Code Structure
```plaintext
.
├── Dataset
│   ├── BioUnitDataCoding                # Codebook Original Data File 
│   └── Questionset-TaxonomyMath         # Questions Needed to be processed
├── Results
│   └── iteration-1
│       ├── final.json                    # Combined final result
│       ├── prompts.txt                   # Prompts for each call
│       ├── raw_results.txt               # Direct LLM output for each call
│       └── results.json                  # Structured results for each call
├── llm.py                                
├── main.py                               # Main file for each iteration
├── prompts.py                            
├── analysis.py                           # Code for analyzing results
├── support.py                            
├── LICENSE                               # License information for the project
└── README.md                             # README file with project information
```