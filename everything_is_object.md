0. type()
1. id()
2. No
3. No
4. Yes
5. No (int is immutable so it will create new object)
6. True (equel value)
7. True (same object)
8. True (equel value)
9. False (diff objects, BUT can be True due to string interning for identical string literals)
10. True (same value)
11. False (diff object)
12. True (same value)
13. True (same object)
14. [1, 2, 3, 4] (linked to same object)
15. [1, 2, 3] (l1 = l1 + [4] creates a new list and reassigns l1 to it, leaving l2 unchanged)
16. 1 (int immutable, also there was no return in fnct)
17. [1, 2, 3, 4] (list is mutable)
18. [1, 2, 3] (fnct changes local var "n" only)
19. dict - True, True, True, False | list - True, True, True , False
20. Tuple
21. Tuple
22. No, its int (to create tuple ", " is needed like a = (1, ))
23. a and b both tuples
24. True (both are int)
25. False (diif objects)
26. True (empty tuples are singleton objects)

#Advanced
270. diff id (a = a + [5] creates new list and assign a to it)
280. same id (a += [4] modifies the list)