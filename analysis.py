import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score

def output_analysis(iteration):
    with open(f'results/iteration-{iteration}/final/1to90.json') as file:
        json_object = json.load(file)

    answers = []
    correct_answers = []
    count = 0
    for question_id, question_data in json_object.items():
        answers.append(question_data["Answer"])
        correct_answers.append(question_data["Correct Answer"])
        count += 1

    accuracy = accuracy_score(correct_answers, answers)
    print("Accuracy:", accuracy)

    confusion_mat = confusion_matrix(correct_answers, answers)
    print("Confusion Matrix:")
    print(confusion_mat)

    labels = np.unique(correct_answers)

    sns.heatmap(confusion_mat, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()
    
    return 

output_analysis(4)
