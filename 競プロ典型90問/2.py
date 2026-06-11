# https://atcoder.jp/contests/typical90/tasks/typical90_b


N = int(input())
if N % 2 == 1: #奇数なら何も出力しない
        pass
else:
      for i in range(2**N): #全ビット探索を行う
             if bin(i).count('1') != N//2: #0の数と1の数が半々である必要がある．
                    continue
             s = []
             for j in range(N): #iの各ビットについて上位bitから調べる
                   bit = ((i >> (N - j - 1)) & 1)
                   if bit == 0: #bitが0なら(，1なら)に置換してsに追加
                           s.append("(")
                   elif bit == 1:
                           s.append(")")
             is_valid = True #正しい()か
             depth = 0 #（の数が）の数より現状何個多く出現しているか
             for t in s:
                   if t == "(":
                           depth = depth + 1
                   elif t == ")":
                           depth = depth - 1
                   if depth < 0:
                           is_valid = False
                           break
             if is_valid:
                print("".join(s))