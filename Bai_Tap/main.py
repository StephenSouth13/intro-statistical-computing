# =============================
# main.py
# Exercises - Python Basics
# =============================

import math
import string


# =====================================================
# Bài 1: Thống kê tần suất từ
# =====================================================

def count_words(text):
    # Chuyển về chữ thường
    text = text.lower()

    # Xóa dấu câu
    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


# =====================================================
# Bài 2: Lọc số nguyên tố
# =====================================================

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def filter_primes(numbers):
    return {num for num in numbers if is_prime(num)}


# =====================================================
# Bài 3: Tìm điểm xa gốc tọa độ nhất
# =====================================================

def farthest_point(points):
    # distance = sqrt(x^2 + y^2)
    return max(points, key=lambda p: math.sqrt(p[0]**2 + p[1]**2))


# =====================================================
# Bài 4: Giao, Hiệu, Hợp của 2 List
# =====================================================

def list_operations(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    intersection = set1 & set2
    union = set1 | set2
    difference = set1 - set2

    return intersection, union, difference


# =====================================================
# Bài 5: Nhóm theo số dư
# =====================================================

def group_by_remainder(numbers, k):
    groups = {}

    for num in numbers:
        remainder = num % k

        if remainder not in groups:
            groups[remainder] = []

        groups[remainder].append(num)

    return groups


# =====================================================
# Bài 6: Tìm cặp số có tổng bằng K
# =====================================================

def find_pairs(numbers, k):
    seen = set()
    pairs = []

    for num in numbers:
        target = k - num

        if target in seen:
            pairs.append((target, num))

        seen.add(num)

    return pairs


# =====================================================
# Bài 7: Chuẩn hóa dữ liệu
# =====================================================

def normalize_data(data):

    # Loại None và số âm
    cleaned = [x for x in data if x is not None and x >= 0]

    if not cleaned:
        return []

    min_val = min(cleaned)
    max_val = max(cleaned)

    # Trường hợp tất cả bằng nhau
    if min_val == max_val:
        return [1.0 for _ in cleaned]

    normalized = [
        (x - min_val) / (max_val - min_val)
        for x in cleaned
    ]

    return normalized


# =====================================================
# Bài 8: Đạo hàm đa thức
# =====================================================
# Đa thức biểu diễn dạng:
# [hệ số, số mũ]
# Ví dụ:
# 3x^2 + 2x + 1
# => [(3,2), (2,1), (1,0)]
# =====================================================

def derivative(polynomial):
    result = []

    for coef, power in polynomial:

        # Đạo hàm hằng số = 0
        if power == 0:
            continue

        new_coef = coef * power
        new_power = power - 1

        result.append((new_coef, new_power))

    return result


def polynomial_to_string(polynomial):

    if not polynomial:
        return "0"

    terms = []

    for coef, power in polynomial:

        if power == 0:
            terms.append(f"{coef}")

        elif power == 1:
            terms.append(f"{coef}x")

        else:
            terms.append(f"{coef}x^{power}")

    return " + ".join(terms)


# =====================================================
# MAIN TEST
# =====================================================

if __name__ == "__main__":

    print("=" * 50)
    print("BÀI 1 - COUNT WORDS")
    print("=" * 50)

    text = "Hello world! Hello Python."
    print(count_words(text))

    print("\n" + "=" * 50)
    print("BÀI 2 - FILTER PRIMES")
    print("=" * 50)

    nums = [1, 2, 3, 4, 5, 6, 7, 11, 15]
    print(filter_primes(nums))

    print("\n" + "=" * 50)
    print("BÀI 3 - FARTHEST POINT")
    print("=" * 50)

    points = [(1, 2), (3, 4), (-10, 1), (0, 0)]
    print(farthest_point(points))

    print("\n" + "=" * 50)
    print("BÀI 4 - LIST OPERATIONS")
    print("=" * 50)

    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]

    inter, union, diff = list_operations(list1, list2)

    print("Intersection:", inter)
    print("Union:", union)
    print("Difference:", diff)

    print("\n" + "=" * 50)
    print("BÀI 5 - GROUP BY REMAINDER")
    print("=" * 50)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(group_by_remainder(nums, 3))

    print("\n" + "=" * 50)
    print("BÀI 6 - FIND PAIRS")
    print("=" * 50)

    nums = [1, 2, 3, 4, 5, 6]
    print(find_pairs(nums, 7))

    print("\n" + "=" * 50)
    print("BÀI 7 - NORMALIZE DATA")
    print("=" * 50)

    data = [10, None, -5, 20, 30]

    print(normalize_data(data))

    print("\n" + "=" * 50)
    print("BÀI 8 - POLYNOMIAL DERIVATIVE")
    print("=" * 50)

    polynomial = [(3, 2), (2, 1), (1, 0)]

    print("Polynomial:")
    print(polynomial_to_string(polynomial))

    derivative_poly = derivative(polynomial)

    print("Derivative:")
    print(polynomial_to_string(derivative_poly))