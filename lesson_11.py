# Rebrain_Python lesson 11
import os


# 1,2,3)
class PC_memory:
    def __init__(self, pc_id, user_name, mem_t, mem_u, mem_p=0):
        self.pc_id = pc_id
        self.user_name = user_name
        self.mem_t = int(mem_t)
        self.mem_u = int(mem_u)
        self.mem_p = int(self.mem_u / self.mem_t * 100) if int(mem_p) <= 0 else int(mem_p)

    def show_used_percent(self):
        print(f"PC with id {self.pc_id} used {self.mem_p} percent of memory.")

    def is_enough_memory(self):
        return False if (100 - self.mem_p) < 10 or (self.mem_t - self.mem_u) < 1073741824 else True


# 4)
local_pc = PC_memory('LEADERSCOMP', 'gleb.obraztsov', '17129029632', '6533365760', '38')


# 5)
local_pc.show_used_percent()
print(local_pc.is_enough_memory())
