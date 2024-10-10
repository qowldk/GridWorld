# 스크립트 최종 과제
import random
import time
import os


class GridWorld:
    def __init__(self):
        self.width = 4 * 3
        self.height = 4 * 3
        self.matrix = [["." for j in range(self.width)] for i in range(self.height)]
        for i in range(3):
            for j in range(3):
                self.matrix[i][j] = 'S'
        for i in range(3, 6):
            for j in range(3, 6):
                self.matrix[i][j] = 'H'
        for i in range(3, 6):
            for j in range(9, 12):
                self.matrix[i][j] = 'H'
        for i in range(6, 9):
            for j in range(9, 12):
                self.matrix[i][j] = 'H'
        for i in range(9, 12):
            for j in range(3):
                self.matrix[i][j] = 'H'
        for i in range(9, 12):
            for j in range(9, 12):
                self.matrix[i][j] = 'G'
        self.state = (0, 0)

    def display(self):

        print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
        for i in range(self.height):
            for j in range(self.width):
                if (i == 3 or i == 6 or i == 9) and j == 0:
                    print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
                if j % 3 == 0:
                    print("ㅣ ", end=" ")
                if i >= 0 and i < 3 and j >= 0 and j < 3:
                    print('\033[31m' + self.matrix[i][j] + '\033[0m', end="  ")
                else:
                    print(self.matrix[i][j], end="  ")
                if j == 11:
                    print("ㅣ", end="")
            print()
            # print("-------------------------------------")
        print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")

    def newDisplay(self):
        if self.state[0] == 9 and self.state[1] == 9:
            result = self.goalSuccess()
            if result == 1:
                return 1
        else:
            print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
            for i in range(self.height):
                for j in range(self.width):
                    if (i == 3 or i == 6 or i == 9) and j == 0:
                        print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
                    if j % 3 == 0:
                        print("ㅣ ", end=" ")
                    if i >= self.state[0] and i < self.state[0] + 3 and j >= self.state[1] and j < self.state[1] + 3:
                        print('\033[31m' + self.matrix[i][j] + '\033[0m', end="  ")
                    else:
                        print(self.matrix[i][j], end="  ")
                    if j == 11:
                        print("ㅣ", end="")
                print()
                # print("-------------------------------------")
            print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")

    def display_one(self, k, t):
        print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
        for i in range(self.height):
            for j in range(self.width):
                if (i == 3 or i == 6 or i == 9) and j == 0:
                    print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
                if j % 3 == 0:
                    print("ㅣ ", end=" ")
                if i == k and j == t:
                    print('\033[31m' + self.matrix[i][j] + '\033[0m', end="  ")
                else:
                    print(self.matrix[i][j], end="  ")
                if j == 11:
                    print("ㅣ", end="")
            print()
            # print("-------------------------------------")
        print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
        time.sleep(0.2)
        self.clearConsole()

    def final_display(self):
        print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
        for i in range(self.height):
            for j in range(self.width):
                if (i == 3 or i == 6 or i == 9) and j == 0:
                    print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
                if j % 3 == 0:
                    print("ㅣ ", end=" ")
                print(self.matrix[i][j], end="  ")
                if j == 11:
                    print("ㅣ", end="")
            print()
            # print("-------------------------------------")
        print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")

    def goalSuccess(self):
        self.display_one(9, 11)
        self.display_one(9, 10)
        self.display_one(9, 9)
        self.display_one(10, 9)
        self.display_one(11, 9)
        self.display_one(11, 10)
        self.display_one(11, 11)
        self.display_one(10, 11)
        self.display_one(10, 10)
        self.final_display()
        # 빰 빰 전체
        return 1

    def chooseAction(self):

        mx_nxt_reward = 0
        action = ""

        if np.random.uniform(0, 1) <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # greedy action
            for a in self.actions:
                # if the action is deterministic
                nxt_reward = self.state_values[self.State.nxtPosition(a)]
                if nxt_reward >= mx_nxt_reward:
                    action = a
                    mx_nxt_reward = nxt_reward
        return action

    def nxtPosition(self):

        while True:
            action = int(input("상하좌우 순서  8246  입력->"))
            if action == 8:
                nxtState = (self.state[0] - 3, self.state[1])
            elif action == 2:
                nxtState = (self.state[0] + 3, self.state[1])
            elif action == 4:
                nxtState = (self.state[0], self.state[1] - 3)
            elif action == 6:
                nxtState = (self.state[0], self.state[1] + 3)
            else:
                print("올바르지 않은 키입니다. 다시 입력하세요. ")
                continue
            # if next state legal
            if (nxtState[0] >= 0) and (nxtState[0] < self.height):
                if (nxtState[1] >= 0) and (nxtState[1] < self.width):
                    return nxtState
            return self.state

    def hole_display(self):

        print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
        for i in range(self.height):
            for j in range(self.width):
                if (i == 3 or i == 6 or i == 9) and j == 0:
                    print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")
                if j % 3 == 0:
                    print("ㅣ ", end=" ")
                if i >= self.state[0] and i < self.state[0] + 3 and j >= self.state[1] and j < self.state[1] + 3:
                    print('\033[31m' + self.matrix[i][j] + '\033[0m', end="  ")
                else:
                    print(self.matrix[i][j], end="  ")
                if j == 11:
                    print("ㅣ", end="")
            print()
            # print("-------------------------------------")
        print("ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ㅡ ")

    def checkingHole(self):
        if self.matrix[self.state[0]][self.state[1]] == 'H':
            self.clearConsole()
            self.hole_display()
            time.sleep(0.5)
            self.clearConsole()
            # time.sleep(0.5)
            self.hole_display()
            print('\033[31m' + "                        !hole!" + '\033[0m')
            return 1

    def rdm_nxtPosition(self):
        while True:
            time.sleep(1)
            action = random.randint(0, 3)  # 이거 고치기
            if action == 0:
                nxtState = (self.state[0] - 3, self.state[1])
            elif action == 1:
                nxtState = (self.state[0] + 3, self.state[1])
            elif action == 2:
                nxtState = (self.state[0], self.state[1] - 3)
            elif action == 3:
                nxtState = (self.state[0], self.state[1] + 3)
            else:
                print("올바르지 않은 키입니다. 다시 입력하세요. ")
                continue
            # if next state legal
            if (nxtState[0] >= 0) and (nxtState[0] < self.height):
                if (nxtState[1] >= 0) and (nxtState[1] < self.width):
                    return nxtState
            return self.state

    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def play(self):
        i = 0
        self.display()
        mode = int(input("직접 입력 모드 : 1 , 자동 진행 모드 : 2 ->"))
        while True:  # i < rounds
            # to the end of game back propagate reward
            if mode == 1:
                inhole = self.checkingHole()
                if inhole == 1:
                    break
                self.state = self.nxtPosition()
                self.clearConsole()
                result = self.newDisplay()
                if result == 1:
                    break
                elif result == 2:
                    break
            elif mode == 2:
                inhole = self.checkingHole()
                if inhole == 1:
                    break
                self.state = self.rdm_nxtPosition()
                self.clearConsole()
                result = self.newDisplay()
                if result == 1:
                    break
                elif result == 2:
                    break


if __name__ == "__main__":
    test = GridWorld()
    test.play()


