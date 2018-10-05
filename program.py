from stack import Stack


def main():
    s1 = Stack()
    s2 = Stack()

    s1.push(1)
    # s1.push(None)
    s1.push(2)
    s1.push(3)
    s1.push('kon')
    print('size of stack1 =', s1.size())
    s2.push('jeden')
    s2.push('dwa')
    s3 = s1 + s2

    # try:
    #     s3 += 'adam'
    # except ValueError as e:
    #     print('Error: ', e)

    print('size of stack1 =', s1.size())
    print('size of stack2 =', s2.size())
    print('size of stack3 =', s3.size())

    [print(obj) for obj in s3.to_list()]

    [print(obj) for obj in s3]

    s4 = Stack()
    for obj in s4:
        print(obj)

    # print('size of stack =', s1.size())
    # print(s1.pop())
    # print(s1.pop())
    # print('size of stack =', s1.size())
    # print(s1.pop())
    # print('is stack empty? ', s1.empty())
    # print(s1.pop())
    # print('is stack empty? ', s1.empty())


if __name__ == '__main__':
    main()
