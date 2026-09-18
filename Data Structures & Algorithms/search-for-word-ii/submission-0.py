class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Add all the words to Trie
        for word in words:
            root.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        visit = set()

        def dfs(r, c, node, ongoing_word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
            (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r, c))

            # move to the children of the current Trie Node
            node = node.children[board[r][c]]

            # increment the ongoing word
            ongoing_word += board[r][c]

            # we found a word here
            if node.isWord:
                res.add(ongoing_word)

            dfs(r+1, c, node, ongoing_word)
            dfs(r-1, c, node, ongoing_word)
            dfs(r, c+1, node, ongoing_word)
            dfs(r, c-1, node, ongoing_word)

            # backtrack visit
            visit.remove((r,c))

        # We start iteration from each character in board
        # because word could be starting anywhere
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res) 

        