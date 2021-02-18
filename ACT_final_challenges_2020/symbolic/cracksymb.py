import angr
import claripy

p = angr.Project("./cracksymb") 

# set the dimension of the input string
pwd_chars = [claripy.BVS(f"pwd_chars{i}", 8) for i in range(24)]
pwd = claripy.Concat( *pwd_chars + [claripy.BVV(b"\n")])

# create a full state
full_state = p.factory.full_init_state(
	add_options = {angr.options.LAZY_SOLVES}, 
	stdin = pwd,
)

# check that all characters are printable
for c in pwd_chars:
    full_state.solver.add(c >= ord('!'))
    full_state.solver.add(c <= ord('~'))

simgr = p.factory.simulation_manager(full_state)

# target address found in ghidra
find_addr  = 0x04033c2

# set the goal address
simgr.explore(find = find_addr)

# print the solution if we reach it
if (len(simgr.found) > 0):
    for found in simgr.found:
        print(found.posix.dumps(0))