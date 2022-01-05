# Rebrain_Python lesson 13
import os


# 1,2,3,4)
class PercentError(Exception):
    pass

class PC_memory:
    def __init__(self, pc_id, user_name, mem_t, mem_u, mem_p=0):
        self.pc_id = pc_id
        self.user_name = user_name
        try:
            self.mem_t = int(mem_t)
            self.mem_u = int(mem_u)
            if self.mem_t < 0 or self.mem_u < 0 or self.mem_u > self.mem_t: raise ValueError 
        except ValueError:
            print('wrong memory value, default value used')
            self.mem_t = 107374182400
            self.mem_u = 0
            self.mem_p = 0
        else:
            try:
                self.mem_p = float(mem_p)
                if self.mem_p < 0 or self.mem_p > 100:
                    raise PercentError('Percent value must be between 0 and 100')
                else:
                    self.mem_p = float(int(self.mem_u / self.mem_t * 100) if int(mem_p) <= 0 else int(mem_p))
            except ValueError:
                print('wrong percent value, value calculated automatically')
                self.mem_p = float(int(self.mem_u / self.mem_t * 100))

    def show_used_percent(self):
        print(f"PC with id {self.pc_id} used {self.mem_p} percent of memory.")

    def is_enough_memory(self):
        return False if (100 - self.mem_p) < 10 or (self.mem_t - self.mem_u) < 1073741824 else True

local_pc = PC_memory('LEADERSCOMP', 'gleb.obraztsov', '10737418240', '1073741824', '2')
print(local_pc.mem_t, local_pc.mem_u, local_pc.mem_p)
