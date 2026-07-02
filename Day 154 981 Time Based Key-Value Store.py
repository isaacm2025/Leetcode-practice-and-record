'''Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
Example 1:

Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

Output:
[null, null, "happy", "happy", null, "sad"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"
Constraints:

1 <= key.length, value.length <= 100
key and value only include lowercase English letters and digits.
0 <= timestamp <= 10^7
All the timestamps of set are strictly increasing.'''

#bf
class TimeMap:
    def __init__(self):
        self.keyStore = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = {}
        if timestamp not in self.keyStore[key]:
            self.keyStore[key][timestamp] = []
        self.keyStore[key][timestamp].append(value)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        seen = 0
        for time in self.keyStore[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.keyStore[key][seen][-1]
#time complexity: O(n) for get(), O(1) for set()
#space complexity: O(n * m) where n is the number of keys and m is the number of timestamps for each key

#bs(array)
class TimeMap:
    def __init__(self):
        self.keyStore = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
#time complexity: O(log n) for get(), O(1) for set()
#space complexity: O(n * m) where n is the number of keys and m is the number of timestamps for each key