from collections import Counter
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        common = []
        
        if "" in strs:
            return ""
        
        for n in range(len(strs)-1):
                if n < len(strs) -1 :
                    min_len = min(len(strs[n]), len(strs[n+1]))
                    a = strs[n]
                    b = strs[n+1]
                    for i in range(min_len):
                        if a[i] == b[i]:
                            common += a[i]
                        else:
                            break

        if len(strs) < 3:
                    if (len(common) == 1):
                        return common[0]
                    elif (len(strs) == 1):
                        return strs[0]
                    elif "" in strs:
                        return ""
                    elif (len(common) > 1):
                        return "".join(common)
                    elif (len(common) == 0):
                        return ""
        else:
            counts = Counter(common)
            duplicates = [
                item * (count // (len(strs) - 1))
                for item, count in counts.items()
                if count >= (len(strs) - 1)
            ]
            results = "".join(duplicates)
           
        while results and not all(s.startswith(results) for s in strs):
            results = results[:-1]

        return results
       
     
          
       
                