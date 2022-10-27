class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        mapping_target = {}
        mapping_source = {}
        for i in range(len(indices)):
            mapping_target[indices[i]] = targets[i]
            mapping_source[indices[i]] = sources[i]
        
        new_str = ""
        pointer = 0
        s_len = len(s)
        while pointer < s_len:
            if pointer not in mapping_target:
                new_str += s[pointer:pointer+1]
                pointer += 1
            elif s[pointer:pointer+len(mapping_source[pointer])] == mapping_source[pointer]:
                new_str += mapping_target[pointer]
                pointer += len(mapping_source[pointer])
            else:
                new_str += s[pointer:pointer+1]
                pointer += 1
        return  new_str