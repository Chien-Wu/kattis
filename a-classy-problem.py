"https://open.kattis.com/problems/classy"

def turn_input_into_count():
    round = int(input(""))
    people = []
    for i in range(round):
        list = input("").split(" ")
        name = list[0][:-1]
        classys = list[1].split("-")
        classys.reverse()

        count = 0
        for i in range(len(classys)):
            if classys[i] == "upper":
                count += 1 * (10 ** (-i))
            elif classys[i] == "middle":
                count += 0 * (10 ** (-i))
            elif classys[i] == "lower":
                count += -1 * (10 ** (-i))
        people.append([name, count])
        sorted_people = sorted(people, key=lambda x: (-x[1], x[0]))
        print(sorted_people)
    return sorted_people

def main():
    case = int(input(""))
    for i in range(case):
        sorted_people = turn_input_into_count()
        for person in sorted_people:
            print(person[0])
        print("=" * 30)

main()
