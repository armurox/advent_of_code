def main():
    num_safe = 0
    for _ in range(1000):
        level = list(map(int, input().split()))
        used = False
        decreasing = False
        increasing = False
        unsafe = False
        removed = False
        prev = level[0]
        for elem in level[1:]:
            if not decreasing and not increasing:
                if elem > prev and elem - prev <= 3:
                    increasing = True
                elif elem < prev and prev - elem <= 3:
                    decreasing = True
                else:
                    if removed:
                        unsafe = True
                        break
                    else:
                        removed = True
            elif increasing:
                if elem <= prev:
                    unsafe = True
                    break
                elif elem - prev > 3:
                    if removed:
                        unsafe = True
                        break
                    else:
                        removed = True
            elif decreasing:
                if elem >= prev:
                    if removed:
                        unsafe = True
                        break
                    else:
                        removed = True
                elif prev - elem > 3:
                    if removed:
                        unsafe = True
                        break
                    else:
                        removed = True
            prev = elem
        if not unsafe:
            used = True
            num_safe += 1
        removed = False
        decreasing = False
        increasing = False
        unsafe = False
        removed = False
        prev = level[0]
        for elem in level[1:]:
            if not decreasing and not increasing:
                if elem > prev and elem - prev <= 3:
                    increasing = True
                elif elem < prev and prev - elem <= 3:
                    decreasing = True
                else:
                    if removed:
                        unsafe = True
                        break
                    else:
                        removed = True
                        continue
            elif increasing:
                if elem <= prev:
                    unsafe = True
                    break
                elif elem - prev > 3:
                    if removed:
                        unsafe = True
                        break
                    else:
                        removed = True
                        continue
            elif decreasing:
                if elem >= prev:
                    if removed:
                        unsafe = True
                        break
                    else:
                        removed = True
                        continue
                elif prev - elem > 3:
                    if removed:
                        unsafe = True
                        break
                    else:
                        removed = True
                        continue
            prev = elem
        if not unsafe and not used:
            num_safe += 1
    print(num_safe + 3)
                    
    
    
if __name__ == "__main__":
    main()
