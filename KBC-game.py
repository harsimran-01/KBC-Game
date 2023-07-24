
#list of questions :In this all the answers are at index 1
questions = [
    [
        "Which tag is used to define an internal style sheet in HTML?",
        "<style>", "<link>", "<head>", "<css>",
        
    ],
    [
        "What does CSS stand for?",
        "Cascading Style Sheets", "Creative Style Sheets", "Computer Style Sheets", "Colorful Style Sheets",
        
    ],
    [
        "Which attribute is used to define inline styles in HTML?",
        "style", "src","class", "id",
        
    ],
    [
        "Which property is used to set the background color of an element in CSS?",
        "background-color", "background", "bgcolor","color",
        
    ],
    [
        "Which CSS property is used to control the spacing between letters in a text?",
        "letter-spacing", "text-spacing","line-height", "word-spacing",
        
    ],
    [
        "Which tag is used to create an unordered list in HTML?",
        "<ul>", "<list>","<ol>", "<li>",
        
    ],
    [
        "Which CSS property is used to control the positioning of an element?",
        "position", "display", "float", "align",
        
    ],
    [
        "What does the <img> tag represent in HTML?",
        "Image", "Link", "Paragraph", "Heading",
        
    ],
    [
        "Which CSS property is used to add a shadow effect to an element's box?",
        "box-shadow", "text-shadow", "shadow-effect", "element-shadow",
        
    ]    
]

#printing First Display Screen
print("\n \n 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝙺𝙰𝚄𝙽 𝙱𝙰𝙽𝙴𝙶𝙰 𝙲𝚁𝙾𝚁𝙴𝙿𝙰𝚃𝙴\n\n")


level = 1   #Putting the level Initially at 1
score = 0   #Putting the Score Initially at 2

#Taking a for loop 
for i in range(0, len(questions)):
    question = questions[i]  

    print(f"Question {i + 1}\n\n {question[0]}\n")   #This line only prints what is at index 0, in the above list questions are at 0 index..

    print(f"Options:\n\n a) {question[1]} \t b) {question[2]}\n")    #prints the value which are at index 1, 2, 3, 4

    print(f" c) {question[3]} \t d) {question[4]}")

    ans = input("\nPlease Enter your Answer: ")     #aking for input of answer.
  
    if ans == question[1]:      #Running an if statement 
        # when the answer user enters is equal to correct answer:
        print("*****You answered 𝚌𝚘𝚛𝚛𝚎𝚌𝚝𝚕𝚢 ****\n")            
        score += 1000      #just adding 1000 to initially assigned value of score
        print(f"      Your Total Score is {score}.     \n")
        level += 1
        print(f"  You Reached to {level}nd Level. \n")

        #when the answer is incorrect
    else:  
        print(f"The correct answer was : {question[1]} .You loose")
        score = score
        print(f"You scored {score}.")
        break  #exits the loop   