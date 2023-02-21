# Data model templates
This file contains JSON templates to create data that can be uploaded to the studyspace aws dynamodb tables.

#### Global remarks
- In JSON, backslash (`\`) is treated as a special character. When writing Latex code, you need to escape the backslash character with another backslash to make a 'real' backslash. Example: The latex code `\begin{aligned} f(x) &= x^2 \\ f'(x) &= 2x \end{aligned}` becomes `\\begin{aligned} f(x) &= x^2 \\\\ f'(x) &= 2x \\end{aligned}`
- The templates show a PutRequest for 1 item. You can put multiple PutRequest in 1 JSON to upload multiple items at the same time. You do this by adding
multiple PutRequest to the list, separated by a comma (the square brackets [] after <table-name> describe a list). Refer to the example file.
- In the 'question', 'hint' and 'solution' fields you can mix normal text and math (latex) expressions. You start and end the latex expression with '$'.
- The 'equation' field only holds a mathematical expression, therefore you do not have to start the expression with a '$'.
- Answer texts hold either text or math expressions. If it is a math expression, start and end with '$'.
- The first answer or first n answers, depending on the question type, are always the correct one. The app then shuffles the answers.
- Images are always provided as svg strings.
- Most fields are mandatory, meaning you have to provide some value. Some are optional, refer to the remarks of each data model to check which attribtutes are optional.


## Single Choice Question
Available tables (to be inserted at `<table-name>`):
- Dev environment:         "SingleChoiceQuestion-6p4kwyei3jep5baa4pwuhpvg5a-dev"
- Production environment:  "SingleChoiceQuestion-fjai5uohmnhclkm226sts6htze-production"

```
{
    <table-name>: [
        {
            "PutRequest": {
                "Item": {
                    "exerciseSets": {
                        "L": [
                            {
                                "S": "0/0/1/exercises/1"
                            }
                        ]
                    },
                    "question": {
                        "S": "Gebe die Ableitung von t an."
                    },
                    "equation": {
                        "S": "t(x) = -x^3 + 2x^2 - e^x"
                    },
                    "image": {
                        "S": ""
                    },
                    "answer0": {
                        "S": "$t'(x) = -3x^2 + 4x - e^x$"
                    },
                    "answer1": {
                        "S": "$t'(x) = -3x^2 + 4x - x e^{x-1}$"
                    },
                    "answer2": {
                        "S": "$t'(x) = -x^2 + 2x - e^x$"
                    },
                    "answer3": {
                        "S": "$t'(x) = -x^2 + 2x - e^x$"
                    },
                    "hint": {
                        "S": "Beachte die Summenregel und die Ableitungsregel der e-Funktion."
                    },
                    "solution": {
                        "S": "Korrekt!"
                    },
                    "__typename": {
                        "S": "SingleChoiceQuestion"
                    }
                }
            }
        }
    ]
}
```
The fields 'equation', 'image', 'answer2' and 'answer3' are optional. You must provide at least 2 answers.


## Single Image Choice Question
Available tables (to be inserted at `<table-name>`):
- Dev environment:         "SingleImageChoiceQuestion-6p4kwyei3jep5baa4pwuhpvg5a-dev"
- Production environment:  "SingleImageChoiceQuestion-fjai5uohmnhclkm226sts6htze-production"

```
{
    <table-name>: [
        {
            "PutRequest": {
                "Item": {
                    "exerciseSets": {
                        "L": [
                            {
                                "S": "0/0/1/exercises/1"
                            }
                        ]
                    },
                    "question": {
                        "S": "Welche Abbildung zeigt den Graphen von t?"
                    },
                    "equation": {
                        "S": "t(x) = -x^3 + 2x^2 - e^x"
                    },
                    "image0": {
                        "S": <svg>
                    },
                    "image1": {
                        "S": <svg>
                    },
                    "image2": {
                        "S": <svg>
                    },
                    "image3": {
                        "S": <svg>
                    },
                    "hint": {
                        "S": "Hinweis ...."
                    },
                    "solution": {
                        "S": "Lösung ..."
                    },
                    "__typename": {
                        "S": "SingleImageChoiceQuestion"
                    }
                }
            }
        }
    ]
}
```
The fields 'equation', 'image2' and 'image3' are optional. You must provide at least 2 images.


## Multiple Question
Available tables (to be inserted at `<table-name>`):
- Dev environment:         "MultipleChoiceQuestion-6p4kwyei3jep5baa4pwuhpvg5a-dev"
- Production environment:  "MultipleChoiceQuestion-fjai5uohmnhclkm226sts6htze-production"

```
{
    <table-name>: [
        {
            "PutRequest": {
                "Item": {
                    "exerciseSets": {
                        "L": [
                            {
                                "S": "0/0/1/exercises/1"
                            }
                        ]
                    },
                    "question": {
                        "S": "Which are capital cities?"
                    },
                    "equation": {
                        "S": ""
                    },
                    "image": {
                        "S": ""
                    },
                    "answers": {
                        "L": [
                            {
                                "S": "Berlin"
                            },
                            {
                                "S": "Managua"
                            },
                            {
                                "S": "San Salvador"
                            },
                            {
                                "S": "New York City"
                            },
                            {
                                "S": "Sao Paulo"
                            }
                        ]
                    },
                    "numCorrectAnswers": {
                        "N": "3"
                    },
                    "hint": {
                        "S": "The biggest city is not always the capital."
                    },
                    "solution": {
                        "S": "Nice job!"
                    },
                    "__typename": {
                        "S": "MultipleChoiceQuestion"
                    }
                }
            }
        }
    ]
}
```
The fields 'equation' and 'image' are optional. You can provide as many answers as you want, but you must provide at least 1 answer and
1 =< numCorrectAnswers =< answers.length must hold.


## True False Question
Available tables (to be inserted at `<table-name>`):
- Dev environment:         "TrueFalseQuestion-6p4kwyei3jep5baa4pwuhpvg5a-dev"
- Production environment:  "TrueFalseQuestion-fjai5uohmnhclkm226sts6htze-production"

```
{
    <table-name>: [
        {
            "PutRequest": {
                "Item": {
                    "exerciseSets": {
                        "L": [
                            {
                                "S": "0/0/1/exercises/1"
                            }
                        ]
                    },
                    "question": {
                        "S": "Gebe die Ableitung von t an."
                    },
                    "equation": {
                        "S": "t(x) = -x^3 + 2x^2 - e^x"
                    },
                    "image": {
                        "S": ""
                    },
                    "isTrue": {
                        "BOOL": true
                    },
                    "hint": {
                        "S": "Beachte die Summenregel und die Ableitungsregel der e-Funktion."
                    },
                    "solution": {
                        "S": "Korrekt!"
                    },
                    "__typename": {
                        "S": "TrueFalseQuestion"
                    }
                }
            }
        }
    ]
}
```
The fields 'equation' and 'image' are optional.


## Drag and drop question
Available tables (to be inserted at `<table-name>`):
- Dev environment:         "DragAndDropQuestion-6p4kwyei3jep5baa4pwuhpvg5a-dev"
- Production environment:  "DragAndDropQuestion-fjai5uohmnhclkm226sts6htze-production"

```
{
    <table-name>: [
        {
            "PutRequest": {
                "Item": {
                    "exerciseSets": {
                        "L": [
                            {
                                "S": "0/0/1/exercises/1"
                            }
                        ]
                    },
                    "question": {
                        "S": "Match capital cities with their country."
                    },
                    "typeListOne": {
                        "N": "0"
                    },
                    "typeListTwo": {
                        "N": "0"
                    },
                    "listOne": {
                        "L": [
                            {
                                "S": "Tegucigalpa"
                            },
                            {
                                "S": "Managua"
                            },
                            {
                                "S": "San Salvador"
                            },
                            {
                                "S": "San Jose"
                            }
                        ]
                    },
                    "listTwo": {
                        "L": [
                            {
                                "S": "Honduras"
                            },
                            {
                                "S": "Nicaragua"
                            },
                            {
                                "S": "El Salvador"
                            },
                            {
                                "S": "Costa Rica"
                            }
                        ]
                    },
                    "hint": {
                        "S": "All countries are located in Central America."
                    },
                    "__typename": {
                        "S": "DragAndDropQuestion"
                    }
                }
            }
        }
    ]
}
```
- You can specify following types in 'typeListOne' and 'typeListTwo': 0 = text, 1 = math expressions, 2 = image (svg string).
- It must hold: listOne.length == listTwo.length . Element k in listOne corresponds to element k in listTwo.
- listOne and listTwo must contain at least 1 element.
