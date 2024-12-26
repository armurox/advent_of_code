import re

def main():
    pattern = re.compile(r'mul\([0-9,^(]*\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r'don\'t\(\)')
    _sum = 0
    with open('3.txt') as file:
        for line in file:
            for match in pattern.finditer(line):
                a, b = map(int, match.group()[4:-1].split(','))
                _sum += a * b
        print(_sum)
            
    
    
if __name__ == "__main__":
    main()
