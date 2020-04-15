class Solution:
    """
    Converting a string into a zig zag pattern. For example, PAYPALISHIRING will become:
        P   A   H   N
        A P L S I I G
        Y   I   R
    This could be read line by line as:
    "PAHNAPLSIIGYIR"

    What we want the function to return is indeed:
    "PAHNAPLSIIGYIR"

    Approach:
    Each row contains a string, and the rows can be made by going through each letter of
    the input string, and putting that character into a row. We then move on to the next row.
    Once we reach the last row, we go backwards and begin working our way backup. When we reach
    the beginning, we proceed forwards again.

    Broken down into simple steps:
    Create an array for each output row

    Iterate through each letter of the input string:
        1) Drop off the letter in the corresponding array
        2) Move to the next array
            a) The next array could either be forwards or backwards, we need to keep track of this
        3) If we reach the end or beginning, we change directions
    """
    def convert(self, s: str, numRows: int) -> str:
        rows = []
        for i in range(numRows):
            rows.append([])
        index = 0
        forward = True
        end = numRows - 1
        for char in s:
            # 3)
            if index == 0:
                forward = True
            if index == end:
                forward = False

            # 1)
            rows[index].append(char)

            # 2)
            index = self.moveAlong(index, forward, end)
        retStr = ""
        for i in range(numRows):
            retStr += "".join(rows[i])
        return retStr
        
    """
    A helper function to move the index in the right direction, and also keeps it contained
    to prevent us from exiting the bounds of the array
    """
    def moveAlong(self, index, forward, end):
        if forward:
            return min(index + 1, end)
        else:
            return max(index - 1, 0)

solver = Solution()
inpStr = "PAYPALISHIRING"
numRows = 3

ans = solver.convert(inpStr, numRows)
print(ans)
