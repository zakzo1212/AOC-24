def get_sum(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)
    diffs = [abs(l1[i] - l2[i]) for i in range(len(l1))]
    return sum(diffs)

def get_sim_score(l1, l2):
    l2_counts = {}
    for num in l2:
        if num in l2_counts:
            l2_counts[num] += 1
        else:
            l2_counts[num] = 1
    
    sim_score = 0
    for num in l1:
        sim_score += l2_counts.get(num, 0)
    return sim_score

if __name__ == "__main__":

    ### PART 1 SOLUTION
    # l1 = []
    # l2 = []
    # with open("input.txt", "r") as f:
    #     for line in f:
    #         nums = list(map(int, line.split()))
    #         if len(nums) == 2:
    #             l1.append(nums[0])
    #             l2.append(nums[1])
    # print(get_sum(l1, l2))

    ### PART 2 SOLUTION
    l1 = []
    l2 = []
    with open("input.txt", "r") as f:
        for line in f:
            nums = list(map(int, line.split()))
            if len(nums) == 2:
                l1.append(nums[0])
                l2.append(nums[1])
    print(get_sim_score(l1, l2))