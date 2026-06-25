# =============================================================================
# PART A – Frequency Counter
# =============================================================================

def freq_counter(arr):
    """Returns a dictionary with the frequency of each integer in arr."""
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


# --- Part A: Task 1 – Build the frequency dictionary ---
arr = [1, 2, 3, 2, 1, 1, 4]
freq = freq_counter(arr)
print("=" * 55)
print("PART A – Frequency Counter")
print("=" * 55)
print(f"Input  : {arr}")
print(f"Output : {freq}")

# --- Part A: Task 2 – Most frequent element ---
most_frequent = max(freq, key=lambda k: freq[k])
print(f"\nMost frequent element : {most_frequent}  (appears {freq[most_frequent]} times)")

# --- Part A: Task 3 – Elements that appear exactly once ---
unique_elements = [k for k, v in freq.items() if v == 1]
print(f"Elements appearing exactly once : {unique_elements}")


# =============================================================================
# PART B – Anagram Check
# =============================================================================

def is_anagram(s1, s2):
    """
    Returns True if s1 and s2 are anagrams of each other.
    Bonus: strips spaces and converts to lowercase before comparing,
    so it handles mixed case and whitespace correctly.
    """
    # Bonus handling: normalise both strings
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Build frequency maps for each string
    def build_freq(s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        return freq

    return build_freq(s1) == build_freq(s2)


print("\n" + "=" * 55)
print("PART B – Anagram Check")
print("=" * 55)

test_pairs = [
    ("listen",   "silent"),
    ("triangle", "integral"),
    ("apple",    "pale"),
    ("rat",      "car"),
    # Bonus: spaces & uppercase
    ("Astronomer", "Moon starer"),
    ("School master", "The classroom"),
]

for s1, s2 in test_pairs:
    result = is_anagram(s1, s2)
    print(f'  is_anagram("{s1}", "{s2}") → {result}')


# =============================================================================
# PART C – Two Sum
# =============================================================================

def two_sum(nums, target):
    """
    Finds two indices i and j such that nums[i] + nums[j] == target.

    Strategy – Hash Map / O(n):
      For every number we visit, we calculate its 'complement':
          complement = target - nums[i]
      The complement is the exact value we NEED to have already seen so
      that the two numbers add up to 'target'.  We store each number we
      visit in a dict {value: index}.  If the complement is already in
      that dict, we found our pair instantly – no second loop required,
      giving us O(n) time complexity.
    """
    seen = {}          # maps { number : its index }

    for i, num in enumerate(nums):
        complement = target - num   # the value we need to pair with num

        if complement in seen:
            return [seen[complement], i]   # pair found

        seen[num] = i   # store current number for future lookups

    return []   # no solution found


print("\n" + "=" * 55)
print("PART C – Two Sum  (O(n) hash-map approach)")
print("=" * 55)

test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4],      6),
    ([3, 3],         6),
]

for nums, target in test_cases:
    result = two_sum(nums, target)
    print(f"  two_sum({nums}, target={target}) → {result}")


# =============================================================================
# PART D – Bonus / Challenge
# =============================================================================

print("\n" + "=" * 55)
print("PART D – Bonus / Challenge")
print("=" * 55)

# ------------------------------------------------------------------
# D-1  Longest Substring Without Repeating Characters (sliding window)
# ------------------------------------------------------------------

def length_of_longest_substring(s):
    """
    Uses a sliding window [left, right] and a hash set to track the
    characters currently inside the window.  Whenever we see a duplicate
    we shrink the window from the left until the duplicate is gone.
    Time: O(n)  Space: O(min(n, alphabet))
    """
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Shrink window until the duplicate is removed
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


print("\n[D-1] Longest Substring Without Repeating Characters")
for s, expected in [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]:
    result = length_of_longest_substring(s)
    print(f'  "{s}" → {result}  (expected {expected})')


# ------------------------------------------------------------------
# D-2  First Non-Repeating Character
# ------------------------------------------------------------------

def first_non_repeating(s):
    """
    Build a frequency map in one pass, then scan the string again to
    find the first character whose count is exactly 1.
    Time: O(n)
    """
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return ""   # no non-repeating character found


print("\n[D-2] First Non-Repeating Character")
for s, expected in [("leetcode", "l"), ("aabb", ""), ("loveleetcode", "v")]:
    result = first_non_repeating(s)
    print(f'  first_non_repeating("{s}") → "{result}"  (expected "{expected}")')


# ------------------------------------------------------------------
# D-3  Group Anagrams Together
# ------------------------------------------------------------------

def group_anagrams(words):
    """
    Sort each word's letters → identical sorted strings for anagrams.
    Use that sorted string as a hash map key to group the original words.
    Time: O(n * k log k)  where k = max word length.
    """
    groups = {}
    for word in words:
        key = "".join(sorted(word))      # e.g. "eat" → "aet"
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())


print("\n[D-3] Group Anagrams Together")
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = group_anagrams(words)
print(f"  Input  : {words}")
print(f"  Output : {groups}")


# ------------------------------------------------------------------
# D-4  Custom HashTable with Chaining
# ------------------------------------------------------------------

class HashTable:
    """
    A hash table that uses separate chaining (each bucket holds a list
    of (key, value) pairs) to handle collisions.

    Methods:
        insert(key, value)  – add or update a key-value pair  O(1) avg
        get(key)            – retrieve the value for a key    O(1) avg
        delete(key)         – remove a key-value pair         O(1) avg
    """

    def __init__(self, capacity=16):
        self._capacity = capacity
        self._buckets  = [[] for _ in range(self._capacity)]
        self._size     = 0

    # ── internal helpers ──────────────────────────────────────────

    def _hash(self, key):
        """Map a key to a bucket index."""
        return hash(key) % self._capacity

    def _find(self, bucket, key):
        """Return (index, pair) if key exists in bucket, else (-1, None)."""
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return i, (k, v)
        return -1, None

    # ── public API ────────────────────────────────────────────────

    def insert(self, key, value):
        """Insert or update key → value."""
        bucket = self._buckets[self._hash(key)]
        idx, pair = self._find(bucket, key)
        if idx == -1:
            bucket.append((key, value))   # new key
            self._size += 1
        else:
            bucket[idx] = (key, value)    # update existing key

    def get(self, key):
        """Return the value for key, or None if not found."""
        bucket = self._buckets[self._hash(key)]
        _, pair = self._find(bucket, key)
        return pair[1] if pair else None

    def delete(self, key):
        """Remove key from the table. Returns True if deleted, False if missing."""
        bucket = self._buckets[self._hash(key)]
        idx, pair = self._find(bucket, key)
        if idx == -1:
            return False
        bucket.pop(idx)
        self._size -= 1
        return True

    def __len__(self):
        return self._size

    def __repr__(self):
        items = []
        for bucket in self._buckets:
            items.extend(bucket)
        return "HashTable({" + ", ".join(f"{k!r}: {v!r}" for k, v in items) + "})"


print("\n[D-4] Custom HashTable with Chaining")
ht = HashTable()

# insert
ht.insert("name",  "Alice")
ht.insert("age",   30)
ht.insert("city",  "Delhi")
print(f"  After 3 inserts  : {ht}")

# get
print(f"  get('name')      : {ht.get('name')}")
print(f"  get('missing')   : {ht.get('missing')}")

# update
ht.insert("age", 31)
print(f"  After update age : {ht.get('age')}")

# delete
ht.delete("city")
print(f"  After delete city: {ht}")
print(f"  Table size       : {len(ht)}")

print("\n" + "=" * 55)
print("All parts complete.")
print("=" * 55)