"""
pattern_templates.py

Author: Mona Khatami
Goal: Internalize core algorithm patterns for FAANG interviews.

Rules:
- Must be rewritten from memory regularly
- Must stay clean and minimal
- No problem-specific hacks
"""

# =========================================================
# 1. HASH MAP / FREQUENCY COUNTER
# =========================================================

def frequency_counter(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq


# =========================================================
# 2. TWO POINTERS
# =========================================================

def two_pointer_template(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # process arr[left], arr[right]

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1


# =========================================================
# 3. SLIDING WINDOW
# =========================================================

def sliding_window_template(arr):
    left = 0
    window = {}
    best = 0

    for right in range(len(arr)):
        # expand
        val = arr[right]
        window[val] = window.get(val, 0) + 1

        # shrink (replace condition)
        while False:
            left_val = arr[left]
            window[left_val] -= 1
            if window[left_val] == 0:
                del window[left_val]
            left += 1

        # update answer
        best = max(best, right - left + 1)

    return best


# =========================================================
# 4. PREFIX SUM
# =========================================================

def prefix_sum_template(nums):
    prefix = [0] * (len(nums) + 1)

    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]

    return prefix


def prefix_sum_hashmap(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}

    for num in nums:
        prefix += num

        if prefix - k in seen:
            count += seen[prefix - k]

        seen[prefix] = seen.get(prefix, 0) + 1

    return count
