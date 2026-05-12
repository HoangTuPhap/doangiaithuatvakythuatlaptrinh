class Solution:
    def findCenter(self, edges):
        # trong star graph, node trung tâm xuất hiện ở mọi cạnh
        # chỉ cần xét 2 cạnh đầu tiên:
        # node chung giữa edges[0] và edges[1] chính là center

        a, b = edges[0]
        c, d = edges[1]

        if a == c or a == d:
            return a  # a xuất hiện ở cả 2 cạnh → là center
        else:
            return b  # ngược lại b là center