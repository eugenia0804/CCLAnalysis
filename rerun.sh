export index=2
export iteration=4
#python example.py --uncomment the code if you only want to run the first ten questions

if [ ! -d "iteration-$iteration" ]; then
    mkdir -p "iteration-$iteration"
    echo "Created directory: iteration-$iteration"
fi

if [ ! -d "iteration-$iteration/final" ]; then
    mkdir "iteration-$iteration/final"
    echo "Created directory: iteration-$iteration/final"
fi

if [ ! -d "iteration-$iteration/raw_results" ]; then
    mkdir "iteration-$iteration/raw_results"
    echo "Created directory: iteration-$iteration/raw_results"
fi

if [ ! -d "iteration-$iteration/results" ]; then
    mkdir "iteration-$iteration/results"
    echo "Created directory: iteration-$iteration/results"
fi

if [ ! -d "iteration-$iteration/prompts" ]; then
    mkdir "iteration-$iteration/prompts"
    echo "Created directory: iteration-$iteration/prompts"
fi

if [ ! -f "iteration-$iteration/prompts.py" ]; then
    cp prompts.py "iteration-$iteration"/
fi

if [ ! -f "iteration-$iteration/prompts-iteration-$iteration.py" ]; then
    mv "iteration-$iteration"/prompts.py "iteration-$iteration"/prompts-iteration-$iteration.py
fi

echo "File pathes are setted"
echo "Start running codes"

python main.py
echo "main.py completed: OPENAI responses are ready"
if [! -f "iteration-$iteration/results/1to10.json"]:
    python support.py
    echo "support.py completed: combined result is ready"
if [! -f "iteration-$iteration/final/1to90.json"]:
    python analysis.py
    echo "analysis.py completed: result analysis is ready"
