# 30. Smart Software Engineer Recruitment System
python_skill_score =int(input("Input Your Score: "))
python_problem_solving_score =int(input("Input Your Problem Solving Score: "))
communication_skill =input("Communication Skill(good/bad): ").lower()
experience =int(input("Your Coding Experience: "))
status = "Selected for Final HR Round" if python_skill_score >= 80 and python_problem_solving_score >= 75 and  communication_skill == "good" and experience >= 2 else "Not Selected"
print(status)
