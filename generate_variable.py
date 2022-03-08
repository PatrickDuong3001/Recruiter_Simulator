for x in range(1,101):    #help generate a massive stack of necessary lists
    with open("generate_list.txt","a") as f:
        f.write(f"elif index == {x}:\n\tself.person_{x}.append(rand_rate)\n")