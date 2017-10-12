if __name__ == '__main__':


    #perm_list = perm.generate(arguments.get("<string>"))

    lines = []
    state = True
    while state is True:
        line = raw_input()
        if not line:
            state = False
        else:
            print(line)
            lines.append(line)

