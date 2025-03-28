import numpy as np

exo1 = np.array([38, 24, 32, 45, 40])
exo2 = np.array([23, 25, 31, 29, 15])
exo3 = np.array([26, 34, 30, 28, 37])

points = np.array([15, 8, 13, 16, 10])

matrix = np.array([exo1,exo2,exo3])

def student_total_time(matrix):

    total_times = []

    for i in range(len(matrix[0, :])):
    
        time = 0
    
        for n in range(len(matrix[:,0])):
    
            time += int(matrix[n,i])
    
        total_times.append(time)
    
    return total_times


#total time 1h45 minutes
def remaining_time(matrix, total_time: float):
    
    time = total_time*(60**2)
    
    timings = student_total_time(matrix) #working"
    
    remaining = []
    
    for i in range(len(timings)):
    
        remaining_time = time - timings[i]*60
    
        remaining.append(remaining_time)
    
    return remaining

def best_scores(points, time_remaining: list):
    
    best_scores = []
    
    for i in range(len(points)):
    
        score = points[i]*time_remaining[i]
    
        best_scores.append(score)
    
    maximum_value = np.max(best_scores)
    
    return maximum_value

#print(best_scores(points, remaining_time(matrix, 1.75)))
print(type(matrix))