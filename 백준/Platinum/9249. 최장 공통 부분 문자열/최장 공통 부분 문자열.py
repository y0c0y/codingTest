import sys

BASE = 256
MOD = 10**9 + 7


def rolling_hash(s, length):
    current_hash = 0
    for i in range(length):
        current_hash = (current_hash * BASE + ord(s[i])) % MOD

    hashes = {current_hash: i for i in range(length)}

    highest_power = pow(BASE, length - 1, MOD)
    for i in range(1, len(s) - length + 1):
        current_hash = (current_hash - ord(s[i - 1]) * highest_power) % MOD
        current_hash = (current_hash * BASE + ord(s[i + length - 1])) % MOD
        hashes[current_hash] = i + length - 1

    return hashes


def can_construct(common_length, s1, s2):
    s1_hashes = rolling_hash(s1, common_length)
    s2_hashes = rolling_hash(s2, common_length)

    for hash_val, idx in s2_hashes.items():
        if (
            hash_val in s1_hashes
            and s1[s1_hashes[hash_val] - common_length + 1 : s1_hashes[hash_val] + 1]
            == s2[idx - common_length + 1 : idx + 1]
        ):
            return True, s2[idx - common_length + 1 : idx + 1]
    return False, ""


sentence1 = sys.stdin.readline().strip()
sentence2 = sys.stdin.readline().strip()

left, right = 0, min(len(sentence1), len(sentence2))
answer_length = 0
lcs_string = ""

while left <= right:
    mid = (left + right) // 2
    exists, candidate_string = can_construct(mid, sentence1, sentence2)
    if exists:
        answer_length = mid
        lcs_string = candidate_string
        left = mid + 1
    else:
        right = mid - 1

print(answer_length)
print(lcs_string)
