# Student Report Card Generator

try:
    # Ask how many students
    no_of_students = int(input("Enter number of students: "))

    total_marks_per_subject = 50
    total_marks_all_subjects = total_marks_per_subject * 3

    # To store all marks for calculating averages
    physics_marks = []
    chemistry_marks = []
    maths_marks = []
    student_totals = []

    # Get data for each student using loop
    for i in range(1, no_of_students + 1):
        name = input(f"\nEnter name of student {i}: ")
        physics = int(input(f"Enter Physics marks out of 50 for student {i}: "))
        chemistry = int(input(f"Enter Chemistry marks out of 50 for student {i}: "))
        maths = int(input(f"Enter Mathematics marks out of 50 for student {i}: "))

        physics_per = (physics / total_marks_per_subject) * 100
        chemistry_per = (chemistry / total_marks_per_subject) * 100
        maths_per = (maths / total_marks_per_subject) * 100

        total = physics + chemistry + maths
        overall_per = (total / total_marks_all_subjects) * 100

        # Save marks for averages later
        physics_marks.append(physics)
        chemistry_marks.append(chemistry)
        maths_marks.append(maths)
        student_totals.append(total)

        # Print report for this student
        print(f"\nNew School Of Learning – Class XI – {name}")
        print("-" * 75)
        print(f"| {'Subject':^15} | {'Total Marks':^11} | {'Marks Obtained':^15} | {'Percentage':^10} |")
        print("-" * 75)
        print(f"| {'Physics':^15} | {total_marks_per_subject:^11} | {physics:^15} | {physics_per:^10.1f} |")
        print(f"| {'Chemistry':^15} | {total_marks_per_subject:^11} | {chemistry:^15} | {chemistry_per:^10.1f} |")
        print(f"| {'Mathematics':^15} | {total_marks_per_subject:^11} | {maths:^15} | {maths_per:^10.1f} |")
        print("-" * 75)
        print(f"| {'Total':^15} | {total_marks_all_subjects:^11} | {total:^15} | {overall_per:^10.2f} |")
        print("-" * 75)

    # After all students: calculate averages
    physics_avg = sum(physics_marks) / no_of_students
    chemistry_avg = sum(chemistry_marks) / no_of_students
    maths_avg = sum(maths_marks) / no_of_students

    physics_avg_percentage = (physics_avg / total_marks_per_subject) * 100
    chemistry_avg_percentage = (chemistry_avg / total_marks_per_subject) * 100
    maths_avg_percentage = (maths_avg / total_marks_per_subject) * 100

    overall_class_percentage = (sum(student_totals) / (no_of_students * total_marks_all_subjects)) * 100

    print("\nClass Average And Percentage for Each Subject:")
    print(f"Physics Average is {round(physics_avg, 2)} and Percentage is {round(physics_avg_percentage, 2)}%")
    print(f"Chemistry Average is {round(chemistry_avg, 2)} and Percentage is {round(chemistry_avg_percentage, 2)}%")
    print(f"Mathematics Average is {round(maths_avg, 2)} and Percentage is {round(maths_avg_percentage, 2)}%")
    print(f"Overall Percentage: {round(overall_class_percentage, 2)}%")

except:
    print("You entered some wrong format.")

finally:
    print("The School Report App compiled successfully.")
