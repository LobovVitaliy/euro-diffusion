from tasks import TaskList, Task
from algorithm import Algorithm


def print_result(i, result):
    print('\nCase Number {}'.format(i))

    for r in result:
        print(r[0], r[1])


def main():
    # fill tasks

    with open('file', 'r') as file:
        country_count = int(file.readline())

        tasks = TaskList()

        while country_count:
            if not 1 <= country_count <= 20:
                print('Error: The number of countries (1 ≤ c ≤ 20)')
                return

            task = Task()

            for i in range(country_count):
                task.add(file.readline())

            tasks.add(task)

            country_count = int(file.readline())

    # make tasks

    case_number = 1

    for task in tasks.list:
        try:
            algorithm = Algorithm()

            for line in task.lines:
                algorithm.add_country(line)

            print_result(case_number, algorithm.run())

            case_number += 1
        except Exception as e:
            print('\nCase Number {}'.format(case_number))
            print('Error: {}'.format(e))


if __name__ == '__main__':
    main()
