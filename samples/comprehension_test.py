import time

MILLION = 10000
THOUSAND = 1000

def main():
    my_list = [num for num in range(MILLION)]

    start_time = time.time_ns()
    # this is the slow version
    for num in my_list:
        created_list = []
        for item in range(THOUSAND):
            created_list.append(item)
    end_time = time.time_ns()
    print(f'the slow version took {end_time - start_time} ns')

    start_time = time.time_ns()
    # this is the faster version
    for num in my_list:
        created_list = [item for item in range(THOUSAND)]
    end_time = time.time_ns()
    print(f'the fast version took {end_time - start_time} ns')

if __name__ == '__main__':
    main()
