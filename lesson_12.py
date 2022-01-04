# Rebrain_Python lesson 12
import os


# 1)
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
local_pc = PC_memory('LEADERSCOMP', 'gleb.obraztsov', '17129029632', '6533365760', '38')


# 2,3)
class PC_advanced(PC_memory):
    def __init__(self, pc_id, user_name, mem_t, mem_u, ld_avg_1m, ld_avg_15m, mem_p=0):
        super().__init__(pc_id, user_name, mem_t, mem_u, mem_p=mem_p)
        self.ld_avg_1m = ld_avg_1m
        self.ld_avg_15m = ld_avg_15m
    def is_overloaded(self):
        return True if self.ld_avg_1m > self.ld_avg_15m * 3 else False
    def __call__(self, line='memory'):
        if str(line) == 'memory':
            return self.is_enough_memory 
        elif str(line) == 'load': 
            return self.is_overloaded
        else:
            return None


# 4,5,6)
pc_adv = PC_advanced('LEADERSCOMP', 'gleb.obraztsov', '17129029632', '6533365760', 2, 1, '38')
print(f"5: {pc_adv.is_overloaded()}")
class_as_func = pc_adv()
print(f"6: {class_as_func()}")     
