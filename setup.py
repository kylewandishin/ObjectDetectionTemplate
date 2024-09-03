import inquirer

def setup():
    questions = [
        inquirer.Checkbox('models',
                        message="Which model would you like to train?",
                        choices=['defect', 'plate'],
                    ),
    ]
    answers = inquirer.prompt(questions)
    models = answers['models']
    print(f"Training {models} models.")
    return models