class Solution:

    def encode(self, strs: List[str]) -> str:
        res_chars = []
        res_chars.append(chr(len(strs))) # less than 100
        for string in strs:
            # Append length of each string
            res_chars.append(chr(len(string))) # less than 200
        for string in strs:
            for c in string:
                res_chars.append(c)
        
        return "".join(res_chars)

    def decode(self, s: str) -> List[str]:
        # Read in length of the list
        num_strs = ord(s[0])
        str_lens = []
        for i in range(1, num_strs + 1):
            str_lens.append(ord(s[i])) # get length of each string
        
        read_index = num_strs + 1

        current_string = []
        strings = []

        for string_length in str_lens:
            for i in range(string_length):
                current_string.append(s[read_index])
                read_index += 1

            strings.append("".join(current_string))
            current_string = []


        return strings
            

