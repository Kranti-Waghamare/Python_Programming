import matplotlib.pyplot as plt

def main():
    language = ["C", "C++", "Java", "Python"]
    Students = [30, 40, 35, 55]

    plt.bar(
        language,                        # Values of X axis
        Students,                        # Values of Y axis
        width = 0.6,                     # width of bars
        edgecolor = "black",             # border color of bars
        linewidth = 1,                   # width of bar border
        alpha = 0.3,                     # transperence 0.0 to 1.0
        label = "Students"               # legend text
    )

    plt.title("Marvellous Bar plot")
    plt.xlabel("Languages")
    plt.ylabel("Number of students")
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()