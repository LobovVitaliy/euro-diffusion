from algorithm import Algorithm


def print_result(i, result):
    print('\nCase Number {}'.format(i))

    for r in result:
        print(r[0], r[1])


def main():
    file = open('file', 'r')

    case_number = 1
    country_count = int(file.readline())

    while country_count:
        algorithm = Algorithm()

        for i in range(country_count):
            algorithm.add_country(file.readline())

        print_result(case_number, algorithm.run())

        case_number += 1
        country_count = int(file.readline())


if __name__ == '__main__':
    main()

