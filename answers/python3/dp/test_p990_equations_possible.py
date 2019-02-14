# coding: utf-8
from collections import defaultdict

__author__ = '代码会说话'
"""
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

 

示例 1：

输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
示例 2：

输出：["b==a","a==b"]
输入：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
示例 3：

输入：["a==b","b==c","a==c"]
输出：true
示例 4：

输入：["a==b","b!=c","c==a"]
输出：false
示例 5：

输入：["c==c","b==d","x!=z"]
输出：true
 

提示：

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] 和 equations[i][3] 是小写字母
equations[i][1] 要么是 '='，要么是 '!'
equations[i][2] 是 '='
"""

class Context:

  def __init__(self):
    self.env = {}
    self.placeholder = 1

  def get(self,name:str):
    return self.env.get(name,None)

  def alloc(self,name:str):
    self.placeholder += 1
    self.env[name] = self.placeholder
    return self.placeholder

  def set(self,name:str,value:int):
    self.env[name] = value

  def __contains__(self, item):
    return item in self.env



class Expr:
  def __init__(self,lhs:str,rhs:str,eq:bool):
    self.lhs = lhs
    self.rhs = rhs
    self.eq = eq
    self.evaluated = False



  def eval(self,ctx:Context):
    lhs_value = ctx.get(self.lhs)
    rhs_value = ctx.get(self.rhs)
    if lhs_value and rhs_value:
      if self.eq:
        return lhs_value == rhs_value
      else:
        return lhs_value != rhs_value
    elif lhs_value or rhs_value:
      if lhs_value:
        if self.eq:
          ctx.set(self.rhs, lhs_value)
        else:
          ctx.alloc(self.rhs)
      else:
        if self.eq:
          ctx.set(self.lhs, rhs_value)
        else:
          ctx.alloc(self.lhs)
    else:
      if self.eq:
        value = ctx.alloc(self.lhs)
        ctx.set(self.rhs, value)
      else:
        ctx.alloc(self.lhs)
        ctx.alloc(self.rhs)

    return True

  @classmethod
  def from_equation(cls,expr:str):
    return Expr(lhs=expr[0], rhs=expr[-1], eq=expr[1] == "=")


class Solution:
  def equationsPossible(self, equations: 'List[str]') -> 'bool':
    ctx = Context()
    exprs = [Expr.from_equation(equation) for equation in equations]
    var_to_exprs = defaultdict(list)
    for expr in exprs:
      var_to_exprs[expr.lhs].append(expr)
      var_to_exprs[expr.rhs].append(expr)
    for expr in exprs:
      related_exprs = [expr]
      while related_exprs:
        cur_expr = related_exprs.pop()
        if cur_expr.evaluated:
          continue
        if not cur_expr.eval(ctx):
          return False
        cur_expr.evaluated = True
        related_exprs.extend(var_to_exprs[cur_expr.lhs])
        related_exprs.extend(var_to_exprs[cur_expr.rhs])
    return True


def test():
  s = Solution()
  # 129 / 175 个通过测试用例
  assert s.equationsPossible(["e!=c","b!=b","b!=a","e==d"]) == False
  assert s.equationsPossible(["c==c","f!=a","f==b","b==c"]) == True
  assert s.equationsPossible(["a==b","b!=a"]) == False
  assert s.equationsPossible(["a==b","b==a"]) == True
  assert s.equationsPossible(["a==b","b==c","a==c"]) == True
  assert s.equationsPossible(["a==b","b!=c","c==a"]) == False
  assert s.equationsPossible(["c==c","b==d","x!=z"]) == True
