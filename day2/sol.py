def check_valid_report(report):
    report = report.split()

    if len(report) <= 1:
        return 1
    
    increasing = None
    for i in range(1, len(report)):
        diff = int(report[i]) - int(report[i-1])
        if i == 1:
            increasing = diff > 0

        if (increasing and diff <= 0) or (not increasing and diff >= 0):
            return 0
        if abs(diff) > 3:
            return 0
        
    return 1

def check_valid_report_with_dampener(report):

    if check_valid_report(report):
        return 1
    
    report = report.split()
    for i in range(1, len(report) - 1):
        damped_report = report[:i] + report[i+1:]
        if check_valid_report(damped_report):
            return 1
    if check_valid_report(report[:-1]):
        return 1
    return 0

if __name__ == "__main__":

    ### PART 1 SOLUTION
    valid_reports = 0
    with open("input.txt", "r") as f:
        for line in f:
            valid_reports += check_valid_report(line)
    print(valid_reports)

    ### PART 2 SOLUTION
    valid_reports = 0
    with open("input.txt", "r") as f:
        for line in f:
            valid_reports += check_valid_report_with_dampener(line)
    print(valid_reports)