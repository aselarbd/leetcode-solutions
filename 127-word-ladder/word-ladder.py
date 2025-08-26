from collections import defaultdict, deque
from string import ascii_letters

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 0
    
        
        word_map = defaultdict(list)
    
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                word_map[pattern].append(word)


                # diff_count = sum(c1 != c2 for c1, c2 in zip(word1, word2))

                # if diff_count==1:
                #     word_map[word1].append(word2)

        queue, visted, i =  deque([(beginWord,0)]), set(beginWord), 0

        while len(queue)>0:
            node,i = queue.popleft()

            if node == endWord:
                return i+1

            for j in range(len(node)):
                p = node[:j]+"*"+node[j+1:]
                
                for word in word_map[p]:
                    if word not in visted:
                        queue.append((word,i+1))
                        visted.add(word)
                
        return 0
        