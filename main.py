# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    endOfProcess=[]
    for i in range(n):
        endOfProcess.append(data[0])
        output.append([i,0])
        del data[0]
    while len(data)!=0:
        # Thread which is about to end its process
        index = endOfProcess.index(min(endOfProcess))
        nextJobTime=data[0]
        del data[0]
        output.append([index, min(endOfProcess)])
        endOfProcess[index]=endOfProcess[index]+nextJobTime
    print(output)
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    entry = input()
    if entry[0]=="I":
        line1=input()
        n = int(line1[0])
        m = int(line1[-1])
        data = list(map(int, input().split()))
        if len(data)!=m:
            print("Job count doesn't match")
            exit()
        if n>m:
            print("More threads than jobs! Excess ignored.")
            n=m
        result = parallel_processing(n, m, data)
        for thread, task in result:
            print(thread, task)
    else:
        print("Incorrect entry")

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
