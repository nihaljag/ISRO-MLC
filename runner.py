import time
import sim

start_time = time.time()

o,s = sim.main(J = 19000)
print(f"Overshoot = {o}, Settling Time = {s}")
print("--- Executed in %s seconds ---" % (time.time() - start_time))
