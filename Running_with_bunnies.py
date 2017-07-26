from Queue import *

class state:
    times = []
    available_bunnies = set()
    def __init__(self, time_limit, bunnies = []):
        self.bunnies = set(bunnies)
        self.time = time_limit

    def comp(self, s):
        if s.bunnies == self.bunnies and self.time == s.time :
            return 0
        elif s.bunnies.issubset(self.bunnies) and self.time >= s.time :
            return 1
        elif self.bunnies.issubset(s.bunnies) and s.time >= self.time :
            return 0
        else :
            return 2

    def travel_rescue(self, cur_pos, next_pos):
        new_state = state(self.time - self.times[cur_pos][next_pos], self.bunnies)
        if next_pos in self.available_bunnies:
            new_state.bunnies.add(next_pos)
        return new_state

    def __str__(self):
        return str(self.bunnies) + " " + str(self.time)

def judge_state(cur_state, state_list):
    for i in range(len(state_list)):
        score = cur_state.comp(state_list[i])
        if score == 1:
            state_list[i] = cur_state
            return True
        elif score == 0:
            return False
    state_list.append(cur_state)
    return True

def answer(times, time_limit):
    loc_num = len(times)
    bunny_num = loc_num - 2
    state.times = times
    state.available_bunnies = set(range(1, loc_num - 1))
    All_state = [[state(float("-inf"))] for x in range(loc_num)]
    q = Queue(maxsize=0)
    q.put((0, state(time_limit)))
    while not q.empty():
        pos, cur_state = q.get()
        for i in range(pos) + range(pos+1, loc_num):
            next_state = cur_state.travel_rescue(pos, i)
            if len(next_state.bunnies) == bunny_num and next_state.time >= 0 and i == loc_num:
                return range(1, loc_num - 1)
            out = judge_state(next_state, All_state[i])
            if not out:
                continue
            else:
                # print((i, str(next_state)))
                q.put((i, next_state))

    rescued = set()
    print [(s.bunnies, s.time) for s in All_state[4]]
    for cur_state in All_state[loc_num - 1]:
        if len(cur_state.bunnies) > len(rescued) and cur_state.time >= 0:
            rescued = cur_state.bunnies

    ret = []

    for x in rescued:
        ret.append(x - 1)

    return ret

print(answer([[0, 2, 2,2,2 ,2, -1], [9, 0, 2, 2,2,2, -1], [9, 3, 0, 2,2,2, -1], [9, 3, 2,2,2, 0, -1], [9, 3, 2, 2, 2, 2, 0],[9, 3, 2, 2, 2, 2, 0], [9, 3, 2, 2, 2, 2, 0] ] , 1))
