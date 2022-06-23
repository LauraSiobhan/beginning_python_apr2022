""" this script takes in a list of data, and transforms it a little bit, then
prints the result """

def main():
    ''' do the thing '''
    # read in data
    filename = 'data.csv'
    with open(filename) as fstream:
        data = fstream.readlines()

    # loop over our list, and process. in this case, capitalize
    for num, name in enumerate(data):
        data[num] = name.title()

    # now, print our processed list
    for name in data:
        print(name)

if __name__ == '__main__':
    main()
