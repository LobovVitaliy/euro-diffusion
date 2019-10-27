from algorithm import Algorithm


def print_result(i, result):
    print('\nCase Number {}'.format(i))

    for r in result:
        print(r[0], r[1])


def fill_tasks(filename):
    with open(filename, 'r') as file:
        country_count = int(file.readline())

        tasks = []

        while country_count:
            if not 1 <= country_count <= 20:
                print('Error: The number of countries (1 ≤ c ≤ 20)')
                return None

            lines = []

            for i in range(country_count):
                lines.append(file.readline())

            tasks.append(lines)

            country_count = int(file.readline())

        return tasks


def make_tasks(tasks):
    case_number = 1

    for lines in tasks:
        try:
            algorithm = Algorithm()

            for line in lines:
                algorithm.add_country(line)

            print_result(case_number, algorithm.run())

            case_number += 1
        except Exception as e:
            print('\nCase Number {}'.format(case_number))
            print('Error: {}'.format(e))


def main():
    tasks = fill_tasks('file')

    if tasks:
        make_tasks(tasks)


if __name__ == '__main__':
    main()
