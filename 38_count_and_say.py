class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return None
        if n == 1:
            return '1'
        else:
            seq = '1'
            cnt = 1
            for i in range(n-1):
                seq_new = ''
                for j in range(len(seq)):
                    if j < len(seq) - 1:
                        if seq[j+1] == seq[j]:
                            cnt += 1
                        else:
                            seq_new = seq_new + str(cnt) + seq[j]
                            cnt = 1
                    else:
                        seq_new = seq_new + str(cnt) + seq[j]
                        cnt = 1
                seq = seq_new
            return seq
                    