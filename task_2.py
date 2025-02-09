"""
Результати:
BFS:
Birmingham Nottingham Stafford Sheffield Derby Stoke-on-Trent Leeds Liverpool Manchester Southport 

DFS:
Birmingham Nottingham Derby Stafford Stoke-on-Trent Liverpool Manchester Leeds Sheffield Southport

Висновок: результати пошуку в ширину відрізняються від результатів пошуку в глибину через різницю 
у алгоритмі обходу графа.

Пошук у глибину (DFS) виконується шляхом відвідування вершини, а потім за допомогою стеку відвідує 
всі сусідні вершини, які ще не були відвідані.

Пошук у ширину (BFS) відрізняється від DFS тим, що він відвідує всі вершини на певному рівні перед
тим, як перейти до наступного рівня. 
"""

from algorithm.bfs import bfs_iterative
from algorithm.dfs import dfs_iterative
from task_1 import G

print("BFS:")
bfs_iterative(G, "Birmingham")

print("\n")

print("DFS:")
dfs_iterative(G, "Birmingham")
