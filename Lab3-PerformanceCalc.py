# Program to calculate the performance metrics 

print("Pipeline Performance Calculator")

while True:
    # We take the input from the user
    tasks = float(input("Enter the number of tasks: "))
    phases = float(input("Enter the number of phases: "))
    delay = float(input("Enter the latches delay duration: "))


    duration = input("Enter duration separated by space: ")
    durationList = duration.split()
    maxTime = max(durationList)

    print("\n")
    print("All durations: ", durationList)
    print("Maximum time is: ", int(maxTime))
    print("\n")

    # Calculate the NPET
    npet = 0

    for num in durationList:
        npet += int(num)

    npet = npet * tasks

    print("Non pipeline execution time (NPET) is: ", float(npet), "ms")
    
    # Calculate the PET
    thou = int(maxTime) + delay
    pet = (tasks + phases - 1)*(thou)

    print("Pipeline execution time (PET) is: ", pet, "ms")
    print("\n")

    # Calculate the performance
    speedratio = npet/pet
    print("Speed up ratio is: ", float(speedratio))

    frequency = 1/thou
    print("Frequecy value is: ", float(frequency))

    throughput = phases/pet
    print("Throughput is: ", float(throughput))

    efficiency = phases/(tasks + phases - 1)
    print("Efficiency is: ", float(efficiency))

    break
     