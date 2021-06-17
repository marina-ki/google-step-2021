# best fit

<a href="./malloc_challenge/real_malloc/best_fit.c">コード</a>

```
Challenge 1: simple malloc => my malloc
Time: 6 ms => 1225 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 5 ms => 457 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 109 ms => 792 ms
Utilization: 8% => 50%
==================================
Challenge 4: simple malloc => my malloc
Time: 21293 ms => 8577 ms
Utilization: 15% => 71%
==================================
Challenge 5: simple malloc => my malloc
Time: 13411 ms => 7360 ms
Utilization: 15% => 74%
==================================
```

# worst fit

```
Challenge 1: simple malloc => my malloc
Time: 8 ms => 1267 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 6 ms => 458 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 107 ms => 55917 ms
Utilization: 8% => 4%
==================================
```

時間も大幅に大きくなった

# 隣接空スロット連結, free のリストをアドレス順に連結

```
Challenge 1: simple malloc => my malloc
Time: 6 ms => 22 ms
Utilization: 70% => 71%
==================================
Challenge 2: simple malloc => my malloc
Time: 5 ms => 17 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 112 ms => 36 ms
Utilization: 8% => 38%
==================================
Challenge 4: simple malloc => my malloc
Time: 18119 ms => 3796 ms
Utilization: 15% => 73%
==================================
Challenge 5: simple malloc => my malloc
Time: 11764 ms => 1631 ms
Utilization: 15% => 75%
==================================
```
