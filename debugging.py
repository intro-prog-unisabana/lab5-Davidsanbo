def get_daily_steps():
    """Return list of daily steps."""
    steps = input("Enter your daily steps for 7 days separated by spaces: ")
    step_list = steps.split()
    step_list = [int(s) for s in step_list]
    return step_list

def total_steps(nums):
    """Return total steps."""
    total = sum(nums)
    return total


def average_steps(total, days=7):
    """Return average steps as int."""
    return total // days


def max_steps(nums):
    """Return max steps."""
    max_val = max(nums)
    return max_val


def min_steps(nums):
    """Return min steps."""
    return min(nums)


def goal_check(nums, goal=10000):
    """Return list of booleans for goal."""
    result = []
    for s in nums:
        if s >= goal:
            result.append(True)
        else:
            result.append(False)
    return result


step_list = get_daily_steps()

total = total_steps(step_list)
average = average_steps(total)
highest = max_steps(step_list)
lowest = min_steps(step_list)
goal_met = goal_check(step_list)

print("Total steps:", total)
print("Average daily steps:", average)
print("Highest steps in a day:", highest)