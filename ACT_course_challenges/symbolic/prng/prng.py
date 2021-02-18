import claripy

mt = [0]*624
index = 0
mag_array = [0, 0x9908B0DF]

#Attention to conditional memory access: those could be handled by claripy.If and looking at the values from ghidra.
#Attention to shifts to the right: could be handled by claripy.LShR. Shifts to the left are ok
def mag(value):
    global mag_array

    return claripy.If((value == 0), claripy.BVV(mag_array[0], 32), claripy.BVV(mag_array[1],32))

def m_seedRand(seed):
  global index
  global mt
  
  mt[0] = seed & 0xffffffff;
  index = 1;
  while (index < 0x270):
    mt[index] = mt[index -1] * 0x17b5
    index = index + 1
  return

def genRandLong():
  global index
  global mt
  global mag_array

  if ((0x26f < index) or (index < 0)):
    if ((0x270 < index) or (index < 0)):
        m_seedRand(0x1105)


    index = 0
    while (index < 0xe3):
      uVar3 = mt[index + 1]
      mt[index] = mt[index + 0x18d] ^ (uVar3 & 0x7fffffff | mt[index] & 0x80000000 >> 1) ^ mag(uVar3 & 1)
      index = index + 1

    while (index < 0x26f):
      uVar3 = mt[index + 1]
      mt[index] = mt[index + -0xe3] ^ (uVar3 & 0x7fffffff | mt[index] & 0x80000000 >> 1) ^ mag(uVar3 & 1)
      index = index + 1

    uVar3 = mt[0]
    mt[0x26f] = mt[0x18c] ^ (uVar3 & 0x7fffffff | mt[0x26f] & 0x80000000 >> 1) ^ mag(uVar3 & 1)
    index = 0


  iVar1 = index
  index = iVar1 + 1
  uVar2 = mt[iVar1] ^ mt[iVar1] >> 0xb
  uVar2 = uVar2 ^ claripy.LShR(uVar2,7) & 0x9d2c5680
  uVar2 = uVar2 ^ claripy.LShR(uVar2,0xf) & 0xefc60000
  return uVar2 ^ uVar2 >> 0x12


seed = claripy.BVS("seed", 32)

m_seedRand(seed)

for _ in range(1000):
    genRandLong()

leek_sym = genRandLong()

s = claripy.Solver()
s.add(leek_sym == 0x380a23f7)

print(s.eval(seed, 1))

