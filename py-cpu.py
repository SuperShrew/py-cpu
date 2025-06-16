
class cpu:
	def __init__(self, ram_size, nv_mem, exec_speed=0, p_ram=False, p_cmd=False, p_count=False):
		self.ram_size = ram_size
		self.nv_mem = nv_mem
		self.exec_speed = exec_speed
		self.p_ram = p_ram
		self.p_cmd = p_cmd
		self.p_count = p_count
		self.ram = [0]*ram_size
		self.acc = 0

	def SET(self, addr, val):
		if type(val) == "<type 'int'>" or type(val) == "<type 'float'>":
			ram[addr] = val
		else:
			ram[addr] = ord(str(val))

	def LDA(self, addr):
		acc = ram[addr]

	def INP(self, type, addr1=None, addr2=None):
		if type == 0:
			acc = int(input("> "))
		else:
			x = addr1
			for i in input("> "):
				ram[x] = i
				if x == addr2:
					break
				else:
					x += 1