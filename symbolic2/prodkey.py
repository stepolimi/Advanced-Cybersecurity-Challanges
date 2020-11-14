import angr
import claripy


proj = angr.Project('prodkey')

state = proj.factory.blank_state(addr= 0x00400e07)
input_str = state.solver.BVS("input_string", 8 *30)

initial_state = proj.factory.entry_state(stdin=input_str) # use as stdin
for i in range(0,29): # make sure all chars are printable
	initial_state.solver.add(input_str.get_byte(i) >= 0x20, input_str.get_byte(i) <= 0x7e)

simgr = proj.factory.simulation_manager(initial_state)

simgr.explore(find=0x00400ea8)

if simgr.found:
	found = simgr.found[0]
	print(found.solver.eval(input_str, cast_to = bytes))
