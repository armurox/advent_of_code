def main():
    a_1 = []
    a_2 = []
    for _ in range(1000):
        a, b = map(int, input().split())
        a_1.append(a)
        a_2.append(b)
    a_1.sort()
    a_2.sort()
    distance_sum = 0
    for i in range(1000):
        distance_sum += abs(a_1[i] - a_2[i])
    print(distance_sum)
    
    
if __name__ == "__main__":
    main()